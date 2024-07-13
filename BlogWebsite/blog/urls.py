


from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.main, name='main'),
    path('blog/', views.blogs, name='blogs'),
    path('users/', views.users, name='users'),
    path('blogs/', views.blogs, name='blogs'),
    path('comments/', views.comments, name='comments'),
    path('categories/', views.categories, name='categories'),
    path('blog/<int:pk>/', views.blogdetails, name='blogdetails'),
]

