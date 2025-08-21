""" Django boilerplate.
    A Django requiremnent that stores the local settings for Django.
    The important phrase is setting up templates """
import os

ROOT_URLCONF = "verbs.urls"
DEBUG = False
ALLOWED_HOSTS=["*"]

SECRET_KEY = "unset-value"  # override this value
# Add HTTPS
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(os.path.dirname(__file__), "templates")],
    }
]
