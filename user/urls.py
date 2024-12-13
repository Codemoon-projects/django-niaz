from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenRefreshView
from user.views import SendSMSPhoneView, LoginView
from user.profileView import ChangeData
from views.karjo import KarjoView

urlpatterns = [
    path("login", LoginView.as_view(), name="login"),
    path("send-sms", SendSMSPhoneView.as_view(), name="sms"),
    path("refresh", TokenRefreshView.as_view(), name="refresh"),
    path("karfarma", ChangeData.as_view(), name="change-data-karfarma"),
    path("karjo", KarjoView.as_view(), name="change-data-karjo")
]

