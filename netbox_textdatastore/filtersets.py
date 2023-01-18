import django_filters
from netbox.filtersets import NetBoxModelFilterSet
from dcim.models import Device
from .models import TextDataObject


class TextDataObjectFilterSet(NetBoxModelFilterSet):
    device_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Device.objects.all(),
        label='Device (ID)',
    )
    device = django_filters.ModelMultipleChoiceFilter(
        field_name='device__name',
        queryset=Device.objects.all(),
        to_field_name='name',
        label='Device (name)',
    )

    class Meta:
        model = TextDataObject
        fields = ['id', 'name', 'hash']
