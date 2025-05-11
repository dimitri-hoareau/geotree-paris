from django.urls import path, include
from rest_framework import routers
from .views import TreeViewSet

router = routers.DefaultRouter()
router.register(r'trees', TreeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]