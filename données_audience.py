#!/usr/bin/python3
# http://initd.org/psycopg/docs/usage.html
from this import d
from typing_extensions import dataclass_transform
import psycopg2
import datetime
from matplotlib import pyplot as plt
HOST = "localhost"
USER = "postgres"
PASSWORD = "postgres"
DATABASE = "postgres"
# Open connection
conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
# Open a cursor to send SQL commands
cur = conn.cursor()
def monthly_connections(date):
    sql = "SELECT COUNT(*) FROM consultations.analyses_territoriales WHERE date::text LIKE {}".format(date)
    cur.execute(sql)
# Fetch data line by line
    raw = cur.fetchone()
    return raw[0]

months=[]

#select only the month and the year
today=str(datetime.date.today())[0:-3]

#we chose to visiualize datas for 1 year
year=int(today[0:4])-1
month=int(today[-2:])

def date_to_string(year,month):
    date = "{}-{:02}".format(year,month)
    return date

this_month = date_to_string(year,month)

months.append(this_month)
for i in range (0,12):
    if month == 12:
        year +=1
        month = 1
    else:
        month+=1
    months.append(str(date_to_string(year,month)))

data_connections=[]
for month in months:
    try :
        data_connections.append(monthly_connections("'{}%'".format(month)))
    except :
        data_connections.append(0)



conn.close()