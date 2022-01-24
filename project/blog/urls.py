from django.urls import path
from . import views

urlpatterns = [
    #path('accounts/login/', views.LoginView.as_view(template_name = 'accounts.login.html'),
    #name = 'login'),
    path('', views.post_list, name="post_list"),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/edit/', views.comment_edit, name='comment_edit'),
    #path('commnet/new', view.comment_new, name='comment_new'),

]