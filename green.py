import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from mahadi import MahadiNX
 
        MahadiNX()
 
 
 
elif bit == "32bit":
 
        from FL32 import MahadiNX
 
 
        MahadiNX()
