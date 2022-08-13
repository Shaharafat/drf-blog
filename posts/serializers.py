from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
  # url = serializers.SerializerMethodField()
  url = serializers.HyperlinkedIdentityField(
    view_name='posts:post_detail',
    lookup_field='slug'
  )
  class Meta:
    model = Post
    fields = ['id','slug','url', 'title', 'body', 'created_at', 'updated_at']

  def get_url(self,obj):
    return obj.get_api_url()


class PostDetailSerializer(serializers.ModelSerializer):
  # url = serializers.HyperlinkedIdentityField(
  #   view_name='posts:post_detail',
  #   lookup_field='slug'
  # )
  class Meta:
    model = Post
    fields = [ 'title', 'body','created_at', 'updated_at']

  # def get_url(self,obj):
  #   return obj.get_api_url()
