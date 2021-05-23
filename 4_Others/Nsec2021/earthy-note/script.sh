#!/bin/bash
# PR07-37-scan

if echo -en "<PROCHECKUP> / HTTP/1.1\nHost: earthy-notes.ctf\nConnection: close\nContent-length: 0\nContent-length: 0\n\n" | socat earthy-notes.ctf 80 | grep -i '<PROCHECKUP>' > /dev/null
then
       echo "earthy-notes.ctf is VULNERABLE!"
fi
