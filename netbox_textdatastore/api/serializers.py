from netbox.api.serializers import NetBoxModelSerializer
from ..models import TextDataObject

# TD: add device_name

class TextDataObjectSerializer(NetBoxModelSerializer):

    class Meta:
        model = TextDataObject
        fields = (
            'pk', 'name', 'device', 'last_updated', 'hash', 'data'
        )
