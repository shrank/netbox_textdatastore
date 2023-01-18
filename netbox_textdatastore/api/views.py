from netbox.api.viewsets import NetBoxModelViewSet

from .. import models, filtersets
from .serializers import TextDataObjectSerializer


class TextDataObjectViewSet(NetBoxModelViewSet):
    queryset = models.TextDataObject.objects.prefetch_related('device')
    serializer_class = TextDataObjectSerializer
    filterset_class = filtersets.TextDataObjectFilterSet
