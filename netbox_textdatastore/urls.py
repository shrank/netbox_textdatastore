from django.urls import path

from netbox.views.generic import ObjectChangeLogView

from . import views
from .models import TextDataObject


urlpatterns = (

    # modules
    path('data/', views.TextDataObjectListView.as_view(), name='TextDataObject_list'),
    path('data/<int:pk>/', views.TextDataObjectView.as_view(), name='TextDataObject'),
    path('data/add/', views.TextDataObjectEditView.as_view(), name='TextDataObject_add'),
    path('data/<int:pk>/edit/', views.TextDataObjectEditView.as_view(), name='TextDataObject_edit'),
    path('data/<int:pk>/delete/', views.TextDataObjectDeleteView.as_view(), name='TextDataObject_delete'),
    path('data/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='TextDataObject_changelog', kwargs={
        'model': TextDataObject
    }),

)
