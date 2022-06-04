# Generated by Django 2.2.16 on 2022-06-03 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_auto_20220603_1826'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='genretitle',
            constraint=models.UniqueConstraint(fields=('title', 'genre'), name='unique_title_genre'),
        ),
    ]