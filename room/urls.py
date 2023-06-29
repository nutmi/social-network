from django.contrib import admin
from django.urls import path
from rest_framework import routers
from .views import RoomViewSet, NormalRoomViewSet, MessageNormalRoomViewSet

router = routers.SimpleRouter()
router.register(r"normalroom", NormalRoomViewSet, basename="normalroom")
router.register(r"grouproom", RoomViewSet, basename="grouproom")
router.register(r"messagenormalroom", MessageNormalRoomViewSet, basename="messagenormalroom")
urlpatterns = router.urls
urlpatterns += []
