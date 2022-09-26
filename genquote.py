from PIL import Image, ImageFont, ImageDraw
from textwrap import wrap as wr
from requests import get
import json

base = "https://zenquotes.io/api/random"
tquote = get(base)

if tquote.status_code != 200:
    print("bad api!")
    exit(1)

tquote = json.loads(tquote.text)
quote  = tquote[0]['q']
author = "~ " + tquote[0]['a'] + " ~"
quote  = "“" + quote + "”"
wquote = wr(quote, width=18)

im   = Image.new("RGB", (1080,1920))
draw = ImageDraw.Draw(im)
font  = ImageFont.truetype("./fonts/Barkentina.ttf", 100)
sfont = ImageFont.truetype("./fonts/Ubuntu-Italic.ttf", 40)

padding = 50
ch = 400

for i in wquote:
    w, h = draw.textsize(i, font=font)
    draw.text( ( (1080-w)/2, ch ), i, font=font)
    ch += h + padding

w, h = draw.textsize(author, font=sfont)
draw.text( ( (1080-w)/2, ch+80), author, font=sfont)

im.save("todayquote.png")

print('saved to todayquote.png')
