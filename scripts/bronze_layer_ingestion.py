## -*- coding: utf-8 -*-
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials as scc
from dotenv import load_dotenv
import psycopg2 as ptgs
import os
from datetime import datetime as dt

load_dotenv()   # reads variables from a .env file and get them with os.getenv()

#Error function
def connection_function(k, e):
    if k is not None and e is None:
        c_time = dt.now().strftime("%d-%m-%Y %H:%M:%S")
        
        print(f"connection has been established at: {c_time}")

    else:    
        e_time = dt.now().strftime("%d-%m-%Y %H:%M:%S")
        e_type = type(e).__name__
        e_message = str(e)
    
        print(f"{e_type} occurred at {e_time} with message {e_message}")

#Establishing Spotify oauth connection
try:
    sp = spotipy.Spotify(auth_manager=scc())
    connection_function("Connected", None)

except Exception as e:
    connection_function(None, e)
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

    connection_function("Connected", None)

except Exception as e:
    connection_function(None, e)
    raise

finally:
    if conn is not None:
        conn.close()