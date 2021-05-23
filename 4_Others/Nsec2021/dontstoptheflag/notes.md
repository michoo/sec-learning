# donstoptheflag


strings dontstoptheflag | grep "$(printf '\[!\]')"
strings dontstoptheflag | grep "$(printf '\[+\]')"
objdump -D ./dontstoptheflag > out.asm  
strace ./dontstoptheflag   
ltrace ./dontstoptheflag     
grep "5b 21" out.asm     
grep "5b 2b" out.asm             

gcc -shared -fPIC -o fake.so fake.c   
strace -E LD_PRELOAD=./fake.so ./dontstoptheflag                    