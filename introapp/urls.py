"""
Mapped Url for accessing intro info
"""

from django.urls import path, include
from introapp import views

app_name = "intro"

urlpatterns = [
    path("", views.display_my_info, name="display-info")
]