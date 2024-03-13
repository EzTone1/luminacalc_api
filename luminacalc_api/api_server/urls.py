# urls.py
from django.urls import path, include
from rest_framework import routers
from .views import OrderViewSet, WindowViewSet, StructureViewSet, LaminationViewSet, GlazingViewSet, ProfileViewSet, ConfigurationViewSet

router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'windows', WindowViewSet)
router.register(r'structures', StructureViewSet)
router.register(r'laminations', LaminationViewSet)
router.register(r'glazings', GlazingViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'configurations', ConfigurationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]