from datetime import date
from rest_framework import serializers, validators
from ..models import CustomUser, Category
from ..models.user import GENDER_CHOICES

class UserEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'full_name',
            'gender',
            'birth_date',
            'bio',
            'interests',
            'profile_type',
            'photo',
        ]
    
    username = serializers.CharField(validators=[validators.UniqueValidator(queryset=CustomUser.objects.all(), message='This username is already in use. Please choose a different one.')])
    gender = serializers.ChoiceField(choices=GENDER_CHOICES)
    interests = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)

    def validate_birth_date(self, value):
        if not value:
            raise serializers.ValidationError("Birth Date is required.")

        today = date.today()
        if value >= today:
            raise serializers.ValidationError("Birth Date cannot be in the future or today's date.")
        
        return value
    
    def validate_interests(self, value):
        print(value, "value")
        if len(value) < 3:
            raise serializers.ValidationError("Select at least 3 interests.")
        return value