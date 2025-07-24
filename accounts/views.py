from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import get_user_model
from django.views import View, generic
from .bioForms import BioForm
from follows.models import Follow
from posts.models import Tweet
# from django.contrib.auth.forms import UserCreationForm # ユーザー登録用のフォームクラス
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy


User = get_user_model() 

def profile(request, username):
    user = get_object_or_404(User, username=username)
    data_list = Tweet.objects.filter(author=user).order_by('-created_at')
    post_count = data_list.count()

    followers = Follow.objects.filter(following=user)
    followings = Follow.objects.filter(follower=user)
    
    is_following = False
    if request.user.is_authenticated:
      is_following = Follow.objects.filter(follower=request.user, following=user).exists()

    return render(request, 'profiles/profile.html', {'profile_user': user, 'data_list':data_list, 'post_count':post_count, 'followers':followers, 'followings':followings, 'is_following':is_following})


class SignUpView(generic.CreateView):
  form_class = CustomUserCreationForm
  success_url = reverse_lazy('login')
  template_name = 'accounts/signup.html'
  
signup = SignUpView.as_view()


class BioUpdate(View):
  def get(self, request, username):
    target_user = get_object_or_404(User, username=username)
    bio = target_user.bio
    bio_form = BioForm(instance=target_user) 
    return render(request, 'profiles/bio.html', {'bio':bio, 'bio_form':bio_form})
  
  def post(self, request, username):
      target_user = get_object_or_404(User, username=username)
      bio_form = BioForm(request.POST, instance=target_user)
      if bio_form.is_valid():
        bio_form.save()
        return redirect('accounts:profile', username=target_user.username)
bio = BioUpdate.as_view()
    