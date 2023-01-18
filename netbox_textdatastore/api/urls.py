from netbox.api.routers import NetBoxRouter
from . import views


app_name = 'netbox_textdatastore'

router = NetBoxRouter()
router.register('data', views.TextDataObjectViewSet)

urlpatterns = router.urls
