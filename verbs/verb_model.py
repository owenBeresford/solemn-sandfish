import sqlite3 
from sqlite3 import Cursor
from stat import S_ISREG
import os
from typing import Any, Final, Self, List #, Optional

def connect(fn:str)-> Cursor:
	s=os.stat(fn)
	if not S_ISREG(s.st_mode) or not os.access(fn, os.R_OK):
		raise Exception("Bad path for DB "+fn)

	db = sqlite3.connect( fn )
	cur=db.cursor()
	return cur

# In my professional opinion match functions (as below) should not make Exceptions for match fail.
# IOIO, XXX look at SQL error handling, I used a wrapper layer on top last time
class VerbModel(object):
	conn: Cursor

	def __init__(self:Self, db:Cursor)->Self:
		self.conn=db


	def matchWeakVerb(self:Self, sample:str)->bool:
		res=self.conn.execute(
	"""SELECT weak_id, weak_word 
		from weak_verbs where weak_word = ? limit 1; """,
	 (sample,)
							)
		ret=res.fetchone()
		return ret!=None

	def matchStrongVerb(self:Self, sample:str)->bool:
		res=self.conn.execute(
	"""SELECT strong_id, strong_word 
			from strong_verbs where strong_word = ? limit 1; """,
	 (sample,)
							)
		ret=res.fetchone()
		return ret!=None

	def replaceVerb(self:Self, sample:str)->List[str]:
		res=self.conn.execute(
	"""SELECT strong_word 
			from strong_verbs
			left join weak_verbs on weak_id= weak_fid
			where weak_word= ?; """,
			 (sample,)
							)
		tmp:list[tuple[str]] =res.fetchall()
		out:list[str]=[]
		for row in tmp: 
			out.extend(row)
		
		return out

