from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("create/", views.create_short_url, name="create"),
    path("register/", views.register, name="register"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
    path("edit/<str:code>/", views.edit_short_url, name="edit"),
    path("delete/<str:code>/", views.delete_short_url, name="delete"),
    path("<str:code>/", views.redirect_url, name="redirect"),
]
