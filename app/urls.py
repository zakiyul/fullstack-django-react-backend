from django.urls import path
from rest_framework import routers, urlpatterns
from .api import ChefViewset

router = routers.DefaultRouter()
router.register('api/chef', ChefViewset)

urlpatterns = router.urls