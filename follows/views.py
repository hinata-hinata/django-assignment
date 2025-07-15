from django.shortcuts import render
from django.views import View
from .models import Follow
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

User = get_user_model()

# @login_required
# def follow_user(request, user_id):
#   if request.method == "POST":
#     target_user = get_object_or_404(User, id=user_id)
#     Follow.objects.get_or_create(follower=request.user, following=target_user)
#     user = request.user
#     # print('foro-kannryou!')
#   return redirect('accounts:profile', username = target_user.username)


# class Followfollower(View):
#   def get(self, request, user_id):
#     data = Follow.objects.get(user_id=user_id)
#     return render(request, 'profiles/profile.html', {'data':data})
  
# followfollower = Followfollower.as_view()

class FollowView(View):
  def post(self, request, user_id):
    if not request.user.is_authenticated:
      return redirect('accounts:login')
    
    target_user = get_object_or_404(User, id=user_id)
    
    follow_relation = Follow.objects.filter(follower=request.user, following=target_user).first()
    
    if follow_relation:
      follow_relation.delete()
    else:
      Follow.objects.get_or_create(follower=request.user, following=target_user)

    return redirect('accounts:profile', username = target_user.username)

follow_view = FollowView.as_view()

class FollowList(View):
  def get(self, request, user_id):
    target_user = get_object_or_404(User, id=user_id)
    follower = Follow.objects.filter()
    return render(request, 'follower.html', )