from rest_framework import serializers
from ..models import Followers

class FollowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Followers
        exclude = ['user', 'followers']
