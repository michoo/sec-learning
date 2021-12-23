#!/usr/bin/python
import subprocess


# Open a file
myfile = open("rocksmall.txt", "r")

lines = myfile.readlines()
i = 0
for line in lines:
    i = i+1
    print(line.strip())
    output = "{}{}{}".format("flag.txt.", i, ".dec")
    subprocess.call(["./mainNew", "flag.txt.enc",output, line.strip() ])
    with open(output) as f:
        for line in f:
            if "HF-" in line:
                message = "{}{}".format("BRUTUS ", line)
                print(message)

# Close opend file
myfile.close()