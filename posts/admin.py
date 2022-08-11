from django.contrib import admin

from .models import Post


# Register your models here.
# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'body')
  list_filter= ['body',]
  fields = ('title', 'author','body')
  search_fields = ('title',)
