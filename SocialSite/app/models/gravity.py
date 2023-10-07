from django.db import models
from ..models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Gravity(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.TextField()
    tag_user = models.ManyToManyField(CustomUser, related_name='tagged_users', blank=True, null=True)
    allow_comment = models.BooleanField(default=True)
    category = models.ManyToManyField(Category, related_name="categories", blank=True)
    media = models.FileField(upload_to='gravity_media/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='gravity_thumbnails/', blank=True, null=True)
    repost_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s post"
    
class Repost(models.Model):
    gravity = models.ForeignKey(Gravity, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    reposted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} reposted {self.gravity}"