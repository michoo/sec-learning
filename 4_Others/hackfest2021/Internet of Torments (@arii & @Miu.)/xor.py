#!/usr/bin/python

import sys

if len(sys.argv) != 4:
  print "Usage: ./xor1 infile outfile keynum"
  print "k is a number in base 10"
  exit()

f = open(str(sys.argv[1]), "rb")
g = open(str(sys.argv[2]), "ab")
k = int(sys.argv[3])

out = ""
try:
    byte = f.read(1)
    while byte != "":
        xbyte = ord(byte) ^ k
        out += chr(xbyte)
        byte = f.read(1)
finally:
    f.close()

g.write(out)
g.close()
