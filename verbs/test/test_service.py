import os
import sys
import unittest
from typing import Self

sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.append(os.path.realpath(os.path.dirname(__file__)))

from create_db import TEST_DB, create_test_db
from service import Service
from text_tokeniser import TextTokeniser
from verb_model import VerbModel, connect


class TestService(unittest.TestCase):

    def setUp(self: Self) -> None:
        self._db = create_test_db(TEST_DB)

    def tearDown(self: Self) -> None:
        # erm?
        pass

    def test_transform(self: Self) -> None:
        obj1 = VerbModel(self._db)
        obj2 = TextTokeniser("")
        obj3 = Service(obj2, obj1)

        ret1 = obj3.transform("I am a weak verb ")  # nothing, passthrough
        self.assertTrue(isinstance(ret1[0], str))
        self.assertEqual(len(ret1), 5)

        ret1 = obj3.transform("I am a badverb ")  # crash bang!
        self.assertEqual(len(ret1), 4)
        self.assertTrue(isinstance(ret1[0], str))
        self.assertTrue(isinstance(ret1[3], str))

        ret1 = obj3.transform("I am a goodverb ")  # match weakVerb
        self.assertEqual(len(ret1), 4)
        self.assertTrue(isinstance(ret1[0], str))
        self.assertTrue(isinstance(ret1[3], list))
        self.assertTrue(isinstance(ret1[3][0], str))
        self.assertEqual(ret1[3][0], "list_follows")


if __name__ == "__main__":
    unittest.main(verbosity=2)
