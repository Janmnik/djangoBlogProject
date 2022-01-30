from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.urls import reverse_lazy

urlpatterns = [
    #path('accounts/login/', views.LoginView.as_view(template_name = 'accounts.login.html'),
    #name = 'login'),
    path('', views.post_list, name="post_list"),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/edit/', views.comment_edit, name='comment_edit'),
    #path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change' ),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset' ),

]