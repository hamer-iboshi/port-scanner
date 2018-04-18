#!/usr/bin/env python3
#coding: utf-8 
import sys
import socket
import select


#arguments
timeout_in_seconds = 1
arg = sys.argv[1:]
try:
	ip_addr = arg[0]
	port_addr = arg[1]
except:
	print("Wrong argumnts\nUsage:\n./scanner <IP> <PORT>")
	sys.exit()

parsed_ip = ip_addr.split('.')
range_ip = parsed_ip[-1].split('-')
prefix_ip = '.'.join(parsed_ip[0:-1])
if len(range_ip)<=1:
		range_ip.append(range_ip[0]) 

range_ports = port_addr.split('-')
if len(range_ports)<=1:
	range_ports.append(range_ports[0])

print("IP:",prefix_ip+'.',range_ip," Port: ",range_ports)
for ip in range(int(range_ip[0]),int(range_ip[1])+1):
	print("--------------------------------------")
	print("IP:",prefix_ip+'.'+str(ip))
	for port in range(int(range_ports[0]),int(range_ports[1])+1):  
		sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
		#sock.setblocking(0)
		result = sock.connect_ex((prefix_ip+'.'+str(ip),int(port)))
		if result==0:
			print('Porta (',port,'): Open')
			ready = select.select([sock], [], [], timeout_in_seconds)
			if ready[0]:
				data = sock.recv(256)
				print(data.decode('utf-8','ignore'))
			else:
				print("Sem informação")
		sock.close()
	print("--------------------------------------\n\n")
