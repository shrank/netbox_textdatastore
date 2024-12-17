from netbox.views import generic
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from . import models, tables, forms, filtersets


class TextDataObjectView(generic.ObjectView):
    queryset = models.TextDataObject.objects.all()


class TextDataObjectListView(generic.ObjectListView):
    queryset = models.TextDataObject.objects.annotate()
    table = tables.TextDataObjectTable
    filterset = filtersets.TextDataObjectFilterSet
    filterset_form = forms.TextDataObjectFilterForm

class TextDataObjectDeleteView(generic.ObjectDeleteView):
    queryset = models.TextDataObject.objects.all()

class TextDataObjectEditView(generic.ObjectEditView):
    queryset = models.TextDataObject.objects.all()
    form = forms.TextDataObjectForm


class TextDataObjectViewDownload(generic.ObjectView):
    queryset = models.TextDataObject.objects.all()

    def get(self, request, **kwargs):
      object = self.get_object(**kwargs)
      response = HttpResponse(content_type='text/plain')
      response.write(object.data)
      response['Content-Disposition'] = f'attachment; filename="{object.device.name}_{object.name}.txt"'
      return response