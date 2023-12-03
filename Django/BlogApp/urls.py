from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_home, name="home" ),
    path('posts/', views.my_posts, name="posts" ),
    # path('authors/', views.my_authors, name="authors" ),
    path('categories/', views.my_categories, name="categories" ),
    path('post/<int:id>/', views.onepost, name = "onepost"),
    # path('author/<int:id>/', views.oneauthor, name = "oneauthor"),
    path('category/<int:id>/', views.onecategory, name = "onecategory"),
    path('comments', views.my_comments, name = "comments"),

    

]