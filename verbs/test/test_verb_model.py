import os

# Note this is a singleton object
import sys
import unittest
from typing import List, Self

sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.append(os.path.realpath(os.path.dirname(__file__)))

from create_db import TEST_DB, create_test_db
from verb_model import VerbModel, connect


class testVerbModel(unittest.TestCase):
    def setUp(self: Self) -> None:
        self._db = create_test_db(TEST_DB)

    def tearDown(self: Self) -> None:
        # erm?
        pass

    def test_connect(self: Self) -> None:
        self.assertTrue(isinstance(connect(TEST_DB), object))
        self.assertRaises(
            Exception,
            connect,
            "/tmp/",
        )

    def test_matchWeakVerb(self: Self) -> None:
        obj = VerbModel(self._db)
        self.assertTrue(obj.matchWeakVerb("goodverb"))
        self.assertFalse(obj.matchWeakVerb("badverb"))
        self.assertFalse(obj.matchWeakVerb(""))
        self.assertFalse(obj.matchWeakVerb(None))

    def test_matchStrongVerb(self: Self) -> None:
        obj = VerbModel(self._db)
        self.assertTrue(obj.matchStrongVerb("goodverb"))
        self.assertFalse(obj.matchStrongVerb("badverb"))
        self.assertFalse(obj.matchStrongVerb(""))
        self.assertFalse(obj.matchStrongVerb(None))

    def test_replaceVerb(self: Self) -> None:
        obj = VerbModel(self._db)
        val1 = obj.replaceVerb("goodverb")
        self.assertTrue(isinstance(val1, List))
        self.assertTrue(len(val1) == 3)

        val2 = obj.replaceVerb("badverb")
        self.assertTrue(isinstance(val2, List))
        self.assertTrue(len(val2) == 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
