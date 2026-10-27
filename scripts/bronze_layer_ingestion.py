## -*- coding: utf-8 -*-
import requests as rq
import json
from dotenv import load_dotenv
import psycopg2 as ptgs
import os
from datetime import datetime as dt

load_dotenv()                                                                   # reads variables from a .env file and get them with os.getenv()
musicbrainz_api_url = "https://musicbrainz.org/ws/2/"                           # musicbrainz initial api url before params

#Connection-Check function
def connection_function(k, e, service):                                                 
    if k is not None and e is None:
        c_time = dt.now().strftime("%d-%m-%Y %H:%M:%S")
        
        print(f"{service} connection has been established at: {c_time}")

    else:    
        e_time = dt.now().strftime("%d-%m-%Y %H:%M:%S")
        e_type = type(e).__name__
        e_message = str(e)
    
        print(f"{service} failed: {e_type} occurred at {e_time} with message {e_message}")

#Establishing Musicbrainz connection
try:                                                                            
    response = rq.get(musicbrainz_api_url)
    if response.status_code == 200:
        connection_function("Connected", None, "musicbrainz")
    else: raise ConnectionError(f"Unexpected status code: {response.status_code}")

except Exception as e:
    connection_function(None, e, "musicbrainz")
    raise


#Connecting to Postgres
conn = None

try:
    conn = ptgs.connect(
        dbname = os.getenv("POSTGRES_DB"),
        user = os.getenv("POSTGRES_USER"),
        password = os.getenv("POSTGRES_PASSWORD"),
        host = "database",
        port = 5432
    )

    connection_function("Connected", None, "postgres")

except Exception as e:
    connection_function(None, e, "postgres")
    raise

finally:
    if conn is not None:
        conn.close()

