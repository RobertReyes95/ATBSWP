import sys #system functions and parameters
import socket 
from datetime import datetime

# Define Target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Translates hostname to IPV4 
else: 
    print("Invalid amount of argumensts")
    print("Syntax python3 scanner.py <ip>")
    sys.exit()

print("-" * 50 )
print("Scanning target: "+ target)
print('Time Started: '+str(datetime.now()))
print("-" * 50)

try: 
        for port in range(20,85) :
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1) # this is a float
            results = s.connect_ex((target,port)) #Error inicator
            print("Checking port {}".format(port))
            if results == 0: 
                print("Port {} is open".format(port))
            s.close()

except KeyboardInterrupt: 
    print("\nExiting program")
    sys.exit()

except socket.gaierror: 
    print('Hostname could not be resolved')
    sys.exit()

except socket.error:
    print("Couldn't connect to server") 
    sys.exit()