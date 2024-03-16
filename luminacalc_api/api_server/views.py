# views.py
from rest_framework import viewsets
from .models import Order, Window, Construction, Lamination, Glazing, Profile, Configuration
from .serializers import OrderSerializer, WindowSerializer, ConstructionSerializer, LaminationSerializer, GlazingSerializer, ProfileSerializer, ConfigurationSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class WindowViewSet(viewsets.ModelViewSet):
    queryset = Window.objects.all()
    serializer_class = WindowSerializer

class ConstructionViewSet(viewsets.ModelViewSet):
    queryset = Construction.objects.all()
    serializer_class = ConstructionSerializer

class LaminationViewSet(viewsets.ModelViewSet):
    queryset = Lamination.objects.all()
    serializer_class = LaminationSerializer

class GlazingViewSet(viewsets.ModelViewSet):
    queryset = Glazing.objects.all()
    serializer_class = GlazingSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ConfigurationViewSet(viewsets.ModelViewSet):
    queryset = Configuration.objects.all()
    serializer_class = ConfigurationSerializer