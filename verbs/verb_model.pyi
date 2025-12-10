from sqlite3 import Cursor

def connect(fn: str) -> Cursor:
    """A wrapper to create a DB connection
    Assuming a similar API in other DB drivers, the below model is quite
    isolated from connection details.

    This separate function supports test data inject in test

    Current version returns a Cursor, may need a Connection in future
    """

class VerbModel:
    """A class to isolate the SQL logic down to business-level logic.

    In my professional opinion match functions (as below) should not make
    Exceptions for match fail, its not an error.

    IOIO, look at SQL error handling, I used a wrapper layer on top last time
    """

    conn: Cursor
    def __init__(self, db: Cursor) -> None: ...
    def matchWeakVerb(self, sample: str) -> bool:
        """Evaluate if param word is a weak verb

        return boolean
        """

    def matchStrongVerb(self, sample: str) -> bool:
        """Evaluate if param word is a strong verb

        return boolean
        """

    def replaceVerb(self, sample: str) -> list[str]:
        """Return an array of stronger verbs compared to param word.
        This should only be called after a word is determined to be a verb.

        return list[str]
        """
