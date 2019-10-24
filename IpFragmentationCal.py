import argparse
import math
parser = argparse.ArgumentParser()

parser.add_argument("-mtu", "--mtu", help="MTU", type=int)
parser.add_argument("-size", "--size", help="Data Size", type=int)

args = parser.parse_args()
size = args.size
mtu = args.mtu
length = mtu - 20
offset = length / 8
numOfFrag = math.ceil((size - 20) / length)

print(numOfFrag)


for i in range(numOfFrag):
    print("Offset of Datagram "+ str(i) + ": " + str(math.ceil(i*offset)))



# print( "Hostname: {}, User: {}, Password: {}, size: {} ".format(
#         args.hostname,
#         args.username,
#         args.password,
#         args.size
#         ))