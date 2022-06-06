import datetime
from rest_framework import serializers

from reviews.models import (
    Category,
    Genre,
    Title,
    Review,
    Comment,
)


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'slug')


class GenresSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name', 'slug')


class TitlesSerializer(serializers.ModelSerializer):
    category = CategoriesSerializer(read_only=True)
    genre = GenresSerializer(read_only=True, many=True)

    class Meta:
        model = Title
        fields = '__all__'

    def validate_genre(self, value):
        for slug in value:
            if Genre.objects.get(slug=slug).exists():
                continue
            return value
        raise serializers.ValidationError(
            "Указанный жанр не существует"
        )

    def validate_category(self, value):
        if (
            self.request.data.get('category')
            and Category.objects.get(slug=value).exists()
        ):
            return value
        raise serializers.ValidationError(
            "Указанная категория не существует"
        )

    def validate_year(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError(
                'Год выпуска не может быть больше текущего'
            )
        return value


class ReviewsSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date')
        read_only_fields = ('title',)

    def validate(self, data):
        if self.context['request'].method == 'POST':
            title_id = (
                self.context['request'].parser_context['kwargs']['title_id']
            )
            user = self.context['request'].user
            if user.reviews.get(title_id=title_id).exist():
                raise serializers.ValidationError(
                    'Возможно оставить только один отзыв на произведение'
                )
        return data

    def validate_score(self, value):
        if 0 >= value >= 10:
            raise serializers.ValidationError(
                'Оценка за пределами допустимого диапазона'
            )
        return value


class CommentsSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'text', 'pub_date')
