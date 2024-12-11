from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path('home/', views.home, name="home"),
    path('detail/<int:id>/', views.detail, name="detail"),
    path('add_movie/', views.add_movie, name="add_movie"),
    path('edit_movies/<int:id>/', views.edit_movies, name="edit_movies"),
    path('delete_movie/<int:id>/', views.delete_movie, name="delete_movie"),
    path('add_review/<int:id>/', views.add_review, name="add_review"),
    path('edit_review/<int:movie_id>/<int:review_id>/', views.edit_review, name="edit_review"),
    path('delete_review/<int:movie_id>/<int:review_id>/', views.delete_review, name="delete_review"),
]
