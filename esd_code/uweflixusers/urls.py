from uweflixusers import views 
from django.urls import path

urlpatterns = [
    path("login-user/", views.login_user, name="login-user"),
    path("logout-user/", views.logout_user, name="logout-user"),
    path("create-user/", views.create_user, name="create-user"),
]