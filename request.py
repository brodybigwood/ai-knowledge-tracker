import commandr, database
from topics import getTopics









concepts = []

def process(data):
    concepts = database.dbTopics()
    conc_existing = []
    conc_new = []
    for node in concepts:
        conc_existing.append(node.get("name", "Unknown"))
    for node in data:
        conc_new.append(node['name'])
    return conc_new, conc_existing


def msg():
    print('enter your message: ')
    prompt = input()
    msg = commandr.getJSON(getTopics(), prompt)
    print('\nend of initial response\n')
    new, existing = process(msg)

    database.merge(new, existing)
    
    return msg

msg()

