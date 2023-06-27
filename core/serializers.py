from rest_framework import serializers
from .models import FriendList

class FriendListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendList
        fields = ["user", "friend"]

    def create(self, validated_data):
        user = validated_data.get("user")
        friend = validated_data.get("friend")
        if user == friend:
            
            raise serializers.ValidationError("cannot add yourself to a friendlist")
        return super().create(validated_data)