import django_filters
from .models import Topic

class TopicFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_expr='exact')
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Topic
        fields = ['id','title']
