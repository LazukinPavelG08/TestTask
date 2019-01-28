from rest_framework import serializers
from .models import Profile

class ProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'id',
            'vk_id',
            'first_name',
            'last_name'
        )