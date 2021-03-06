from django.contrib import admin
from .models import Post, Comments


#admin.site.register(Post)
#admin.site.register(Comments)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
   list_display = ('title','text','author')
   list_filter = ('created_date','published_date','author')
   search_fields =('title', 'text')


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
   list_display = ('post', 'email', 'author', 'text', 'created_date', 'active')
   list_filter = ('active', 'created_date', 'updated_date')
   search_fields = ('post','text') 
# Register your models here.
