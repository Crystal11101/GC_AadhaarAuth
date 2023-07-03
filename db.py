from cassandra.cluster import Cluster

#docker run -p 9042:9042 --name cassandra -d cassandra
cluster = Cluster(['localhost'], port=9042)
session = cluster.connect()
# session.set_keyspace('db_ks1')

row = session.execute("select release_version from system.local").one()
if row:
  print(row[0])
else:
  print("An error occurred.")