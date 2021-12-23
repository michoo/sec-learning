This is a simple Linux encryption algorithm. It has two basic functions: [./encrypt SOURCE DESTINATION] will prompt you for a password to encrypt the file. [./encrypt SOURCE DESTINATION QUICK] will use a hard-coded default password. Flag #1 uses the quick method, so the algorithm can be reversed engineered quite easily. Flag #2 uses the other method, so it will have to be brute forced using the rocksmall.txt word list and a custom script you wrote.

g++ -o main main.c 

This is a simple Linux encryption algorithm. It has two basic functions: [./encrypt SOURCE DESTINATION] will prompt you for a password to encrypt the file. [./encrypt SOURCE DESTINATION QUICK] will use a hard-coded default password. Flag #1 uses the quick method, so the algorithm can be reversed engineered quite easily. Flag #2 uses the other method, so it will have to be brute forced using the rocksmall.txt word list and a custom script you wrote.

Use the algorithm your made during Flag #1 and script a bruteforce with rocksmall.txt.

The content of the file looks like this: You found a flag! <[MD5]>


g++ -o mainNew mainNew.c 


pour supprimer les loup'es
rm flag.txt.*.dec

grep -nr 'You found a flag! <' .
./flag.txt.766.dec:1:You found a flag! <9zwnex7gp2roqt3p628lobx6986jskp9>

