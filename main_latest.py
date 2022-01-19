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

# ----------- Apache2 config
    print('')
    print( t() + bcolors.GREEN + '[processing]' + bcolors.ENDC, end=' '),
    print(  bcolors.GREEN  + ' Configuring Apache' + bcolors.ENDC),
    os.system('sudo apt install apache2 -y');

# ----------- PHP8 config
    print('')
    print( t() + bcolors.GREEN + '[processing]' + bcolors.ENDC, end=' '),
    print(  bcolors.GREEN  + ' Configuring PHP8' + bcolors.ENDC),
    os.system('sudo apt install software-properties-common');
    os.system('sudo add-apt-repository ppa:ondrej/php -y');
    os.system('sudo apt update');
    os.system('sudo apt install php8.0 libapache2-mod-php8.0 -y');
    os.system('sudo systemctl restart apache2');
    os.system('sudo apt update');
    os.system('sudo apt install php8.0-fpm libapache2-mod-fcgid -y');
    os.system('sudo a2enmod proxy_fcgi setenvif');
    os.system('sudo a2enconf php8.0-fpm');
    os.system('systemctl restart apache2');
    os.system('sudo apt install php libapache2-mod-php php-mbstring php-xmlrpc php-soap php-gd php-xml php-cli php-zip php-bcmath php-tokenizer php-json php-pear -y');

# ----------- NODEJS config
    print('')
    print( t() + bcolors.GREEN + '[processing]' + bcolors.ENDC, end=' '),
    print(  bcolors.GREEN  + ' Configuring NODEJS' + bcolors.ENDC),
    os.system('sudo apt install nodejs -y');
    os.system('sudo apt install npm -y');
    os.system('sudo npm install -g n -y');
    os.system('sudo n stable -y');
    os.system('node -v');
    os.system('npm -v');

# ----------- mysql8 config
    print('')
    print( t() + bcolors.GREEN + '[processing]' + bcolors.ENDC, end=' '),
    print(  bcolors.GREEN  + ' Configuring MSYQL8' + bcolors.ENDC),
    os.system('sudo apt update');
    os.system('sudo apt install mysql-server -y');
    os.system('sudo mysql_secure_installation');
    print(  bcolors.GREEN  + '''
    .. VALIDATE PASSWORD COMPONENT -- y
	.. password validation policy -- 2
	.. set password
	.. Estimated strength of the password -- y
	.. Remove anonymous users -- y
	.. Disallow root login remotely -- n
	.. Remove test database and access to it -- y
	.. Reload privilege tables -- y
    ''' + bcolors.ENDC),
    print('')
    os.system('mysql -V');

# ----------- composer config
    print('')
    print( t() + bcolors.GREEN + '[processing]' + bcolors.ENDC, end=' '),
    print(  bcolors.GREEN  + ' Configuring Composer' + bcolors.ENDC),
    os.system('sudo apt update');
    os.system('sudo apt install curl unzip -y');
    os.system('sudo apt install php php-curl -y');
    os.system('sudo apt install composer');



main()
