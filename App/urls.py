from Blog.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home , name = 'home'),
    path('comment', views.comment, name = 'comment'),
    path('profile', views.profile, name = 'profile'),
    path('recent-posts', views.recentposts, name = 'recentposts'),
    path('update-like/', views.update_like, name = 'update-like'),
    path('update-bookmark/', views.update_bookmark, name = 'update-bookmark'),
    path('register', views.register, name = 'register'),
    path('loginsession/<slug:slug>/<slug:name>', views.loginsession, name = 'loginsession'),
    path('login', views.login_view, name = 'login'),
    path('logout', views.logout_view, name = 'logout'),
    path('category/<str:cat>', views.category, name = 'category'),
    path('categories', views.categories, name = 'categories'),
    path('categories/<str:name>', views.category_detail, name = 'category_detail'),
    path('<slug:name>/<slug:slug>', views.postpage, name = 'postpage')
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)