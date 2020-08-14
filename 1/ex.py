from pyredis import Client

client = Client(host="localhost")
client.ping()