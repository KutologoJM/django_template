from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="knox_login"),
    path("logout/", views.LogoutView.as_view(), name="knox_logout"),
    path("logout/all/", views.LogoutAllView.as_view(), name="knox_logout_all"),
]
