import django_filters

from photo.models import Photo


class PhotoFilter(django_filters.FilterSet):
    date = django_filters.IsoDateTimeFromToRangeFilter()
    lat = django_filters.RangeFilter()
    lon = django_filters.RangeFilter()
    location_name = django_filters.CharFilter(lookup_expr='iexact')
    people_name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Photo
        fields = ('date', 'people_name', 'location_name', 'lon', 'lat',)