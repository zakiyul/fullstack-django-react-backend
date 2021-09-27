from rest_framework import routers, urlpatterns
from .api import FoodViewset

router = routers.DefaultRouter()
router.register('api/food', FoodViewset)

urlpatterns = router.urls