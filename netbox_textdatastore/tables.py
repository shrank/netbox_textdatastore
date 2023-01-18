import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import TextDataObject


class TextDataObjectTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )

    device = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = TextDataObject
        fields = ('pk', 'name', 'last_updated', 'device', 'actions')
        default_columns = ('name', 'last_updated', 'device')
