import sqlite3
from sqlite3 import Cursor
from typing import Final

TEST_DB: Final[str] = "/tmp/test1.dbx"


def create_test_db(fn: str) -> Cursor:
    sql = """
BEGIN;

create table verb_groups (
  group_id integer primary key AUTOINCREMENT, 
  group_word text not null
);

create table weak_verbs (
  weak_id integer primary key AUTOINCREMENT, 
  weak_word text not null,
  reference integer,
  parent_fid integer,
  group_fid integer,
  desc text,
  FOREIGN KEY(group_fid) REFERENCES verb_group(group_id)
);

create table strong_verbs (
  strong_id integer primary key AUTOINCREMENT, 
  strong_word text not null,
  weak_fid integer,
  FOREIGN KEY(weak_fid) REFERENCES weak_verbs(weak_id)
);

insert into weak_verbs( weak_word, reference, parent_fid, desc ) 
values
	("goodverb", 0, -1, "made up word here" ),
	("childverb", 0, 0, "made up word here" ),
	("refverb", 1, -1, "made up word here" ),
	("brokenverb", -1, -1, "made up word here" );

insert into strong_verbs( weak_fid, strong_word ) 
values
	(1, "goodverb" ),
	(-1, "brokenverb" ),
	(1, "goodverb2" ),
	(1, "goodverb3" );

COMMIT;
"""
    db = sqlite3.connect(fn)
    cur = db.cursor()
    sql2 = "SELECT sql FROM sqlite_master WHERE name= 'verb_groups';"
    res = cur.execute(sql2)
    if res.fetchone() is None:
        cur.executescript(sql)
        db.commit()

    # I hope this will auto flush properly, I have no user level access to sqlite3_db_cacheflush()
    return cur


# TODO: add destroyDB
