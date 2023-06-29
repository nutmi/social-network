from django.shortcuts import render
from .models import GroupRoom, MessageNormalRoom, NormalRoom
from rest_framework import mixins, viewsets
from .serializers import RoomSerializer, NormalRoomSerializer, MessageNormalRoomSerializer
from django.db.models import Q

class MessageNormalRoomViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = MessageNormalRoomSerializer
    lookup_field = "id"

    def get_queryset(self):
        return  MessageNormalRoom.objects.filter(user=self.request.user)

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
        return GroupRoom.objects.filter(creator=self.request.user)
    
class NormalRoomViewSet(mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):
    lookup_field = "id"
    serializer_class = NormalRoomSerializer

    def get_queryset(self):
        return NormalRoom.objects.filter(Q(user_1=self.request.user) | Q(user_2=self.request.user))