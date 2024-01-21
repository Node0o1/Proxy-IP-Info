'''
NOTE: This program checks proxies for connectivity and if connected, returns the 
public ip information pertaining to its connection. Use case check for anonimity.
format- <ip:port> <127.0.0.1:1234>
'''
import requests
from multiprocessing import Pool as pThread
import json
import random

TIMEOUT = 20
BROWSER_HEADERS = [
    {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0"},#FireFox
    {"User-Agent":"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10136"},#Edge
    {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36"}, #google chrome
    {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 OPR/76.0.4017.177"}, #opera
]

def get_pub_ip():
    try:
        content=json.loads(requests.get('https://api.myip.com', timeout=TIMEOUT).text)
    except:
        return 'Public IP currently unavailable.'
    else:
        return content['ip']

def check(proxy):
    rand_header = BROWSER_HEADERS[random.randint(0, len(BROWSER_HEADERS)-1 )]
    proxies={'https': proxy}
    try:
        content=requests.get('https://api.myip.com', proxies=proxies, header= rand_header, timeout= TIMEOUT, verify= True)
    except Exception as e:
        None
    else:
        try:
            prox_details=json.loads(content.text)
        except:
            print(f'{chr(0x0a)}Error encountered with {proxy}, skipping.')
        else:
            print(f'{chr(0x0a)}{proxy}{chr(0x0a)}{prox_details}')

def main():
    try:
        in_file=str(input("ENTER PROXY FILE NAME: "))
        print(f'YOUR PUBLIC IP: {get_pub_ip()}')
        with open(in_file, mode='r') as fhandle:
            pThread().map(check,['http://'+ str(x).strip() for x in fhandle.read().split()]) 
    except Exception as e:
        print(f'{type(e).__name__} ERROR :: {e.args}')

if __name__=="__main__":
    main()
