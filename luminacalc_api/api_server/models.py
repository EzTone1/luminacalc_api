# models.py
from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    order_number = models.CharField(max_length=20, unique=True)
    measurer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    customer_name = models.CharField(max_length=100)
    STATUS_CHOICES = (
        ('measuring', 'Замер не произведен'),
        ('config_entering', 'Конфигурации не настроены'),
        ('wait_cost', 'Ожидание просчета'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='measuring')

class Window(models.Model):
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField()

class Construction(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='structures')
    windows = models.ManyToManyField(Window, related_name='structures')

class Lamination(models.Model):
    name = models.CharField(max_length=100)

class Glazing(models.Model):
    name = models.CharField(max_length=100)

class Profile(models.Model):
    name = models.CharField(max_length=100)

class Configuration(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='configurations')
    name = models.CharField(max_length=100)
    lamination = models.ForeignKey(Lamination, on_delete=models.SET_NULL, null=True, blank=True)
    glazing = models.ForeignKey(Glazing, on_delete=models.SET_NULL, null=True, blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    constructions = models.ManyToManyField(Construction, related_name='configurations')