import os
import re
import sys
import unittest
from typing import Final, List, Self, Type

import django
from django.http import HttpRequest, HttpResponse

# I am aware that the more recent Django docs favour making a client object,
# but I think I need to inject settings to the requests i.e. POST
from django.test.client import RequestFactory

sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.append(os.path.realpath(os.path.dirname(__file__)))

from main import choices, export, index


class TestMain(unittest.TestCase):

    def setUp(self: Self) -> None:
        self.fact = RequestFactory()

    def tearDown(self: Self) -> None:
        pass

    def test_index(self: Self) -> None:
        reqt: HttpRequest = self.fact.get("/")
        resp: HttpResponse = index(reqt)
        self.assertEqual(resp.status_code, 200)

        reqt = self.fact.get("/v1/explore")
        resp = index(reqt)
        self.assertEqual(resp.status_code, 200)

        reqt = self.fact.put("/")
        resp = index(reqt)
        self.assertEqual(resp.status_code, 409)

        # This should work, but the client isn't executing the whole stack.
        # I will need to pickup this point in the external URL test
        # reqt2 = self.fact.get('/v3.141/explore/')
        # resp2 =index(reqt2)
        # print("invalid URL:", resp2, resp2.status_code, resp2.text  )
        # self.assertNotEqual(resp2.status_code, 200)

    def test_choices(self: Self) -> None:
        reqt: HttpRequest = self.fact.post(
            "/v1/map-verbs",
            data={"smpl": "sdf sfsd sfs carry dgdfg dfg dgf"},
        )
        resp: HttpResponse = choices(reqt)
        self.assertEqual(resp.status_code, 200)
        ret = re.search('select name="word3"', resp.text)
        print("SDFSDF", ret)
        self.assertNotEqual(ret, None)

        reqt = self.fact.post(
            "/v1/map-verbs",
            data={"smpl": "sdf sfsd sfs dgdfg dfg dgf"},
        )
        resp = choices(reqt)
        self.assertEqual(resp.status_code, 200)
        ret = re.search('select name="word[0-9]"', resp.text)
        self.assertEqual(ret, None)

        reqt = self.fact.post(
            "/v1/map-verbs",
            data={"smpl": ""},
        )
        resp = choices(reqt)
        self.assertEqual(resp.status_code, 200)
        ret = re.search('select name="word[0-9]"', resp.text)
        self.assertEqual(ret, None)

    def test_export(self: Self) -> None:
        pass  # code doesn't exist


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "verbs.settings")
    django.setup()
    unittest.main(verbosity=2)
