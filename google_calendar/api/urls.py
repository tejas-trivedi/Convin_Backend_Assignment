from .views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('calendar/init/', RedirectOauthView),
    path('google_oauth/callback/', CallbackView)
]