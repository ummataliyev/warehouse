from django.urls import path

from apps.material import views

urlpatterns = [
    path(
        'api/product-materials/',
        views.ProductMaterialsView.as_view(),
        name='product-materials'
    ),
]
