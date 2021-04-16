# Web Directory listing

## Robots.txt

* http://target.com/robots.txt

## Brute Force

* dirb http://target.com:80 /usr/share/wordlists/dirb/common.txt
* wfuzz -c --hc 404 -z file,/usr/share/wordlists/wfuzz/general/megabeast.txt http://target.com/FUZZ
* gobuster dir -u http://bank.htb -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php -o scans/gobuster-bank.htb-root-medium-php -t 50
* python3 dirsearch.py -e php,html,js -u https://target -w /path/to/wordlist 
https://github.com/maurosoria/dirsearch