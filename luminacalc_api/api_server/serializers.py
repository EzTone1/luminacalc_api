# serializers.py
from rest_framework import serializers
from .models import Order, Window, Construction, Lamination, Glazing, Profile, Configuration

class WindowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Window
        fields = ['id', 'width', 'height']

class ConstructionSerializer(serializers.ModelSerializer):
    windows = WindowSerializer(many=True)

    class Meta:
        model = Construction
        fields = ['id', 'order', 'windows']

    def create(self, validated_data):
        windows_data = validated_data.pop('windows')
        construction = Construction.objects.create(**validated_data)
        for window_data in windows_data:
            Window.objects.create(construction=construction, **window_data)
        return construction

class LaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lamination
        fields = ['id', 'name']

class GlazingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Glazing
        fields = ['id', 'name']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'name']

class ConfigurationSerializer(serializers.ModelSerializer):
    lamination = LaminationSerializer(read_only=True)
    glazing = GlazingSerializer(read_only=True)
    profile = ProfileSerializer(read_only=True)
    constructions = ConstructionSerializer(many=True, read_only=True)

    class Meta:
        model = Configuration
        fields = ['id', 'order', 'name', 'lamination', 'glazing', 'profile', 'constructions']

class OrderSerializer(serializers.ModelSerializer):
    configurations = ConfigurationSerializer(many=True, read_only=True)
    constructions = ConstructionSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'order_number', 'measurer', 'created_at', 'customer_name', 'status', 'configurations', 'constructions']