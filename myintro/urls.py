"""
Project Settings
"""

from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path("api/intro/", include("introapp.urls"))
]

urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT,
    )

