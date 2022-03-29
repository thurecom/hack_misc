# Nmap 7.91 scan initiated Thu Oct 14 14:19:34 2021 as: nmap -sC -sV -p- -v -oN nmap seal.htb
Nmap scan report for seal.htb (10.129.239.244)
Host is up (0.0086s latency).
rDNS record for 10.129.239.244: seal
Not shown: 65532 closed ports
PORT     STATE SERVICE    VERSION
22/tcp   open  ssh        OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 4b:89:47:39:67:3d:07:31:5e:3f:4c:27:41:1f:f9:67 (RSA)
|   256 04:a7:4f:39:95:65:c5:b0:8d:d5:49:2e:d8:44:00:36 (ECDSA)
|_  256 b4:5e:83:93:c5:42:49:de:71:25:92:71:23:b1:85:54 (ED25519)
443/tcp  open  ssl/http   nginx 1.18.0 (Ubuntu)
| http-methods: 
|_  Supported Methods: OPTIONS GET HEAD POST
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Seal Market
| ssl-cert: Subject: commonName=seal.htb/organizationName=Seal Pvt Ltd/stateOrProvinceName=London/countryName=UK
| Issuer: commonName=seal.htb/organizationName=Seal Pvt Ltd/stateOrProvinceName=London/countryName=UK
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-05-05T10:24:03
| Not valid after:  2022-05-05T10:24:03
| MD5:   9c4f 991a bb97 192c df5a c513 057d 4d21
|_SHA-1: 0de4 6873 0ab7 3f90 c317 0f7b 872f 155b 305e 54ef
| tls-alpn: 
|_  http/1.1
| tls-nextprotoneg: 
|_  http/1.1
8080/tcp open  http-proxy
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.1 401 Unauthorized
|     Date: Thu, 14 Oct 2021 14:19:43 GMT
|     Set-Cookie: JSESSIONID=node01ne18ri96sxkb10t7lq8h0xm9b46.node0; Path=/; HttpOnly
|     Expires: Thu, 01 Jan 1970 00:00:00 GMT
|     Content-Type: text/html;charset=utf-8
|     Content-Length: 0
|   GetRequest: 
|     HTTP/1.1 401 Unauthorized
|     Date: Thu, 14 Oct 2021 14:19:43 GMT
|     Set-Cookie: JSESSIONID=node01ps8zjnwspck51x9xtjk9xpptv44.node0; Path=/; HttpOnly
|     Expires: Thu, 01 Jan 1970 00:00:00 GMT
|     Content-Type: text/html;charset=utf-8
|     Content-Length: 0
|   HTTPOptions: 
|     HTTP/1.1 200 OK
|     Date: Thu, 14 Oct 2021 14:19:43 GMT
|     Set-Cookie: JSESSIONID=node0v6ybx7taxfsvvwz81epydzy345.node0; Path=/; HttpOnly
|     Expires: Thu, 01 Jan 1970 00:00:00 GMT
|     Content-Type: text/html;charset=utf-8
|     Allow: GET,HEAD,POST,OPTIONS
|     Content-Length: 0
|   RPCCheck: 
|     HTTP/1.1 400 Illegal character OTEXT=0x80
|     Content-Type: text/html;charset=iso-8859-1
|     Content-Length: 71
|     Connection: close
|     <h1>Bad Message 400</h1><pre>reason: Illegal character OTEXT=0x80</pre>
|   RTSPRequest: 
|     HTTP/1.1 505 Unknown Version
|     Content-Type: text/html;charset=iso-8859-1
|     Content-Length: 58
|     Connection: close
|     <h1>Bad Message 505</h1><pre>reason: Unknown Version</pre>
|   Socks4: 
|     HTTP/1.1 400 Illegal character CNTL=0x4
|     Content-Type: text/html;charset=iso-8859-1
|     Content-Length: 69
|     Connection: close
|     <h1>Bad Message 400</h1><pre>reason: Illegal character CNTL=0x4</pre>
|   Socks5: 
|     HTTP/1.1 400 Illegal character CNTL=0x5
|     Content-Type: text/html;charset=iso-8859-1
|     Content-Length: 69
|     Connection: close
|_    <h1>Bad Message 400</h1><pre>reason: Illegal character CNTL=0x5</pre>
| http-auth: 
| HTTP/1.1 401 Unauthorized\x0D
|_  Server returned status 401 but no WWW-Authenticate header.
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Site doesn't have a title (text/html;charset=utf-8).
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port8080-TCP:V=7.91%I=7%D=10/14%Time=61683C7F%P=x86_64-pc-linux-gnu%r(G
SF:etRequest,F6,"HTTP/1\.1\x20401\x20Unauthorized\r\nDate:\x20Thu,\x2014\x
SF:20Oct\x202021\x2014:19:43\x20GMT\r\nSet-Cookie:\x20JSESSIONID=node01ps8
SF:zjnwspck51x9xtjk9xpptv44\.node0;\x20Path=/;\x20HttpOnly\r\nExpires:\x20
SF:Thu,\x2001\x20Jan\x201970\x2000:00:00\x20GMT\r\nContent-Type:\x20text/h
SF:tml;charset=utf-8\r\nContent-Length:\x200\r\n\r\n")%r(HTTPOptions,108,"
SF:HTTP/1\.1\x20200\x20OK\r\nDate:\x20Thu,\x2014\x20Oct\x202021\x2014:19:4
SF:3\x20GMT\r\nSet-Cookie:\x20JSESSIONID=node0v6ybx7taxfsvvwz81epydzy345\.
SF:node0;\x20Path=/;\x20HttpOnly\r\nExpires:\x20Thu,\x2001\x20Jan\x201970\
SF:x2000:00:00\x20GMT\r\nContent-Type:\x20text/html;charset=utf-8\r\nAllow
SF::\x20GET,HEAD,POST,OPTIONS\r\nContent-Length:\x200\r\n\r\n")%r(RTSPRequ
SF:est,AD,"HTTP/1\.1\x20505\x20Unknown\x20Version\r\nContent-Type:\x20text
SF:/html;charset=iso-8859-1\r\nContent-Length:\x2058\r\nConnection:\x20clo
SF:se\r\n\r\n<h1>Bad\x20Message\x20505</h1><pre>reason:\x20Unknown\x20Vers
SF:ion</pre>")%r(FourOhFourRequest,F6,"HTTP/1\.1\x20401\x20Unauthorized\r\
SF:nDate:\x20Thu,\x2014\x20Oct\x202021\x2014:19:43\x20GMT\r\nSet-Cookie:\x
SF:20JSESSIONID=node01ne18ri96sxkb10t7lq8h0xm9b46\.node0;\x20Path=/;\x20Ht
SF:tpOnly\r\nExpires:\x20Thu,\x2001\x20Jan\x201970\x2000:00:00\x20GMT\r\nC
SF:ontent-Type:\x20text/html;charset=utf-8\r\nContent-Length:\x200\r\n\r\n
SF:")%r(Socks5,C3,"HTTP/1\.1\x20400\x20Illegal\x20character\x20CNTL=0x5\r\
SF:nContent-Type:\x20text/html;charset=iso-8859-1\r\nContent-Length:\x2069
SF:\r\nConnection:\x20close\r\n\r\n<h1>Bad\x20Message\x20400</h1><pre>reas
SF:on:\x20Illegal\x20character\x20CNTL=0x5</pre>")%r(Socks4,C3,"HTTP/1\.1\
SF:x20400\x20Illegal\x20character\x20CNTL=0x4\r\nContent-Type:\x20text/htm
SF:l;charset=iso-8859-1\r\nContent-Length:\x2069\r\nConnection:\x20close\r
SF:\n\r\n<h1>Bad\x20Message\x20400</h1><pre>reason:\x20Illegal\x20characte
SF:r\x20CNTL=0x4</pre>")%r(RPCCheck,C7,"HTTP/1\.1\x20400\x20Illegal\x20cha
SF:racter\x20OTEXT=0x80\r\nContent-Type:\x20text/html;charset=iso-8859-1\r
SF:\nContent-Length:\x2071\r\nConnection:\x20close\r\n\r\n<h1>Bad\x20Messa
SF:ge\x20400</h1><pre>reason:\x20Illegal\x20character\x20OTEXT=0x80</pre>"
SF:);
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel


go to port 8080 http page, create an account and look for commits concerning tomcat
username="tomcat" password="42MrHBf*z8{Z%"

go back to the https page, dirbuster it and find /manager/status. The page requires connection, use the creds you found.
-> Tomcat Server status page

status/..;/

msfvenom java/shell/reverse_tcp or java/meterpreter/reverse_tcp (neither worked for the moment, try again after reloading the machine)

exploit 47892
