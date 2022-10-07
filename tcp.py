#!/usr/bin/env python3

import socket

'''
@param request: A raw http request
@param host_ip: The name of the host to connect to
@param host_port: The port on the host to connect to
<br>
Sends a request to a specified host over TCP and reads a reply
'''
def send(request, host_ip, host_port):
	# Initialize a TCP client socket using SOCK_STREAM
	tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	try:
		# Establish connection to TCP server and exchange data
		tcp_client.connect((host_ip, host_port))
		tcp_client.sendall(request.encode())
		
		print(request)
		
		# Read data from the TCP server and close the connection
		received = b""
		while True:
			buf = tcp_client.recv(4096)
			if buf:
				received += buf
			else:
				break
		print(str(received, 'UTF-8'))
	finally:
		tcp_client.close()


