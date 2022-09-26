"""
created to test simple connection to database Postgres
"""
import psycopg2

conn = psycopg2.connect("dbname=db-dev user=postgres password=rosa host=localhost")
cur = conn.cursor()
cur.execute('SELECT * FROM "Items"')

records = cur.fetchall()
print(records)