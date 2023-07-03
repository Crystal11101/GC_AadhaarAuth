from fastapi import FastAPI, Response
from cassandra.cluster import Cluster
from db import session
from models import User
# Cassandra init
# 127.0.0.1
# cluster = Cluster()
# session = cluster.connect('cassandra') 
# session.set_keyspace('users')

app = FastAPI()
keyspace="db_ks1"
session.set_keyspace('db_ks1')

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post('/post')
        # session.execute("CREATE TABLE IF NOT EXISTS db_ks1.users (username text, password text, PRIMARY KEY (username))")
async def addUser(data:User):
    # select the keyspace and table
    table_name = 'users'

    # build and execute the INSERT query
    query = f"INSERT INTO {table_name} (username, password) VALUES (%s, %s)"
    params = (data.username, data.password)
    session.execute(query, params)
    return "User added"

@app.get('/getAllUsers')
async def getAllUsers():
    table_name='users'
    result = session.execute(f'SELECT * FROM {table_name}')
    return result