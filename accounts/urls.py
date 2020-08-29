from django.urls import path
from django.urls import path
from accounts.views import UserProfileCreate, UserProfileUpdate
from . import views


urlpatterns = [
    # path('profile', views.profile, name='profile'),
    path('profile/add/', UserProfileCreate.as_view(), name='profile-add'),
    path('profile/<int:pk>/', UserProfileUpdate.as_view(), name='profile-update'),
]
