"""This pico service's Controller class.
Please see Django notes for more information.
This will autolaod Django and start a HTTP service when run from the command line"""

import os
import sys
from typing import Final

import django
from django.core.management import execute_from_command_line
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import path

csfp = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if csfp not in sys.path:
    sys.path.insert(0, csfp)

from factory import create_verb_service
from service import Service

__package__ = "verbs"

DB_NAME: Final[str] = os.path.join(os.path.dirname(__file__), "asset", "verbs.sqlite3.db")


def choices(reqt: HttpRequest) -> HttpResponse:
    """
    A loose function to apply the Service object

    IMPURE across Django stack,
    """

    if reqt.method == "GET":
        return render(reqt, "index.html", {"smpl": "", "choice": None, "generated": None, "firsttab": "explore"})
    elif reqt.method == "POST":
        src: str = reqt.POST.get("smpl", "")
        svr: Service = create_verb_service(DB_NAME)
        resp: list[str | list[str]] = svr.transform(src)
        return render(reqt, "index.html", {"smpl": src, "choice": resp, "generated": None, "firsttab": "choice"})
    else:
        fixie: str = (
            "You requested an unsupported HTTP verb: "
            + reqt.method
            + "\nPlease use GET to access the form, and POST to retun it"
        )
        tmp: HttpResponse = render(
            reqt, "index.html", {"smpl": fixie, "choice": None, "generated": None, "firsttab": "explore"}, status=406
        )
        return tmp


def export(reqt: HttpRequest) -> HttpResponse:
    #    smpl: str= reqt.POST.get("smpl", "")
    #     rslt:str = reqt.POST.get("" )
    print("TODO: add code here " + reqt.method, reqt.POST)
    # TODO Add extra function for export-text
    tmp: HttpResponse = render(reqt, "error.html", status=501)
    return tmp


def index(reqt: HttpRequest) -> HttpResponse:
    """Inital page impressiion, with not data set.
    IMPURE across Django stack
    """
    tmp: HttpResponse = render(
        reqt, "index.html", {"smpl": "", "choice": None, "generated": None, "firsttab": "explore"}
    )
    if reqt.method != "GET":
        tmp.status_code = 409
    return tmp


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    django.setup()
    execute_from_command_line()
