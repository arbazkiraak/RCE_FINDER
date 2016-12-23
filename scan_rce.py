#!/usr/bin/env python
# RCE Finder
# By Rudra Sarkar - twitter.com/rudr4_sarkar
import re
import urllib
from httpheader import *
from rcepayload import *

print ga.green+'''
  _______    ______    _______       _______  __    _____  ___   ________    _______   _______   
 /"      \  /" _  "\  /"     "|     /"     "||" \  (\"   \|"  \ |"      "\  /"     "| /"      \  
|:        |(: ( \___)(: ______)    (: ______)||  | |.\\   \    |(.  ___  :)(: ______)|:        | 
|_____/   ) \/ \      \/    |       \/    |  |:  | |: \.   \\  ||: \   ) || \/    |  |_____/   ) 
 //      /  //  \ _   // ___)_      // ___)  |.  | |.  \    \. |(| (___\ || // ___)_  //      /  
|:  __   \ (:   _) \ (:      "|    (:  (     /\  |\|    \    \ ||:       :)(:      "||:  __   \  
|__|  \___) \_______) \_______)     \__/    (__\_|_)\___|\____\)(________/  \_______)|__|  \___) 
                                                        
                                                    
        ##############################################################
        #|  By Rudra Sarkar - @rudr4_sarkar                          #
        #|  Loaded Modules : 1                                       #
        ##############################################################
        '''+ga.end

def urls_or_list():
	url_or_list = raw_input(" [!] Scan URL or List of URLs? [1/2]: ")
	if url_or_list == "1":
	 	 url = raw_input(" [!] Enter the URL: ")
	 	 
		 if "?" in url:
		 	rce_func(url)
		 else:
			print ga.red +"\n [Warning] "+ ga.end + ga.bold+"%s"%url +ga.end + ga.red +" is not a valid URL"+ga.end			
			print ga.red +" [Warning] You should write a Full URL .e.g http://site.com/page.php?id=value \n"+ ga.end
			exit()
	if url_or_list =="2":
		 urls_list = raw_input( ga.green+" [!] Enter the list file name .e.g [list.txt]: "+ga.end)
		 open_list = open(urls_list).readlines()
		 for line in open_list:
			 if "?" in line:
			 	links = line.strip()
		  	 	url = links
		  	 	print ga.green+" \n [!] Now Scanning %s"%url +ga.end
		  	 	rce_func(url)
			 else:
			 	links = line.strip()
		  	 	url = links
				print ga.red +"\n [Warning] "+ ga.end + ga.bold+"%s"%url +ga.end + ga.red +" is not a valid URL"+ga.end				
				print ga.red +" [Warning] You should write a Full URL .e.g http://site.com/page.php?id=value \n"+ ga.end
		 exit()				

urls_or_list()



