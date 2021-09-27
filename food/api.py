from rest_framework import viewsets
from .models import FoodModel
from .serializers import FoodSerializerGet, FoodSerializerPost

class FoodViewset(viewsets.ModelViewSet):
  queryset = FoodModel.objects.all()
  serializer_class = FoodSerializerPost

  def get_serializer_class(self):
      if self.request.method == 'GET':
        return FoodSerializerGet
      else:
        return self.serializer_class