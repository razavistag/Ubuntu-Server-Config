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
    print("           UBUNTU SERVER CONFIGURATION")
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

# -----------------------------------------------------------------------------------
    print('')
    print( t() + bcolors.GREEN + '[processing]' + bcolors.ENDC, end=' '),
    print(  bcolors.GREEN  + ' Configuring Apache' + bcolors.ENDC),

    os.system('sudo apt install apache2 -y');
    print('')
    print( t() + bcolors.GREEN + '[done]' + bcolors.ENDC, end=' '),
    print(bcolors.GREEN + ' apache2 installed' + bcolors.ENDC),
# -----------------------------------------------------------------------------------  
    update()
# -----------------------------------------------------------------------------------
    print('')
    print( t() + bcolors.GREEN + '[processing]' + bcolors.ENDC, end=' '),
    print(  bcolors.GREEN  + ' Installing composer' + bcolors.ENDC),

    os.system('sudo apt install composer -y');
    print('')
    print( t() + bcolors.GREEN + '[done]' + bcolors.ENDC, end=' '),
    print(bcolors.GREEN + ' composer installed' + bcolors.ENDC),
# -----------------------------------------------------------------------------------  
# -----------------------------------------------------------------------------------
    print('')
    print( t() + bcolors.GREEN + '[processing]' + bcolors.ENDC, end=' '),
    print(  bcolors.GREEN  + ' Installing PHP' + bcolors.ENDC),

    os.system('sudo apt install php libapache2-mod-php php-mbstring php-xmlrpc php-soap php-gd php-xml php-cli php-zip php-bcmath php-tokenizer php-json php-pear -y');
    print('')
    print( t() + bcolors.GREEN + '[done]' + bcolors.ENDC, end=' '),
    print(bcolors.GREEN + ' PHP installed' + bcolors.ENDC),
# -----------------------------------------------------------------------------------    
    update()
# -----------------------------------------------------------------------------------
    print('')
    print( t() + bcolors.GREEN + '[processing]' + bcolors.ENDC, end=' '),
    print(  bcolors.GREEN  + ' Installing MYSQL Database ' + bcolors.ENDC),

    os.system('sudo apt install mariadb-server -y');
    print('')
    print( t() + bcolors.GREEN + '[done]' + bcolors.ENDC, end=' '),
    print(bcolors.GREEN + ' MYSQL Database  installed' + bcolors.ENDC),
# -----------------------------------------------------------------------------------  
    update()
    # -----------------------------------------------------------------------------------
    print('')
    print( t() + bcolors.GREEN + '[processing]' + bcolors.ENDC, end=' '),
    print(  bcolors.GREEN  + ' Configuring MYSQL ' + bcolors.ENDC),
    print(  bcolors.GREEN  + '''
    Remove anonymous users? [Y/n] y
    Disallow root login remotely? [Y/n] n
    Remove test database and access to it? [Y/n] y
    Reload privilege tables now? [Y/n] y

    Password should Cantain 8 Char, Captial, Simple letter, Special Char
    ''' + bcolors.ENDC),

    print('')
    os.system('sudo mysql_secure_installation');
    print('')
    print( t() + bcolors.GREEN + '[done]' + bcolors.ENDC, end=' '),
    print(bcolors.GREEN + ' Database Configuration' + bcolors.ENDC),
# -----------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------
    print('')
    print( t() + bcolors.GREEN + '[processing]' + bcolors.ENDC, end=' '),
    print(  bcolors.GREEN  + ' Installing Latest Laravel Framework ' + bcolors.ENDC),

    os.system('sudo composer global require laravel/installer');
    print('')
    print( t() + bcolors.GREEN + '[done]' + bcolors.ENDC, end=' '),
    print(bcolors.GREEN + ' Laravel Installed' + bcolors.ENDC),
# -----------------------------------------------------------------------------------  
    print('')
    print( t() + bcolors.GREEN + '[processing]' + bcolors.ENDC, end=' '),
    print(  bcolors.GREEN  + ' Creating Demo Project ' + bcolors.ENDC),

    os.system('composer create-project laravel/laravel example-demo');
    print('')
    print( t() + bcolors.GREEN + '[done]' + bcolors.ENDC, end=' '),
    print(bcolors.GREEN + ' Laravel Project Installed SuccessFully' + bcolors.ENDC),

    print('')
    print( t() + bcolors.GREEN + '[processing]' + bcolors.ENDC, end=' '),
    print(  bcolors.GREEN  + ' CONFIGURATION COMPLETED ' + bcolors.ENDC),
    print('')
    print(  bcolors.GREEN  + '''
    
    RUN YOUR PROJECT
        cd example-demo
        php artisan serve
    ''' + bcolors.ENDC),  

main()
