from _typeshed import Incomplete
from django.http import HttpRequest, HttpResponse
from django.urls import path as path
from service import Service as Service
from typing import Final

csfp: Incomplete
DB_NAME: Final[str]

def choices(reqt: HttpRequest) -> HttpResponse:
    """
    A loose function to apply the Service object

    IMPURE across Django stack,
    """

def export(reqt: HttpRequest) -> HttpResponse: ...
def index(reqt: HttpRequest) -> HttpResponse:
    """Inital page impressiion, with not data set.
    IMPURE across Django stack
    """
