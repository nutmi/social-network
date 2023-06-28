from django.contrib import admin
from django.urls import path
from rest_framework import routers
from .views import RoomViewSet, NormalRoomViewSet

router = routers.SimpleRouter()
router.register(r"normalroom", NormalRoomViewSet, basename="normalroom")
urlpatterns = router.urls
urlpatterns += []
