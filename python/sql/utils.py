import sqlite3
from contextlib import contextmanager

@contextmanager
def connect_to_db(database):
    path = ''
    conn = sqlite3.connect(path+database)
    cur = conn.cursor()
    yield cur
    conn.commit()
    conn.close()