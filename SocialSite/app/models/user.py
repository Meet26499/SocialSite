from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models

PROFILE_TYPE_CHOICES = (
    ('public', 'Public'),
    ('private', 'Private'),
)

GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    full_name = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True, validators=[MinLengthValidator(10)] )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    birth_date = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True)
    interests = models.ManyToManyField('Category', related_name='users', blank=True)
    profile_type = models.CharField(max_length=10, choices=PROFILE_TYPE_CHOICES)
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

    def __str__(self):
        return self.username
    
class Followers(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    followers = models.ManyToManyField(CustomUser, related_name='user_followers')

    def __str__(self):
        return self.user.username
