from netbox.plugins import PluginTemplateExtension
from . import models, tables
from dcim.models import Device


class DeviceRawData(PluginTemplateExtension):
    model = 'dcim.device'

    def right_page(self):
        if not isinstance(self.context['object'], Device):
            return ''
            
        return self.render('netbox_textdatastore/device_incl.html', extra_context={
            'table': tables.TextDataObjectTable(models.TextDataObject.objects.filter(device=self.context['object'])),
        })


template_extensions = [DeviceRawData]
