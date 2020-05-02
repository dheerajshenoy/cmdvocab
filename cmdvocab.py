#!/usr/bin/env python3

import sys,getopt
import urllib 
import requests
import http
import header as imp 
from bs4 import BeautifulSoup
import os 
from os import system 
from os import path

VERBOSE = 0

HELP_MENU = "\nUSAGE:\n cmdvocab.py -W word [OPTIONS] - OPTIONS can have these value:\n -h, --help \t---> this help list\n -W, --word \t---> Word whose meaning is desired\n -v, --verbose \t---> verbose\n -s, --save \t---> save file location with name\n -a, --audio \t---> pronunciation audio \n -wotd \t\t---> Word of the day\n\ne.g:\ncmdvocab.py -v -W hello -a ;\n\nThis statement provides meaning of the word HELLO and also as the argument -a is provided it produces the pronunciation\nNOTE:(-v) or (--verbose) argument must be included before the (-W) word argument or even the (-wotd) word of the day"

def have_internet():
    conn = http.client.HTTPConnection("www.google.com", timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False
    
def main(argv):
    options = "-h -W: -w -s: -a -v"
    long_options = ["help","word=","wotd","save=","audio","verbose"]
    try :
        opts, args = getopt.getopt(argv,options,long_options)
        for opt,arg in opts:
            if opt in ("-h","--help"):
                print(HELP_MENU)
            
            elif opt in ("--wotd"):
                url = "https://www.dictionary.com/e/word-of-the-day/"
                if(have_internet()):
                    respond = requests.get(url)
                    if(respond.status_code == 200):
                        soup = BeautifulSoup(respond.text,"html.parser")
                        wotd_date = soup.find(class_="wotd-item-headword__date")
                        wotd = soup.find(class_="wotd-item-headword__word")
                        wotd_meaning = soup.find('div',class_="wotd-item-headword__pos")
                        DATE = wotd_date.div.text
                        WOTD = wotd.h1.text.strip('\n')
                        for span in wotd_meaning('span'):
                            span.decompose()
                        MEANING = wotd_meaning.text.strip('\n').capitalize()
                        print("\nWORD OF THE DAY: " + WOTD),                        
                        global word
                        word = WOTD
                        print(MEANING),
                    else:
                        input("SERVER error!\nCheck again later")
                else:
                    print("\nNo Internet Connection Detected! Try again later...")
                    exit(1)
                
            elif opt in ("-v","--verbose"):
                global VERBOSE 
                VERBOSE = 1
        
            elif opt in ("-W","--word"):
            
                word = arg
                url = "https://www.dictionary.com/browse/" + word + "?s=t"
                if(have_internet()):
                    respond = requests.get(url)
                    if(respond.status_code == 200):
                        soup = BeautifulSoup(respond.text,"html.parser")
                        s = soup.find(class_="css-1o58fj8 e1hk9ate4")
                        global S 
                        if(VERBOSE):
                            S = s.text
                            print(S)
                        else:
                            S = s.span.text
                            print(S)
                    elif(respond.status_code == 404):
                        print("Check the word again! It's not a valid word")
                else:
                    print("No internet connection deteced!")

            elif opt in ("-a","--audio"):
            
                url = "https://www.dictionary.com/browse/" + word + "?s=t"
                if(have_internet()):
                    respond = requests.get(url)
                    if(respond.status_code == 200):
                        soup = BeautifulSoup(respond.text,"html.parser")
                        k = soup.find(class_="audio-wrapper css-48y3p0 e1rg2mtf7")
                        a = k.source["src"]
                        b = urllib.request.urlopen(a)
                        data = b.read()
                        F = word + ".mp3"
                        with open(F,'wb') as f:
                            f.write(data)
                        print("\nWAITING FOR AUDIO")    
                        system("mpv --no-terminal " + F)
                
                    #if(bool(int(DIR_BOOL)) == False):
                        system("rm " + F)
                #input('\nPress any key to continue....')
            
            
            elif opt in ("-s","--save"):
                with open(arg,'a+') as f:
                    if(f.readlines() == []):
                        f.write(word.capitalize() + ':\n' + S + '\n')
                    else:
                        f.write('\n' + word.capitalize() + '\n' + S)
                    print("\nSuccesfully written to file ->" + arg)
    except getopt.GetoptError:
        print(HELP_MENU)

            
    
if __name__ == "__main__":
    if(len(sys.argv[1:]) == 0):
        print(HELP_MENU)
    else:
        main(sys.argv[1:])
