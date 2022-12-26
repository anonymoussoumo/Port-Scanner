#!/usr/bin/python3

import socket
import sys
import time
import threading
import pyfiglet

usage = "python3 port_scanner.py TARGET START_PORT END_PORT"

text = pyfiglet.figlet_format("PORT SCANNER")
print(text)

start_time = time.time()

if(len(sys.argv) != 4):
    print(usage)
    sys.exit()

try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
        print("Name Resolution Error")
        sys.exit()

start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

print("Scanning Target",target)

def scan_port(port):
        #print("Scanning port:",port)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        conn = s.connect_ex((target, port))
        if(not conn):
            print("Port {} is OPEN".format(port))
        s.close()

for port in range(start_port, end_port+1):

        thread = threading.Thread(target = scan_port, args = (port,))
        thread.start()

end_time = time.time()
print("Time Taken:",end_time - start_time,'seconds')        