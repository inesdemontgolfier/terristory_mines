#!/usr/bin/python3
# http://initd.org/psycopg/docs/usage.html
import psycopg2
HOST = "localhost"
USER = "postgres"
PASSWORD = "postgres"
DATABASE = "postgres"
# Open connection
conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
# Open a cursor to send SQL commands
cur = conn.cursor()
# Execute a SQL SELECT command
sql = "SELECT COUNT(*) FROM consultations.analyses_territoriales AND date::text LIKE {date}".format(date="'2021%'")
cur.execute(sql)
# Fetch data line by line
raw = cur.fetchone()
print(raw[0])
##print(raw+2)
##conn.close()
