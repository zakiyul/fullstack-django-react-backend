from django.db import models
from django.db.models import fields
from rest_framework import serializers, request
from .models import FoodModel
from app.serializers import ChefSerializer

class FoodSerializerGet(serializers.ModelSerializer):
  chef = ChefSerializer(read_only=True)

  class Meta:
    model = FoodModel
    fields = ['id','nama','harga','chef','gambar']

class FoodSerializerPost(serializers.ModelSerializer):
  class Meta:
    model = FoodModel
    fields = '__all__'