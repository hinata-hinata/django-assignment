from django.urls import path
from . import views

urlpatterns = [
  path('follow/<int:user_id>/', views.follow_view, name='follow'),
  path('followlist/<int:user_id>/', views.followlist, name='followlist'),
  path('followerlist/<int:user_id>/', views.followerlist, name='followerlist'),
  
]
                                                                   