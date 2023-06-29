from django.shortcuts import render
from .models import GroupRoom, MessageNormalRoom, NormalRoom, Guest
from rest_framework import mixins, viewsets
from .serializers import GroupRoomSerializer, NormalRoomSerializer, MessageNormalRoomSerializer, GuestSerializer
from django.db.models import Q

class GuestViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = GuestSerializer
    lookup_field = "id"
    queryset = Guest.objects.all()



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
    serializer_class = GroupRoomSerializer

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