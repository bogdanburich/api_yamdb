from rest_framework import filters, mixins, viewsets
from users.permissions import Admin, ReadOnly, Superuser
from django_filters.rest_framework import DjangoFilterBackend


class ListCreateDeleteViewSet(
    mixins.ListModelMixin, mixins.CreateModelMixin,
    mixins.DestroyModelMixin, viewsets.GenericViewSet
):
    permission_classes = [Superuser | Admin | ReadOnly]
    lookup_field = 'slug'
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('name', 'slug')


class ListCreateRetrieveUpdateDeleteViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    filter_backends = (filters.SearchFilter,)
