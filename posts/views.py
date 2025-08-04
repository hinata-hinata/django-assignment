from django.shortcuts import redirect, render

from likes.models import Like
from .models import Tweet
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied

User = get_user_model()

class IndexView(View):
  def get(self, request):
    data_list = Tweet.objects.all().order_by('-created_at')
    
    for tweet in data_list:
      tweet.like_count = Like.objects.filter(tweet=tweet).count()

  
    return render(request, 'posts/index.html', {'data_list':data_list})
  
  def post(self, request):
    tweet_id = request.POST.get('tweet_id')
    tweet = get_object_or_404(Tweet, id=tweet_id)
    user = request.user
    
    like, created = Like.objects.get_or_create(user=user, tweet=tweet)

    if created:
      like.like_count += 1
      like.save()

    return redirect('posts:index')


index = IndexView.as_view()


class CreateView(LoginRequiredMixin, generic.edit.CreateView):
  model = Tweet
  fields = ['content']
  template_name = 'posts/create.html'
  success_url = '/'

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
  
create = CreateView.as_view()


class UpdateView(LoginRequiredMixin, generic.edit.UpdateView):
  model = Tweet
  fields = ['content']
  template_name = 'posts/update.html'
  success_url = '/'
  
  def dispatch(self, request, *args, **kwargs):
    obj = self.get_object()
    if obj.author != self.request.user:
      raise PermissionDenied('編集権限がありません')
    return super().dispatch(request, *args, **kwargs)
  
update = UpdateView.as_view()


class DeleteView(LoginRequiredMixin, generic.edit.DeleteView):
  model = Tweet
  template_name = 'posts/delete.html'
  success_url = '/'
  
  def dispatch(self, request, *args, **kwargs):
      obj = self.get_object()
      if obj.author != self.request.user:
          raise PermissionDenied('削除権限がありません。')
      return super().dispatch(request, *args, **kwargs)
    
delete = DeleteView.as_view()