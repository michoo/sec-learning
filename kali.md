# Prepare your pentest lab

## Install Virtualbox

https://www.virtualbox.org/

## Download Kali

https://www.offensive-security.com/kali-linux-vm-vmware-virtualbox-image-download/ 

check fingerprint:

```bash
sha256sum file.zip
```

Unzip and import ova file into Virtualbox.

## Configuration of downloaded VM

- remove all useless stuff in vm configuration (A:, CD,..)
- set network to NAT
- set dragndrop and copy past if you need it
- deactivate audio

## Start Kali

Update OS:

```bash
sudo apt update
sudo apt upgrade
```

## Install and activate a Firewall

```bash
sudo apt install ufw gufw
sudo ufw enable
```

and set and deny all to all input.

## Install an antivirus

```bash
sudo apt install clamav clamtk
```

Why not...

## Change macadress

```bash
sudo ifconfig wlan0 down
sudo macchanger -r wlan0
sudo macchanger -s wlan0
sudo ifconfig wlan0 up
```

Youĺl have to redo that at restart

## Change Kali default password

for user: Kali

```bash
sudo passwd
```

for user: root

```bash
su
sudo passwd
```

## Regenerate ssh keys

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

## Ip forwarding on your host machine and into your kali machine

### Check

```bash
sudo sysctl net.ipv4.ip_forward
sudo cat /proc/sys/net/ipv4/ip_forward
```

if 1: then it's forwarding

### Deactivate ipv4 forwarding and deactivate ipv6(all)

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

# Checklist before connecting to Hack The Box

- check firewall is up
- change mac adress
- check ip forwarding is deactivated
- start your own vpn (optional)