from django.db import models
from django.urls import reverse

from netbox.models import NetBoxModel
from dcim.models import Device


class TextDataObject(NetBoxModel):

    name = models.CharField(
        max_length=100,
        default="device config"
    )

    data = models.TextField(
        blank=True,
        default=""
    )

    hash = models.CharField(
        max_length=100,
        default="",
        blank=True,
    )

    device = models.ForeignKey(
        to=Device,
        on_delete=models.CASCADE,
        related_name='textdata',
    )

    class Meta:

        ordering = ('device', 'name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_textdatastore:TextDataObject', args=[self.pk])
