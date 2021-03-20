# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 17:26:38 2020

@author: DELL
"""
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
# Create table
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
t = ('RHAT',)
c.execute('SELECT * FROM stocks WHERE symbol=?', t)
print(c.fetchone())
purchases = []
for i in range(3):
    de= str(input("text: "))
    se= str(input("text: "))
    we= str(input("text: "))
    qw= int(input("integer: "))
    sw= int(input("integer: "))
    rew=(de,se,we,qw,sw)
    purchases.append(rew)
c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
for row in c.execute('SELECT * FROM stocks ORDER BY price'):
        print(row)