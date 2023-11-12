from bs4 import BeautifulSoup
import re
import json

# Baca file HTML
with open("C:/Users/Miri-Net/Documents/upwork/aliexpress/scraping/dokumen.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Buat objek BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser').find("script", string=re.compile(r'window._dida_config_ = '))
parsing = json.loads(soup.string.split('window._dida_config_._init_data_')[1].replace("window._dida_config_._init_data_ = ", "").replace("};", "}").replace(" = {","{"). replace("data:", '"data" :'))
print(json.dumps(parsing))
with open("kunam.txt" , "w") as w:
    w.write(json.dumps(parsing))