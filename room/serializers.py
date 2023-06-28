from rest_framework import serializers
from .models import GroupRoom, Message, NormalRoom, Guest


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupRoom
        fields = ["creator", "id"]

class NormalRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = NormalRoom
        fields = ["user_1", "user_2"]

    def create(self, validated_data):
        user_1 = validated_data.get("user_1")
        user_2 = validated_data.get("user_2")

        if user_1 == user_2:
            raise serializers.ValidationError("you can't create room with your self")
        existing_room = NormalRoom.objects.filter(user_1=user_1, user_2=user_2)
        if existing_room:
            raise serializers.ValidationError("you already have room with this person")
        return super().create(validated_data)