from django.contrib import admin
from django.urls import include, path
from views.blogs import BlogsView, BlogView
from views.main import MainView, TabligView
from views.drug import DrugView, DrugdethView
from views.kifpool import KifPoolview
from views.jobs.list import RepotageView, RepoSearch
from views.jobs.detail import RepotageOneView
from views.sms import SmsView
from views.profile.profile import KarfarmaRepotageView, ProfileView
from views.resume.list import ResumeView
from views.resume.detail import OneResumeView
from views.messages import MessageListView
from views.profile.karfarma import KarfarmaProfileUpdateView
from views.profile.karjo import KarjoProfileUpdater

urlpatterns = [
    path("main/", MainView.as_view(), name="main"),
    path("tablig/", TabligView.as_view(), name="tablig"),
    path("blogs/", BlogsView.as_view(), name="blogs"),
    path("blogs/<int:pk>", BlogView.as_view(), name="blog page"),
    path("drug-stores/", DrugView.as_view(), name="drug-stores"),
    path("drug-stores/<int:pk>", DrugdethView.as_view(), name="drug-stores"),
    path("karfarma/profile", ProfileView.as_view()),
    path("karfarma/repotages", KarfarmaRepotageView.as_view()),
    path("kifpool", KifPoolview.as_view()),
    path("sms", SmsView.as_view()),
    path("messages", MessageListView.as_view(), name="messagess"),
    
    path("jobs", RepotageView.as_view(), name="jobs"),
    path("jobs/<int:pk>", RepotageOneView.as_view(), name="onerepotage" ),
    
    path("resumes", ResumeView.as_view(), name="resume"),
    path("resume/<int:pk>", OneResumeView.as_view(), name="oneresume"),
    
    path("profile/karfarma", KarfarmaProfileUpdateView.as_view()),
    path("profile/karjo", KarjoProfileUpdater.as_view()),
    path("repotage", RepotageView.as_view()),
    path("reposearch", RepoSearch.as_view())
]