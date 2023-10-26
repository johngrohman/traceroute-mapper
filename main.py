import getloc
import os
import io
import traceroute

def main():
    print("Input IP address")
    ipaddress = input()
    output = os.system(f'traceroute {ipaddress} > file.txt')
    file = io.open('file.txt')
    solution = file.read()
    iplist = traceroute.parseTraceRoute(solution, ipaddress)
    result = getloc.getLocations(iplist)
    for r in result:
        print(r.city)

    # solutions = getloc.getLocations(ipaddress)
    

if __name__ == "__main__":
    main()