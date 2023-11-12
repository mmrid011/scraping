import requests
import json
from bs4 import BeautifulSoup
import re

def parsingHtmlJson(html_content):
    soup = BeautifulSoup(html_content, 'html.parser').find("script", string=re.compile(r'window._dida_config_ = '))
    # print(soup)
    parsing = soup.string.split('window._dida_config_._init_data_')[1].replace("data: {", '"data" : {').replace("window._dida_config_._init_data_=", "").replace("= {","{")
    # with open('output.json', 'w', encoding='utf-8') as file:
    #     json.dump(parsing, file, indent=2, ensure_ascii=False)

    return json.loads(parsing)

def getWholesale():
    url = "https://www.aliexpress.us/w/wholesale-watch.html?g=y&SearchText=watch&shpf_co=US"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text



print(parsingHtmlJson(getWholesale()))
