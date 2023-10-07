from django.contrib import admin
from .models import CustomUser, Followers, Gravity, Category, Repost


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'phone_number', 'gender', 'bio']

@admin.register(Followers)
class FollowersAdmin(admin.ModelAdmin):
    list_display = ['user']

@admin.register(Gravity)
class GravityAdmin(admin.ModelAdmin):
    list_display = ['user', 'description', 'repost_count']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Repost)
class RepostAdmin(admin.ModelAdmin):
    list_display = ['user', 'gravity']
