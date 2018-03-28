#!/usr/bin/env python3
import sys

#arguments
arg = sys.argv[1:]
try:
	ip_addr = arg[0]
	port_addr = arg[1]
except:
	print("Wrong argumnts\nUsage:\n./scanner <IP> <PORT>")
	sys.exit()

ip = ip_addr.split('-')[0]
sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
