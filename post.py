#!/usr/bin/env python3

from tcp import *

data = (
	"POST /path/script.cgi HTTP/1.0\r\n"
	"Content-Type: application/x-www-form-urlencoded\r\n"
	"Content-Length: 25\r\n\r\n"
	"thing=Stuff&trinket=gizmo"
)

send(data, "127.0.0.1", 8000)

input("Press Enter to continue...")


