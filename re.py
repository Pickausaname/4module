import re
import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER, mount TEXT)''')
def poisk(filename):
    openfile=open(filename)
    spisok=[]
    for line in openfile:
        line=line.lstrip()
        result=re.findall('^From: ([\w@.]+)',line)
        if len(result)>0:
            spisok.append(result)
    return spisok

def unicemail(filename):
    sp=[]
    for i in poisk(filename):
        if i not in sp:
            sp.append(i)
    return sp
