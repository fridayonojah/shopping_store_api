from django.urls import path
from rest_framework import permissions
from rest_framework_nested import routers
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from . import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet)
router.register('customers', views.CustomerViewSet)
router.register('orders', views.OrderViewSet, basename='orders')

products_router = routers.NestedDefaultRouter(
    router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet,
                         basename='product-reviews')

products_router.register('images', views.ProductImageViewSet, basename='product-images')

carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', views.CartItemViewSet, basename='cart-items')


# Documentation
schema_view = get_schema_view(
    openapi.Info(
        title="Shoping Store API",
        default_version="v1",
        description="API backend for shopping store project.",
        terms_of_service="https://cribr.com/permissions",
        contact=openapi.Contact(email="calebseyi123@gmail.com"),
        license=openapi.License(name="BSD License")
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

swagger_documentation_endpoint = path(
    'documentation/', schema_view.with_ui( 
        'swagger', cache_timeout=0), name='schema-swagger'),


# URLConf
urlpatterns = router.urls + products_router.urls + carts_router.urls + list(swagger_documentation_endpoint)
