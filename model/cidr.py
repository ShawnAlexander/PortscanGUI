import ipaddress

def parseIP(cidrNotation):
    addressSplit = cidrNotation.split('/')
    ip = addressSplit[0]
    cidrSubnet = addressSplit[1]

    ipSplit = ip.split('.')
    return (ipSplit, cidrSubnet)

def convertCidrToDec(cidrSubnet):
    netmask = ""
    for x in range(0, int(cidrSubnet)):
        netmask += str(1)

    for x in range(0, 32 - int(cidrSubnet)):
        netmask += str(0)

    netmask1 = netmask2 = netmask3 = netmask4 = ""
    for x in range(0, 8):
        netmask1 += str(netmask[x])
    for x in range(8, 16):
        netmask2 += str(netmask[x])
    for x in range(16, 24):
        netmask3 += str(netmask[x])
    for x in range(24, 32):
        netmask4 += str(netmask[x])

    netmask1 = str(int(netmask1, base=2))
    netmask2 = str(int(netmask2, base=2))
    netmask3 = str(int(netmask3, base=2))
    netmask4 = str(int(netmask4, base=2))
    return(netmask1, netmask2, netmask3, netmask4)

def printIPsInSubnet(ip, netmask):
    if int(netmask[2]) < 255:
        count3 = 255-int(netmask[2])
        for loop3 in range (0, count3):
            for loop4 in range (1,256):
                print("{}.{}.{}.{}".format(ip[0], ip[1], loop3, loop4))
    elif int(netmask[3]) < 255:
        count4 = 255-int(netmask[3])
        for loop4 in range (1, count4):
            print("{}.{}.{}.{}".format(ip[0], ip[1], ip[2], loop4))

def main():
    print("Your Name, Python - CIDR Notation")

    cidrNotation = input("Enter your network in CIDR. e.g 192.168.10.0/30: ")

    parseString = parseIP(cidrNotation)
    ip = parseString[0]
    cidrSubnet = parseString[1]
    print("Using my own functions")
    print("IP:{}.{}.{}.{}\tCIDR:{}".format(ip[0], ip[1],ip[2],ip[3],cidrSubnet))

    netmask = convertCidrToDec(cidrSubnet)
    print("subnet: {}.{}.{}.{}".format(netmask[0],netmask[1],netmask[2],netmask[3]))
    print("IPs in subnet:")
    printIPsInSubnet(ip, netmask)

    # Let the ipaddress library do the work for you
    print("\nUsing import ipaddress:")
    network = ipaddress.ip_network(cidrNotation)
    print("IP:{}\tCIDR:{}".format(network, cidrSubnet))
    print("subnet:{}".format(network.netmask))
    print("IPs in subnet:")
    for hosts in network.hosts():
        print(hosts)

if __name__  == "__main__":
    main()