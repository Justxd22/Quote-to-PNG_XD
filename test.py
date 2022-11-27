import json, requests, random
from gquote import gquote
from urllib.request import urlretrieve

token = "1FSlwhgUOg_ZRw21PJ9qOmL0aqukh8a8eyHm86vBdP"
colls = [3672442, 214, 474028, 381380, 3333421, 932210, 11649432, 1599413, 1041983, 220381, 1410320, 540518, 17098, 467163, 443273]
base = f"https://api.unsplash.com/photos/random?collections={random.choice(colls)}&h=1080&w=1350&client_id={token}&content_filter=high"

r = requests.get(base)
r = json.loads(r.text)

url = r['urls']['raw']+"&q=100&fit=crop&w=1080&h=1350"
color = r['color']

print(url, color)

p = gquote(background=urlretrieve(url)[0], color=color).run()

# testing script .U
