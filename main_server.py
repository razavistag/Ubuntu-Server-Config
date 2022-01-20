import os
import sys
import time
class bcolors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[31m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    BGRED = '\033[41m'
    WHITE = '\033[37m'

def t():
    current_time = time.localtime()
    ctime = time.strftime('%H:%M:%S', current_time)
    return '[' + ctime + ']'

def s():
    print("           UBUNTU DEVELOPMENT SERVER CONFIGURATION")
    print("           V-0.1")

def update():
    print( t() + bcolors.GREEN + '[processing]' + bcolors.ENDC, end=' '),
    print(  bcolors.GREEN  + ' UPDATING PACKAGES' + bcolors.ENDC),
    print('')

    os.system('sudo apt update');
    print('')
    print( t() + bcolors.GREEN + '[done]' + bcolors.ENDC, end=' '),
    print(bcolors.GREEN + ' Dependency tree builded' + bcolors.ENDC),

def main():
    os.system('clear')
    s()
    update()

    # ----------- ssh config
    print('')
    print( t() + bcolors.GREEN + '[processing]' + bcolors.ENDC, end=' '),
    print(  bcolors.GREEN  + ' Configuring SSH' + bcolors.ENDC),
    os.system('sudo apt update');
    os.system('sudo apt install openssh-server -y');
    os.system('sudo systemctl status ssh');

    # ----------- remoteDesktop config
    print('')
    print( t() + bcolors.GREEN + '[processing]' + bcolors.ENDC, end=' '),
    print(  bcolors.GREEN  + ' Configuring Remote Desktop' + bcolors.ENDC),
    os.system('sudo apt update'); 
    os.system('sudo apt install xrdp -y'); 
    os.system('sudo systemctl status xrdp'); 
    os.system('sudo adduser xrdp ssl-cert'); 
    os.system('sudo systemctl restart xrdp'); 
    os.system('sudo firewall-cmd --zone=public --permanent --add-port=3389/tcp'); 
    os.system('sudo firewall-cmd --reload'); 

    
 

 


    

    




main()
