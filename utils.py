import requests
import json
import random
from globals import BROWSER_HEADERS, TIMEOUT

def get_pub_ip() -> str:
    try: content=json.loads(requests.get('https://api.myip.com', timeout=TIMEOUT).text)
    except: return 'Public IP currently unavailable.'
    else: return content['ip']

def check(proxy):
    rand_header = BROWSER_HEADERS[random.randint(0, len(BROWSER_HEADERS)-1 )]
    proxies={'https': proxy}
    try: content=requests.get('https://api.myip.com', proxies=proxies,headers=rand_header, timeout= TIMEOUT, verify= True)
    except: None
    else:
        try: prox_details=json.loads(content.text)
        except: print(f'{chr(0x0a)}Error encountered with details for {proxy}. Skipping.')
        else: print(f'{chr(0x0a)}{proxy}{chr(0x0a)}{prox_details}')
