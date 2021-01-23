# Sec-learning

This project is for learning pentest in a oscp context with Hack The Box. It's based on numerous ressources. Hope you'll enjoy!

## OSCP rules

https://help.offensive-security.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide

## Hack The Box

Get an invite https://www.hackthebox.eu/invite
Your first CTF :)

## Prepare your pentest lab

### Install Virtualbox

https://www.virtualbox.org/

### Download Kali

https://www.offensive-security.com/kali-linux-vm-vmware-virtualbox-image-download/ 

check fingerprint:

```bash
sha256sum file.zip
```

Unzip and import ova file into Virtualbox.

### Configuration of downloaded VM

- remove all useless stuff in vm configuration (A:, CD,..)
- set network to NAT
- set dragndrop and copy past if you need it
- deactivate audio

### Start Kali

Update OS:

```bash
sudo apt update
sudo apt upgrade
```

### Install and activate a Firewall

```bash
sudo apt install ufw gufw
sudo ufw enable
```

and set and deny all to all input.

### Install an antivirus

```bash
sudo apt install clamav clamtk
```

Why not...

### Change macadress

```bash
sudo ifconfig wlan0 down
sudo macchanger -r wlan0
sudo macchanger -s wlan0
sudo ifconfig wlan0 up
```

Youĺl have to redo that at restart

### Change Kali default password

for user: Kali

```bash
sudo passwd
```

for user: root

```bash
su
sudo passwd
```

### Regenerate ssh keys

This will move your default keys to the new folder...

```bash
su
cd /etc/ssh/
mkdir default_kali_keys
mv ssh_host_* default_kali_keys/
```

Regenerate the keys:

```bash
sudo dpkg-reconfigure openssh-server
Creating SSH2 RSA key; this may take some time ...
Creating SSH2 DSA key; this may take some time ...
Creating SSH2 ECDSA key; this may take some time ...
insserv: warning: current start runlevel(s) (empty) of script `ssh' overrides LSB defaults (2 3 4 5).
insserv: warning: current stop runlevel(s) (2 3 4 5) of script `ssh' overrides LSB defaults (empty).
```

Verify ssh key hashes are different:

```bash
md5sum ssh_host_*
cd default_kali_keys/
md5sum *
```

### Ip forwarding on your host machine and into your kali machine

#### Check

```bash
sudo sysctl net.ipv4.ip_forward
sudo cat /proc/sys/net/ipv4/ip_forward
```

if 1: then it's forwarding

#### Deactivate ipv4 forwarding and deactivate ipv6(all)

```bash
sudo sysctl -w net.ipv4.ip_forward=0
sudo nano /etc/sysctl.conf
```

and add:

```bash
net.ipv4.ip_forward = 0
net.ipv6.conf.all.forwarding=0
```

```bash
sudo sysctl -p
```

## Checklist before connecting to Hack The Box

- check firewall is up
- change mac adress
- check ip forwarding is deactivated
- start your own vpn (optional)

## Reports

### Installation

- MarkdownPP
pip install MarkdownPP

- Pandoc
https://github.com/jgm/pandoc/releases
https://github.com/jgm/pandoc/releases/download/2.11.3.2/pandoc-2.11.3.2-1-amd64.deb

```bash
sudo dpkg -i pandoc.*.deb
```

- LaTeX (eg. TeX Live) in order to get pdflatex or xelatex

```bash
sudo apt install texlive-full
```

- Eisvogel Pandoc LaTeX PDF Template (already include)
https://github.com/Wandmalfarbe/pandoc-latex-template/blob/master/eisvogel.tex

### Reports scripts

- ./new_report.sh will generate a new directory with everything to start writing a report
- into report directory (date), you'll find a script ./generate.sh, it will generate everything pdf, and 7z

## Inspiration

### Experience OSCP

https://rana-khalil.gitbook.io/hack-the-box-oscp-preparation/
https://github.com/rkhal101/Hack-the-Box-OSCP-Preparation
https://ranakhalil101.medium.com/my-oscp-journey-a-review-fa779b4339d9

### Videos IPPSEC

https://www.youtube.com/channel/UCa6eh7gCkpPo5XXUDfygQQA

### Reports templates

https://liodeus.github.io/2020/10/19/OSCP-exam-report-training.html
https://www.offensive-security.com/pwk-online/PWKv1-REPORT.odt
