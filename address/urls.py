from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('addresses', views.AddressViewSet, basename='addresses')
router.register('city', views.CityViewSet, basename='city')
router.register('state', views.StateViewSet, basename='state')
urlpatterns = [
]
urlpatterns += router.urls
