from py2neo import Graph, Node, Relationship
from map import compare
import os, json
from dotenv import load_dotenv

load_dotenv()

graph = Graph(
    os.getenv("NEO4J_URI"), 
    auth=(os.getenv("NEO4J_USER"), os.getenv("NEO4J_PASS"))
)

def dbTopics():
    result = graph.run("MATCH (n) RETURN n")
    return list(result)

def merge(new, existing):
    data = compare(new, existing)
    print('\nmapping data: \n')
    for node in data:
        name = node['name']
        status = node['status']
        print(status)
        if 'unique' in status:
            newNode = Node(name=name, learned=False, type='concept')
            graph.create(newNode)