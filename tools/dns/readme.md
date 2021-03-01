# DNS


## A - records

A stands for address.

The A record maps a name to one or more IP addresses, when the IP are known and stable. So that would be 123.244.223.222 => example.com

AAAA - points to a IPv6 Record

## CNAME

The CNAME record connects a name to another name. An example of that would be:

www.example.com,CNAME,www.example.com.cdn.cloudflare.net.

Another example is. If you have the domains mail.example.com and webmail.example.com. You can have webmail.example.com point to mail.example.com. So anyone visiting webmail.example.com will see the same thing as mail.example.com. It will NOT redirect you. Just show you the same content.

Another typical usage of CNAME is to link www.example.com to example.com

CNAME is quite convenient. Because if you change the A-record. The IP-address, you don't need to change the other subdomains, like ftp.example.com or www.example.com. Since they both point to example.com, which is a A-record and points directly to the IP.

Another note. If foo.example.com points to bar.example.com, that mean that bar.example.com is the CNAME (Canonical/real/actual Name) of foo.example.com.

## Alias

Kind of like CNAME in that it points to another name, not an IP.

## MX - Mail exchange

MX records tell the DNS system where to send all that email you receive.
https://en.wikipedia.org/wiki/MX_record

## TXT Records

TXT records allow the domain owner to authenticate themselves by posting secret codes within their DNS. 

## WHOIS enumeration
```bash
whois domain-name-here.com 
```

## Perform DNS IP Lookup
```bash
dig a domain-name-here.com @nameserver 
```

## Perform MX Record Lookup
```bash
dig mx domain-name-here.com @nameserver
```

## Perform Zone Transfer with DIG
```bash
dig axfr domain-name-here.com @nameserver
```

## DNS Zone Transfers

### Windows DNS zone transfer

```bash
nslookup -> set type=any -> ls -d blah.com
```

### Linux DNS zone transfer
```bash
dig axfr blah.com @ns1.blah.com
```


## DNS recon

dnsrecon -h


dnsrecon -r 127.0.0/24 -n IP_DNS_SERVER
dnsrecon -r 127.1.0/24 -n IP_DNS_SERVER
dnsrecon -r 10.129.29.0/24 -n IP_DNS_SERVER