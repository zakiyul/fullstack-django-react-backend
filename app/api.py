from rest_framework import serializers, viewsets
from .models import Chef
from .serializers import ChefSerializer

class ChefViewset(viewsets.ModelViewSet):
  queryset = Chef.objects.all()
  serializer_class = ChefSerializer