## -*- coding: utf-8 -*-
import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials as scc
from dotenv import load_dotenv
import psycopg2 as ptgs
import os
from datetime import datetime as dt

load_dotenv()                                                                   # reads variables from a .env file and get them with os.getenv()

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

#Establishing Spotify oauth connection
try:                                                                            
    sp = spotipy.Spotify(auth_manager=scc())
    connection_function("Connected", None, "spotify")

    #API call
    #results = sp.search(q='Drake', type='artist', limit=1)
    results = sp.artist('3TVXtAsR1Inumwj472S9r4')
    print(json.dumps(results, indent=2))

except Exception as e:
    connection_function(None, e, "spotify")
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

