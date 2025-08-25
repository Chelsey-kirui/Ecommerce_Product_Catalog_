from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from EcommerceCatalog.views import ProductViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
