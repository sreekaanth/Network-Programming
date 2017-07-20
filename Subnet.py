from netaddr import *
import pprint
import math
ip = input("enter the IP address in the specific format")
ip = IPNetwork(ip)
print(ip.network)
print(ip.netmask)
print(ip.broadcast)
