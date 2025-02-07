import django_filters
from .models import NewsItem

class NewsItemFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')  # Case-insensitive partial match
    content = django_filters.CharFilter(field_name='content', lookup_expr='icontains')  # Case-insensitive partial match

    class Meta:
        model = NewsItem
        fields = ['title', 'content']