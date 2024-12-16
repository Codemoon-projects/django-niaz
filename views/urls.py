from django.contrib import admin
from django.urls import include, path
from views.blogs import BlogsView, BlogView
from views.main import MainView
from views.drug import DrugView
from views.kifpool import KifPoolview
from views.repotage import RepotageView
from views.sms import SmsView
from views.resume import ResumeView
from views.profile.profile import KarfarmaRepotageView, ProfileView
from views.onerepotage import RepotageOneView
from views.oneresume import OneResumeView
from views.messages import MessageListView
from views.profile.karfarma import KarfarmaProfileUpdateView
from views.profile.karjo import KarjoProfileUpdater

urlpatterns = [
    path("main/", MainView.as_view(), name="main"),
    path("blogs/", BlogsView.as_view(), name="blogs"),
    path("resume/<int:pk>", OneResumeView.as_view(), name="oneresume"),
    path("blogs/<int:pk>", BlogView.as_view(), name="blog page"),
    path("drug-stores/", DrugView.as_view(), name="drug-stores"),
    path("repotage/<int:pk>", RepotageOneView.as_view(), name="onerepotage" ),
    path("karfarma/profile", ProfileView.as_view()),
    path("karfarma/repotages", KarfarmaRepotageView.as_view()),
    path("kifpool", KifPoolview.as_view()),
    path("sms", SmsView.as_view()),
    path("repotage", RepotageView.as_view(), name="repotages"),
    path("messages", MessageListView.as_view(), name="messagess"),
    path("resumes", ResumeView.as_view(), name="resume"),
    
    path("profile/karfarma", KarfarmaProfileUpdateView.as_view()),
    path("profile/karjo", KarjoProfileUpdater.as_view()),
]