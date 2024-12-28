from django.contrib import admin
from django.urls import include, path
from views.blogs import BlogsView
from views.main import MainView
from views.main import BlogdownView



urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("api/", include("views.urls"), name="api"),
    path("auth/", include("user.urls"), name="auth"),
    path("remove", BlogdownView.as)
]