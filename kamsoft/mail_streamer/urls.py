from django.urls import path
from . import views

urlpatterns = [path("", views.mails_data)]