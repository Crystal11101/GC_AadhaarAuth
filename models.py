# from cassandra.cqlengine import columns
# from cassandra.cqlengine.models import Model
from pydantic import BaseModel

class User(BaseModel):
    __keyspace__="db_ks1"
    username: str
    password: str
