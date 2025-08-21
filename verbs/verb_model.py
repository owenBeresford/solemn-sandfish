import os
import sqlite3
from sqlite3 import Cursor
from stat import S_ISREG
from typing import List, Self 


def connect(fn: str) -> Cursor:
	""" A wrapper to create a DB connection
		Assuming a similar API in other DB drivers, the below model is quite 
		isolated from connection details.

		This separate function supports test data inject in test

		Current version returns a Cursor, may need a Connection in future
	"""
    s = os.stat(fn)
    if not S_ISREG(s.st_mode) or not os.access(fn, os.R_OK):
        raise Exception("Bad path for DB " + fn)

    db = sqlite3.connect(fn)
    cur = db.cursor()
    return cur


class VerbModel(object):
	""" A class to isolate the SQL logic down to business-level logic. 

		In my professional opinion match functions (as below) should not make 
		Exceptions for match fail, its not an error.

		IOIO, look at SQL error handling, I used a wrapper layer on top last time
	"""
    conn: Cursor

    def __init__(self: Self, db: Cursor) -> Self:
        self.conn = db

    def matchWeakVerb(self: Self, sample: str) -> bool:
		""" Evaluate if param word is a weak verb

			return boolean
		"""
        res = self.conn.execute(
            """SELECT weak_id, weak_word 
		from weak_verbs where weak_word = ? limit 1; """,
            (sample,),
        )
        ret = res.fetchone()
        return ret is not None

    def matchStrongVerb(self: Self, sample: str) -> bool:
		""" Evaluate if param word is a strong verb

			return boolean
		"""
        res = self.conn.execute(
            """SELECT strong_id, strong_word 
			from strong_verbs where strong_word = ? limit 1; """,
            (sample,),
        )
        ret = res.fetchone()
        return ret is not None

    def replaceVerb(self: Self, sample: str) -> List[str]:
		""" Return an array of stronger verbs compared to param word.
			This should only be called after a word is determined to be a verb.
			
			return list[str]
		"""

        res = self.conn.execute(
            """SELECT strong_word 
			from strong_verbs
			left join weak_verbs on weak_id= weak_fid
			where weak_word= ?; """,
            (sample,),
        )
        tmp: list[tuple[str]] = res.fetchall()
        out: list[str] = []
        for row in tmp:
            out.extend(row)

        return out

