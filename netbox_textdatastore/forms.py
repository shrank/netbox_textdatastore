from django.forms import CharField
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import DynamicModelChoiceField, TagFilterField
from dcim.models import Device
from .models import TextDataObject


class TextDataObjectForm(NetBoxModelForm):

    device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        required=True
    )

    class Meta:
        model = TextDataObject
        fields = ('name', 'device', 'hash','data', 'tags')

        help_texts = {
            'hash': "Hash of the data to detect changes",
        }

class TextDataObjectFilterForm(NetBoxModelFilterSetForm):
    model = TextDataObject
    name = CharField(
        required=False
    )
    device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        required=False
    )
    data = CharField(
        required=False
    )
    tag = TagFilterField(model)
