from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from picassoapp import views

urlpatterns = [
    path('', views.homepage, name="home"),
    path('user/<username>/', views.user_feed, name="user_feed"),
    path('delete-post/<post_id>/', views.delete_post),
    path('like-post/<post_id>/', views.like_post),
    path('all-posts/', views.view_all_posts, name="all_posts"),
    path('users/', views.all_users, name="all_users"),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
