export IP=10.129.124.102

## ENUMERATION :

```bash
Nmap 7.92 scan initiated Wed Mar 23 13:06:03 2022 as: nmap -sC -sV -p- -oN ./nmap.txt -vvv IP
Nmap scan report for 10.129.131.8
Host is up, received syn-ack (0.052s latency).
Scanned at 2022-03-23 13:06:03 GMT for 62s
Not shown: 65532 closed tcp ports (conn-refused)
PORT     STATE SERVICE REASON  VERSION
22/tcp   open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 b4:de:43:38:46:57:db:4c:21:3b:69:f3:db:3c:62:88 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDqz2EAb2SBSzEIxcu+9dzgUZzDJGdCFWjwuxjhwtpq3sGiUQ1jgwf7h5BE+AlYhSX0oqoOLPKA/QHLxvJ9sYz0ijBL7aEJU8tYHchYMCMu0e8a71p3UGirTjn2tBVe3RSCo/XRQOM/ztrBzlqlKHcqMpttqJHphVA0/1dP7uoLCJlAOOWnW0K311DXkxfOiKRc2izbgfgimMDR4T1C17/oh9355TBgGGg2F7AooUpdtsahsiFItCRkvVB1G7DQiGqRTWsFaKBkHPVMQFaLEm5DK9H7PRwE+UYCah/Wp95NkwWj3u3H93p4V2y0Y6kdjF/L+BRmB44XZXm2Vu7BN0ouuT1SP3zu8YUe3FHshFIml7Ac/8zL1twLpnQ9Hv8KXnNKPoHgrU+sh35cd0JbCqyPFG5yziL8smr7Q4z9/XeATKzL4bcjG87sGtZMtB8alQS7yFA6wmqyWqLFQ4rpi2S0CoslyQnighQSwNaWuBYXvOLi6AsgckJLS44L8LxU4J8=
|   256 aa:c9:fc:21:0f:3e:f4:ec:6b:35:70:26:22:53:ef:66 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBIuoNkiwwo7nM8ZE767bKSHJh+RbMsbItjTbVvKK4xKMfZFHzroaLEe9a2/P1D9h2M6khvPI74azqcqnI8SUJAk=
|   256 d2:8b:e4:ec:07:61:aa:ca:f8:ec:1c:f8:8c:c1:f6:e1 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIB7eoJSCw4DyNNaFftGoFcX4Ttpwf+RPo0ydNk7yfqca
80/tcp   open  http    syn-ack Apache httpd 2.4.41 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-generator: WordPress 5.8.1
|_http-title: Backdoor &#8211; Real-Life
1337/tcp open  waste?  syn-ack
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

```bash
whatweb 10.129.124.102
http://10.129.124.102 [200 OK] Apache[2.4.41], Country[RESERVED][ZZ], Email[wordpress@example.com], HTML5, HTTPServer[Ubuntu Linux][Apache/2.4.41 (Ubuntu)], IP[10.129.124.102], JQuery[3.6.0], MetaGenerator[WordPress 5.8.1], PoweredBy[WordPress], Script, Title[Backdoor &#8211; Real-Life], UncommonHeaders[link], WordPress[5.8.1]
```

## Trying to exploit vulnerable WordPress plugins

--> WordPress built website with vulnerable plugins => scan the website with WPScan

```bash
wpscan --url http://10.129.124.102/ --api-token [retrieve token on wpscan.com] --enumerate p,u --plugins-detection aggressive
```

--> results : vulnerable plugin akismet at url http://10.129.124.102/wp-content/plugins/akismet

When we visit this URL, it is not available, so we go up a directory to http://10.129.124.102/wp-content/plugins/ and we see that there is another plugin that can be exploited : **ebook-download** (see https://www.exploit-db.com/exploits/39575)

We successfully manage to download the example given in the PoC --> The website is vulnerable to LFI exploits.

/etc/passwd didn't give any useful information

Another guess would be to bruteforce /proc/[PID]/cmdline to see what are the processes running on the machine and what were the commands used to start them. To do that, we use the Intruder of Burpsuite. Long story short, we discover that an instance of gdbserver is running on port 1337. It wasn't discovered by nmap or rustscan because it was started with the option --once which means that once a connection has been established, every other attempt is rejected.

See https://infosecwriteups.com/backdoor-hackthebox-walkthrough-6e4e8b483db1 for the end
