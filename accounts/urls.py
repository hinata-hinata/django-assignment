from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
  path('signup/', views.signup, name='signup'),
  path('<str:username>/profile/', views.profile, name='profile'),
  path('bioupdate/<str:username>/', views.bio, name='bio'),
]
