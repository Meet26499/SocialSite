from rest_framework import serializers
from ..models import Gravity, Repost, CustomUser, Category

class GravitySerializer(serializers.ModelSerializer):
    reposted_by = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), many=True, required=False)

    class Meta:
        model = Gravity
        fields = '__all__'
    
class GravityCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gravity
        exclude = ['repost_count', 'user']

    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)
    description = serializers.CharField()

    def validate_category(self, value):
        if len(value) == 0:
            raise serializers.ValidationError("Select at least 1 category for your gravity.")
        return value
    
    def validate_media(self, value):
        if not value:
            raise serializers.ValidationError("Please upload related file for it.")
        return value
    
    def validate_thumbnail(self, value):
        media_data = self.initial_data.get('media')
        if media_data and not value:
            raise serializers.ValidationError("Please upload a thumbnail for the uploaded media file.")
        return value
    
    def validate_tag_user(self, value):
        print(value, "value")
        current_user = self.context['request'].user

        if current_user in value:
            raise serializers.ValidationError("You can not tag yourself.")
        return value

class RepostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repost
        exclude = ['user', 'gravity']