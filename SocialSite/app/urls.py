from django.urls import path
from .views import (RegistrationView, LoginView, GravityListView, 
                    GravityCreateView, RepostCreateView, FollowUserView,
                    UnfollowUserView, CustomUserEditView)

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('edit-user/', CustomUserEditView.as_view(), name='edit-user'),
    path('login/', LoginView.as_view(), name='login'),
    path('gravity/post/', GravityCreateView.as_view(), name='gravity-create'),
    path('gravity/list/', GravityListView.as_view(), name='gravity-list'),
    path('gravity/repost/<int:gravity_id>/', RepostCreateView.as_view(), name='repost-gravity'),
    path('follow/<int:follower_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:follower_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
]
