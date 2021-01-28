# Nmap


## Nmap target
default scans, which will scan 1000 TCP ports  

```bash
# Scan an IP
nmap 192.168.1.1
# Scan a host
nmap www.testhostname.com
# Scan a range
nmap 192.168.1.1-20
# Scan a subnet
nmap 192.168.1.0/24
# Scan from a list file
nmap -iL list-of-ips.txt

```

## Nmap port selection

```bash
# Scan a port
nmap -p 22 192.168.1.1
# Scan a range
nmap -p 1-100 192.168.1.1
# Scan 100 most famous port (fast)
nmap -F 192.168.1.1
# Scan all ports
nmap -p- 192.168.1.1
```
## Nmap scan type

```bash
# Scan TCP CONNECT
nmap -sT 192.168.1.1
# Scan TCP SYN(default)
nmap -sS 192.168.1.1
# Scan UDP ports
nmap -sU -p 123,161,162 192.168.1.1
# Scan selected ports - ignore discovery
nmap -Pn -F 192.168.1.1

```

## Nmap Service and OS Detection

```bash
# Detect OS and Services 	
nmap -A 192.168.1.1
# Standard service detection 	
nmap -sV 192.168.1.1
# More aggressive Service Detection 	
nmap -sV --version-intensity 5 192.168.1.1
# Lighter banner grabbing detection 	
nmap -sV --version-intensity 0 192.168.1.1
```

## Scripts

Find scripts  
```bash
locate nse | grep script  

```

Find more specific script  
```bash
locate nse | grep dns 

```

Find help for a specific script  
```bash
nmap --script-help=ssl-heartbleed

```

Execute a specific script scan  
```bash
nmap -sV -p 443 --script=ssl-heartbleed.nse 192.168.1.1
```
Execute a regex script scan  
```bash
nmap -sV --script=smb* 192.168.1.1
```

## Scan for DDOS relection

```bash
nmap -sU -A -PN -n -pU:19,53,123,161 --script=ntp-monlist,dns-recursion,snmp-sysdescr 192.168.1.0/2
```

## Detect HeartBleed vulnerability

```bash
nmap -sV -p 443 --script=ssl-heartbleed 192.168.1.0/24
```

## Find ip informations

```bash
nmap --script=asn-query,whois,ip-geolocation-maxmind 192.168.1.0/24
```