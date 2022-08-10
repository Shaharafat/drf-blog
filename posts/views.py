from django.shortcuts import render
# from django.views.generic import APIView
from rest_framework import generics

from .models import Post
from .serializers import PostSerializer


class GetPosts(generics.ListAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  
