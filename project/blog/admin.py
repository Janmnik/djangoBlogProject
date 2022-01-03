from django.contrib import admin
from .models import Post, Comments


admin.site.register(Post)

#@admin.register(Comments)
 #   list_display = ('name', 'email', 'post', 'created', 'active')
  #  list_filter = ('active', 'created', 'updated')
   # search_fields = 
# Register your models here.
