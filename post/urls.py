from django.urls import path

from post import views


urlpatterns = [

    path('', views.home, name="home"),
    path('<int:pk>', views.details, name="detail"),
    path('add', views.addPost, name="add"),
    path('update/<int:pk>', views.updatePost, name="update"),
    path('delete/<int:pk>', views.deletePost, name="delete"),

]
