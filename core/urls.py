from django.contrib import admin
from django.urls import path
from rest_framework import routers
from .views import FriendListViewSet
router = routers.SimpleRouter()
router.register(r"friend", FriendListViewSet, basename="friend")
urlpatterns = router.urls
urlpatterns += []