#!/usr/bin/env python3

import netaddr
import pprint
import valverangequery


net = netaddr.IPNetwork("208.78.164.0/23")
x = []
for i in net: 
	x.append(str(i))
scanner = valverangequery.SourceScanner(port=27015, timeout=120.000, force_list=x)

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
