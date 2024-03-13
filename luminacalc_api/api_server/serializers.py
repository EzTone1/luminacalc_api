# serializers.py
from rest_framework import serializers
from .models import Order, Window, Construction, Lamination, Glazing, Profile, Configuration

class WindowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Window
        fields = '__all__'

class StructureSerializer(serializers.ModelSerializer):
    windows = WindowSerializer(many=True, read_only=True)

    class Meta:
        model = Construction
        fields = '__all__'

class LaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lamination
        fields = '__all__'

class GlazingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Glazing
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    structures = StructureSerializer(many=True, read_only=True)
    configurations = ConfigurationSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'