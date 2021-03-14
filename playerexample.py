#!/usr/bin/env python3

import pprint
from valverangequery import *


# Specify the port as a keyword argument for alternative ports.
# The default port is 27015. Official Valve servers run on several ports per IP.
player_query = PlayerQuery("208.78.164.167")#, port=12345)
player_list = player_query.player()
for player in player_list: 
	print(player)
