from netbox.views import generic
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
