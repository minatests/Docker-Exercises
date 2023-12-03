from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.my_authors, name="authors" ),
    path('author/<int:id>/', views.oneauthor, name = "oneauthor"),
]

