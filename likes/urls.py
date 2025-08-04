from django.urls import path

urlpatterns = [
  path('like/<int:user_id>/', like)
]
