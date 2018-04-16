#!/usr/bin/env python3
import sys
import socket

#arguments
arg = sys.argv[1:]
try:
	ip_addr = arg[0]
	port_addr = arg[1]
except:
	print("Wrong argumnts\nUsage:\n./scanner <IP> <PORT>")
	sys.exit()

ip = ip_addr.split('-')[0]
ports = port_addr.split('-')
print(ip,"port: ",ports)
for port in range(int(ports[0]),int(ports[1])+1):  
	sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
	result = sock.connect_ex((ip_addr,int(port)))
	if result==0:
		print('Open ',port)
		print(sock.recv(256))
	sock.close()
