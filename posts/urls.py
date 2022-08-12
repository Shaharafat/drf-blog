from django.urls import path

from .views import GetPosts, PostDetails

app_name='post'
urlpatterns = [
  path('', GetPosts.as_view(), name='all_posts'),
  path('<str:slug>/', PostDetails.as_view(), name='post_detail')
]
