from rest_framework import serializers
from .models import GroupRoom, MessageNormalRoom, NormalRoom, Guest
from django.db.models import Q





class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ["user", "room"]

    def create(self, validated_data):
        room_data = validated_data.get("room")
        room = GroupRoom.objects.get(id=room_data.id)
        user = validated_data.get("user")
        if room.creator == user:
            raise serializers.ValidationError("you can't add your self ")
        try:
            if Guest.objects.get(user=user, room=room_data):
                raise serializers.ValidationError("you are already in this room")
        except Guest.DoesNotExist:
            room.amout_of_users += 1
            room.save()
            return super().create(validated_data)
    



class MessageNormalRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageNormalRoom
        fields = ["user", "room", "text"]

    def create(self, validated_data):
        room_data = validated_data.get("room")
        user = validated_data.get("user")
        room = NormalRoom.objects.get(id=room_data.id)
        if room.user_2 == user or room.user_1 == user:
            return super().create(validated_data)
        else:
            raise serializers.ValidationError("this is not your room")


class GroupRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupRoom
        fields = ["creator", "id"]

class NormalRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = NormalRoom
        fields = ["user_1", "user_2", "id"]

    def create(self, validated_data):
        user_1 = validated_data.get("user_1")
        user_2 = validated_data.get("user_2")

        if user_1 == user_2:
            raise serializers.ValidationError({"non_field_errors": "You can't create a room with yourself."})
        
        existing_room = NormalRoom.objects.filter(user_1=user_1, user_2=user_2)
        if existing_room:
            raise serializers.ValidationError({"non_field_errors": "You already have a room with this person."})

        return super().create(validated_data)