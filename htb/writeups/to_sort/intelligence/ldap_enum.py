#!/usr/bin/env python3
import ldap3
import json
 
 
def find_user_entries(host, port, ssl=False):
    server = ldap3.Server(host, get_info=ldap3.ALL, port=port, use_ssl=ssl)
    connection = ldap3.Connection(server)
    connection.bind()
    root_domain = server.info.__dict__['raw']['rootDomainNamingContext'][0].decode()
    connection.search(search_base=root_domain, search_filter='(&(objectClass=person))', search_scope='SUBTREE', attributes='*')
    return connection.entries
 
 
HOST = "dc.intelligence.htb"
PORT = 389
entries = find_user_entries(HOST, PORT)
with open(HOST + ".json", "w") as f:
    json.dump([json.loads(e.entry_to_json()) for e in entries], f)
