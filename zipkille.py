from threading import Thread 
import time 
import os
try:
	from colorama import Fore
except:
	 
	os.system("pip install colorama -y") 
	os.system("clear") 
	
	
from zipfile import ZipFile
from datetime import datetime

os.system("clear") 
print(Fore.CYAN+"""
  .S    S.    .S_SSSs     .S_SsS_S.    .S   .S_sSSs     .S_SSSs    
.SS    SS.  .SS~SSSSS   .SS~S*S~SS.  .SS  .SS~YS%%b   .SS~SSSSS   
S%S    S&S  S%S   SSSS  S%S `Y' S%S  S%S  S%S   `S%b  S%S   SSSS  
S%S    d*S  S%S    S%S  S%S     S%S  S%S  S%S    S%S  S%S    S%S  
S&S   .S*S  S%S SSSS%S  S%S     S%S  S&S  S%S    d*S  S%S SSSS%S  
S&S_sdSSS   S&S  SSS%S  S&S     S&S  S&S  S&S   .S*S  S&S  SSS%S  
S&S~YSSY%b  S&S    S&S  S&S     S&S  S&S  S&S_sdSSS   S&S    S&S  
S&S    `S%  S&S    S&S  S&S     S&S  S&S  S&S~YSY%b   S&S    S&S  
S*S     S%  S*S    S&S  S*S     S*S  S*S  S*S   `S%b  S*S    S&S  
S*S     S&  S*S    S*S  S*S     S*S  S*S  S*S    S%S  S*S    S*S  
S*S     S&  S*S    S*S  S*S     S*S  S*S  S*S    S&S  S*S    S*S  
S*S     SS  SSS    S*S  SSS     S*S  S*S  S*S    SSS  SSS    S*S  
SP                 SP           SP   SP   SP                 SP   
Y                  Y            Y    Y    Y                  Y    
                                                                                                                                 
""")
time.sleep(5)
os.system("clear")
print(Fore.LIGHTGREEN_EX+"""
        **               **     **  **  **        
       //  ******       /**    //  /** /**        
 ****** **/**///**      /**  ** ** /** /**  ***** 
////** /**/**  /**      /** ** /** /** /** **///**
   **  /**/******       /****  /** /** /**/*******
  **   /**/**///        /**/** /** /** /**/**//// 
 ******/**/**           /**//**/** *** ***//******
////// // //            //  // // /// ///  ////// 
""") 
print("zip kille 1.0")
print("") 
print(Fore.CYAN+"┌─["+Fore.MAGENTA+"enter the zip file") 
zf = input(Fore.CYAN+"└──╼>>"+Fore.YELLOW+"") 
print(Fore.CYAN+"┌─["+Fore.MAGENTA+"enter the password list ")
passlist2 = input(Fore.CYAN+"└──╼ >>"+Fore.YELLOW+" ")
time.sleep(2)
print(Fore.LIGHTGREEN_EX+"KILLE ZIP START") 
def std():
	zf2 = ZipFile(zf)
	tests = 0
	start_time = datetime.now()
	for password in open(passlist2):
	    password = password.strip("\n") 
	    tests += 1
	    try:
	        zf2.extractall(pwd=password.encode())
	        end_time = datetime.now()
	        t = end_time - start_time
	        print("-"*50)
	        print(Fore.LIGHTGREEN_EX+"Password : {}     ||     {} Passwords Tested in {} seconds !".format(password,tests,t.total_seconds()))
	        break
	    except :
	    	continue
	    	
	    	
	    	
	    	
a=Thread(target=std)
a.start()