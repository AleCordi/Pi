#!/usr/bin/env python3
#Open file hostname in a list
with open('/Users/alemacco/Desktop/list/server_list.txt') as f:
    servers = f.read().splitlines()
    print(servers)