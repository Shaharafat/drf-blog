from django.shortcuts import render
# from django.views.generic import APIView
from rest_framework import generics, permissions

from .models import Post
from .serializers import PostDetailSerializer, PostSerializer


class GetPosts(generics.ListAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  
class PostDetails(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = PostDetailSerializer
  lookup_field='slug'
  queryset = Post.objects.all()
  permission_classes = [permissions.IsAuthenticated]
