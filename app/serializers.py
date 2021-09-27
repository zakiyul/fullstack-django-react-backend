from rest_framework import fields, serializers
from .models import Chef

class ChefSerializer(serializers.ModelSerializer):
  class Meta:
    model = Chef
    fields = '__all__'