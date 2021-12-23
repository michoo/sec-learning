la cle
01100001 01010110 01100101 01110010 01111001 01010011 01110100 01110010 01101111 01101110 01100111 01010000 01100001 01110011 01110011 01110000 01101000 01110010 01100001 01110011 01100101

aVery...

https://linoxide.com/gpg-command-encrypt-decrypt-file/
gpg -d FILE.zip.gpg

on se retrouve avec le premier flag



une image affiche d2VsbFBsYXllZA==

echo "d2VsbFBsYXllZA=="|base64 -d
wellPlayed

sudo apt install steghide

a utiliser avec steghide extract -sf FILE.jpg 
on recupere un FLAG.mp3 qui quand on l' ecoute ne fait pas de sont

en regardant le fichier on voit qu' il est compresse
binwalk --extract FLAG.mp3
on recupere le dernier flag
