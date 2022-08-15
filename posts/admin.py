from django.contrib import admin

from .models import Post


# Register your models here.
# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "body")
    list_filter = [
        "body",
    ]
    fields = ("title", "body")
    search_fields = ("title",)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        print(obj.author)
        super().save_model(request, obj, form, change)
