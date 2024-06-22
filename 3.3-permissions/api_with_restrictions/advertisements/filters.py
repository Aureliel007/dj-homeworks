from django_filters import rest_framework as filters
from django_filters import DateFromToRangeFilter, ChoiceFilter

from advertisements.models import Advertisement, AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    created_at = DateFromToRangeFilter()
    status = ChoiceFilter(choices=AdvertisementStatusChoices.choices)
    is_favorite = filters.BooleanFilter(method='filter_is_favorite')

    class Meta:
        model = Advertisement
        fields = ['created_at', 'status', 'creator']

    def filter_is_favorite(self, queryset, name, value):
        user = self.request.user
        if value and not user.is_anonymous:
            return queryset.filter(favorited_by=user)
        return queryset