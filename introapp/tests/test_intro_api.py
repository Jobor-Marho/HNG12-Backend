"""
Test if intro API works
"""

from django.test import SimpleTestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from dateutil import parser
from dateutil.tz import tzutc
from datetime import timezone

class IntroAPI(SimpleTestCase):
    """Test the intro API"""

    def test_intro(self):
        """Test intro check"""
        client = APIClient()
        url = reverse("intro:display-info")
        res = client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn("email", res.data)
        self.assertIn("current_datetime", res.data)
        self.assertIn("github_url", res.data)

        # Check that the email is not empty and is a valid email
        email = res.data["email"]
        self.assertIsInstance(email, str)  # Check that email is a string
        self.assertTrue(bool(email), "Email should not be empty.")
        self.assertRegex(email, r"[^@]+@[^@]+\.[^@]+", "Invalid email format.")

        # Check that current_datetime is a valid ISO 8601 formatted datetime
        current_datetime = res.data["current_datetime"]
        self.assertIsInstance(current_datetime, str)  # Ensure it's a string

        # Define the expected format
        iso_8601_format = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$'

        # Check if it matches the expected ISO 8601 format with 'Z' at the end
        self.assertRegex(current_datetime, iso_8601_format, f"Invalid datetime format: {current_datetime}")

        try:
            # Replace 'Z' with '+00:00' to handle UTC timezone correctly for parsing
            current_datetime = current_datetime.replace('Z', '+00:00')

            # Parse the datetime string
            parsed_datetime = parser.isoparse(current_datetime)

            # Check if tzinfo is tzutc(), which is equivalent to UTC
            self.assertIsInstance(parsed_datetime.tzinfo, tzutc, "Datetime is not in UTC.")

            # Alternatively, check if the UTC offset is 0 (indicating UTC)
            self.assertEqual(parsed_datetime.utcoffset(), timezone.utc.utcoffset(parsed_datetime), "Datetime is not in UTC.")

        except ValueError:
            self.fail(f"Invalid datetime format: {current_datetime}")

        # Check that github_url is a valid URL
        github_url = res.data["github_url"]
        self.assertIsInstance(github_url, str)  # Ensure it's a string
        self.assertTrue(bool(github_url), "GitHub URL should not be empty.")
        self.assertRegex(github_url, r"^(https?://)?(www\.)?github\.com/[A-Za-z0-9_-]+(/[A-Za-z0-9_-]+)*$", "Invalid GitHub URL format.")