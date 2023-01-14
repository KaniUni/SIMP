import requests
from datetime import datetime
import re
from pprint import pprint
import json


time = int(datetime.now().timestamp())
link = 'https://www.instagram.com/accounts/login/'
login_url = f"https://www.instagram.com/accounts/login/ajax/"

payload = {
    'username': 'username',
    'enc_password': 'PWD_INSTAGRAM_BROWSER:0:{time}:password',
    'queryParams': "{}",
    'optIntoOneTap': 'false',
    'stopDeletionNonce': "", 
    'trustedDeviceRecords': "{}"
}


response = requests.get(link)
csrf = response.cookies['csrftoken']
print(csrf)

response = requests.post(login_url, data=payload, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
    "X-Xequested-Xith": "XMLHttpRequest",
    "Referer": "https://www.instagram.com/",
    "X-CSRFtoken": csrf,
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "www.instagram.com",
    "Origin": "https://www.instagram.com"
})

response_json = json.loads(response.text)
pprint(response_json)
The response I receive after running the above code shows that I request is not authenticated:

{'authenticated': False, 'status': 'ok', 'user': True}

How can I login to Instagram using requests? Is there an updated method?

pythonajaxcookiespython-requestsinstagram
Share
edited Jul 4, 2022 at 16:20
asked Jul 4, 2022 at 15:54
Harsh Sinha's user avatar
Harsh Sinha
3144 bronze badges
2 Answers
Sorted by:

Highest score (default)

1


In general, these use cases lend themselves perfectly for selenium, scrapy, playwright or puppeteer. I do not have an instagram account, so I don't know if this works, but in theory it might return a valid response:

import requests

cookies = {
    'csrftoken': '9e7U8qRNqAbazRC0kwrRgyN2okh1kihx',
    'mid': 'YsM1_AALAAEG2fGCvkPXE5DVlJD0',
    'ig_did': '494394E2-A583-4F01-BC32-5E4344FE2C4D',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'X-CSRFToken': '9e7U8qRNqAbazRC0kwrRgyN2okh1kihx',
    'X-Instagram-AJAX': 'c6412f1b1b7b',
    'X-IG-App-ID': '936619743392459',
    'X-ASBD-ID': '198387',
    'X-IG-WWW-Claim': '0',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://www.instagram.com',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://www.instagram.com/accounts/login/?',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'csrftoken=9e7U8qRNqAbazRC0kwrRgyN2okh1kihx; mid=YsM1_AALAAEG2fGCvkPXE5DVlJD0; ig_did=494394E2-A583-4F01-BC32-5E4344FE2C4D',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

data = {
    'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1656960533:ARxQAMMwb3Yd6w3UdaFGt0Q3mTZ7lMDJHHmZFLaGEfQahXJOTxqb35Q/ZGC3B70DxZRhKcnaf3xImXyL7EFseRF/yZG4dvauui/LzLU7oAHK3rYHSYsjPjQTham/5DFXq6m4foqB5fIiJoChT+ng58EDUkFA1A==',
    'username': 'somerandomemail@hotmail.com',
    'queryParams': '{}',
    'optIntoOneTap': 'false',
    'stopDeletionNonce': '',
    'trustedDeviceRecords': '{}',
}

response = requests.post('https://www.instagram.com/accounts/login/ajax/', cookies=cookies, headers=headers, data=data)