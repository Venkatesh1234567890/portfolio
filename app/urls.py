from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name="home"),
    path('posts/', views.posts, name="posts"),
    path('post/<slug:slug>/', views.post, name="post"),
    path('profile/', views.profile, name="profile"),

    #CRUD PATHS

    path('create_post/',views.createpost, name="create_post"),
    path('update_post/<slug:slug>/',views.updatepost, name="update_post"),
    path('delete_post/<slug:slug>/',views.deletepost, name="delete_post"),


    path('send_email/',views.sendEmail, name="send_email"),
]
