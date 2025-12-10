from sqlite3 import Cursor
from typing import Final

TEST_DB: Final[str]

def create_test_db(fn: str) -> Cursor: ...
