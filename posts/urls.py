from django.urls import path

from .views import GetPosts

urlpatterns = [
  path('', GetPosts.as_view(), name='all_posts')
]
