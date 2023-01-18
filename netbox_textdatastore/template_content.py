from extras.plugins import PluginTemplateExtension
from . import models, tables


class DeviceRawData(PluginTemplateExtension):
    model = 'dcim.device'

    def right_page(self):
        return self.render('netbox_textdatastore/device_incl.html', extra_context={
            'table': tables.TextDataObjectTable(models.TextDataObject.objects.filter(device=self.context['object'])),
        })


template_extensions = [DeviceRawData]
