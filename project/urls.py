from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app import views as app_views
from food import views as food_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app_views.index),
    path('add-chef', app_views.addChef),
    path('edit-chef/<int:pk>', app_views.editChef),
    path('delete/<int:pk>', app_views.deleteChef),
    path('add-food', food_views.addFood),
    path('', include('app.urls')),
    path('', include('food.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
