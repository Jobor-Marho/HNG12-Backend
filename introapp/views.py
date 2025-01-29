"""
Views path for accessing my intro api
"""

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.conf import settings
from datetime import datetime, timezone




@api_view(['GET'])
@permission_classes([AllowAny])
def display_my_info(request):
    """
    Displays my registered email, current datetime and my github url
    """

    # Get the current UTC time
    current_time_utc = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')


    data = {
        "email": settings.EMAIL_ADDRESS,
        "current_datetime": current_time_utc,
        "github_url": settings.GITHUB_URL
        }

    return Response(data=data, status=status.HTTP_200_OK)
