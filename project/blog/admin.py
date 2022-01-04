from django.contrib import admin
from .models import Post, Comments


admin.site.register(Post)
#admin.site.register(Comments)

@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
   list_display = ('post', 'email', 'author', 'text', 'created_date', 'active')
   list_filter = ('active', 'created_date', 'updated_date')
   search_fields = ('post','text') 
# Register your models here.
