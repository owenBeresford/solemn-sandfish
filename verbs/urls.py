""" Django boilerplate 
    A file holding the Django route-map
"""
from django.urls import path
from django.conf.urls import handler404, handler500

from .main import choices, export, index
from . import views

handler404 = views.error_404
handler500 = views.error_500

# URL map for Django
urlpatterns = [path("v1/explore", index),  path("v1/map-verbs", choices), path("v1/export-text", export), path("", index)]

