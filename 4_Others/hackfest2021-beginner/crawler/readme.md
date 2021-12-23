# Crawler
sudo nmap -sC -sV -O -oA nmap/initial beginner-web.hfctf.ca

tarting Nmap 7.92 ( https://nmap.org ) at 2021-11-20 21:40 EST
Nmap scan report for beginner-web.hfctf.ca (44.197.198.61)
Host is up (0.21s latency).
rDNS record for 44.197.198.61: ec2-44-197-198-61.compute-1.amazonaws.com
Not shown: 992 closed tcp ports (reset)
PORT     STATE    SERVICE      VERSION
22/tcp   open     ssh          OpenSSH 7.6p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 ea:64:5e:9e:f1:34:a5:fb:3f:06:6e:cc:2b:02:f4:e2 (RSA)
|   256 58:d0:1c:1f:02:0d:c6:f2:3c:cb:5c:7d:74:7d:d8:11 (ECDSA)
|_  256 d0:cf:8d:78:85:f0:c7:a5:b1:b3:59:4b:c2:05:b0:14 (ED25519)
25/tcp   filtered smtp
53/tcp   open     domain       ISC BIND 9.11.4-P2 (RedHat Enterprise Linux 7)
| dns-nsid: 
|_  bind.version: 9.11.4-P2-RedHat-9.11.4-26.P2.el7_9.7
80/tcp   open     http         Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-server-header: Apache/2.4.29 (Ubuntu)
135/tcp  filtered msrpc
139/tcp  filtered netbios-ssn
445/tcp  filtered microsoft-ds
1433/tcp filtered ms-sql-s


sudo nmap -sU -sT -p0-65535 -oA nmap/all beginner-web.hfctf.ca


udp
netcat -u host port
tcp scan
netcat -z -v beginner-web.hfctf.ca 1-65535