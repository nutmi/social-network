from django.contrib import admin
from django.urls import path
from rest_framework import routers
from .views import RoomViewSet

router = routers.SimpleRouter()
router.register(r"room", RoomViewSet, basename="room")
urlpatterns = router.urls
urlpatterns += []
