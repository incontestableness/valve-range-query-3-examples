#!/usr/bin/env python3

import pprint
from valverangequery import *


# This will scan 208.78.164.0 - 208.78.165.255 (CIDR 208.78.164.0/23)
axlimits = [164,165]
aylimits = [0,255]
base_ipaddr = "208.78"
scanner = SourceScanner(timeout=120.0, axlimits=axlimits, aylimits=aylimits, base_ipaddr=base_ipaddr)

servers = scanner.scan_servers()
for server_obj in servers: 
	data = {
		'map_name' : server_obj['map'], 
		'host' : server_obj['host_ip'],	
		'num_players' : server_obj['numplayers'], 
		'max_players' : server_obj['maxplayers'], 
		'server_name' : server_obj['name'], 
		'game_name' : server_obj['game'], 
		'folder' : server_obj['folder'], 
		'protocol' : server_obj['protocol'], 
		'num_bots' : server_obj['bots'], 
		'num_humans' : server_obj['numplayers'] - server_obj['bots']
	}
	if data["folder"] == b"tf": 
		pprint.pprint(data)
