from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.contrib.auth import get_user_model
from posts.models import Tweet  # Tweetモデルをインポート
from .models import Like

User = get_user_model()

class LikeView(View):
  def post(self, request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    user = request.user
    
    like, created = Like.objects.get_or_create(user=user, tweet=tweet)

    if created:
        # 新規にLikeされたときのみ、like_countを増やす
        like.like_count += 1
        tweet.save()

    return redirect('tweet_detail', tweet_id=tweet.id)



