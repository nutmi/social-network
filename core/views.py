from django.shortcuts import render
from .serializers import FriendListSerializer
from rest_framework import mixins, viewsets
from .models import FriendList
# Create your views here.
class FriendListViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    serializer_class = FriendListSerializer
    lookup_field = "id"
    

    def get_queryset(self):
        return FriendList.objects.filter(user=self.request.user)
    
