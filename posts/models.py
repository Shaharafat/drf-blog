import uuid

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from django.shortcuts import reverse
from django.template.defaultfilters import slugify


class Post(models.Model):
  slug = models.SlugField(blank=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=250)
  body = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)

  class Meta:
      ordering = ['-created_at']
    
  # def get_api_url(self):
  #   try:
  #     return reverse('')

  def __str__(self):
    return self.title

def pre_save_post_reciever(sender, instance, *args, **kwargs):
  slug = slugify(instance.title)
  slug = f'{slug}-{instance.id}'
  #TODO: Some validation needs here
  instance.slug = slug
pre_save.connect(pre_save_post_reciever, sender=Post)
