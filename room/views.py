from django.shortcuts import render
from .models import Room, Message
from rest_framework import mixins, viewsets
from .serializers import RoomSerializer
from django.db.models import Q


# Create your views here.
class RoomViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    lookup_field = "id"
    serializer_class = RoomSerializer

    def get_queryset(self):
        return Room.objects.filter(creator=self.request.user)
