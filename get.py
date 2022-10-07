#!/usr/bin/env python3

from tcp import *

data = (
	"GET /index.html HTTP/1.1\r\n"
	"Host: 127.0.0.1\r\n"
	"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
	" (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246\r\n"
	"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
	"Accept-Language: en-US,en;q=0.5\r\n"
	"Accept-Encoding: gzip, deflate\r\n"
	"DNT: 1\r\n"
	"Connection: close\r\n"
	"Upgrade-Insecure-Requests: 1\r\n\r\n"
)

send(data, "127.0.0.1", 8000)

input("Press Enter to continue...")


