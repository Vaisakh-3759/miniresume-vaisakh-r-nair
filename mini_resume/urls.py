from django.urls import path
from .views import heakth_check, ResumeApi

urlpatterns = [
    path('health/', heakth_check.as_view(), name='health'),
    path('resumes/', ResumeApi.as_view(), name='resumes'),
]
