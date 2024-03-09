from django.urls import path
from django.urls import include

from rest_framework.routers import DefaultRouter

from apps.material import views


router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'raw_materials', views.RawMaterialViewSet)
router.register(r'product_materials', views.RawMaterialViewSet)
router.register(r'warehouses', views.WarehouselViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
