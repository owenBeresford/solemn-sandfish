from django.http import HttpRequest, HttpResponse
from django.urls.exceptions import Resolver404

def error_404(reqt: HttpRequest, exception: Resolver404) -> HttpResponse:
    """Emit a more user friendly error message
    IMPURE across Django stack

            I would like to know where doesn't seem be be an official means to
                        access the path in that exception.
    """

def error_500(reqt: HttpRequest) -> HttpResponse:
    """Emit a more user friendly error message
    IMPURE across Django stack
    """
