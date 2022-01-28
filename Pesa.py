"""
part one!!!!!!!!!!!!!
"""
import numpy as np
import pandas as pd
from requests_html import HTMLSession
sess = HTMLSession()

query = "Dollar"

#user-agent
headers = {

“Accept”: “text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image

apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9″,

“Accept-Encoding”: “gzip, deflate”,

“Accept-Language”: “en-GB,en-US;q=0.9,en;q=0.8”,

“Dnt”: “1”,

“Host”: “httpbin.org”,

“Upgrade-Insecure-Requests”: “1”,

“User-Agent”: “Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36”,}

url = f"https://www.google.com/search?q={query}"

resp = sess.get(url, headers = headers)
dframe = r.html.find('div.VgAgW', first = True).text #div.VgAgW might be dynamic, might change in the future... keeping reviewing
