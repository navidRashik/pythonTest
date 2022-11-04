from dataclasses import fields
from django_filters import rest_framework as filters
from .models import Movie


# We create filters for each field we want to be able to filter on
class MovieFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains', field_name='title')
    genre = filters.CharFilter(lookup_expr='icontains', field_name='genre')
    year = filters.NumberFilter(lookup_expr='exact', field_name='year')
    year__gt = filters.NumberFilter(lookup_expr='gt', field_name='year')
    year__lt = filters.NumberFilter(field_name='year', lookup_expr='lt')
    creator__username = filters.CharFilter(
        lookup_expr='icontains', field_name='creator__username')

    class Meta:
        model = Movie
        fields = ['title', 'genre', 'year', 'year__gt',
                  'year__lt', 'creator__username']
