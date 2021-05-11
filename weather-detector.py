import requests
import json
from PIL import Image, ImageFont, ImageDraw 
from datetime import date

key = "xxxxxxd1ee198f8a28e3fc456d0ffdd2"
position = [300, 430, 555, 690, 825]

india = ["Bengaluru", "Chennai", "Hyderabad", "Vijayawada", "Kadapa"]
us = ["New York", "Chicago", "Washington", "Los Angeles", "San Diego"]
country_list = [india,us]

for country in country_list:
    image = Image.open("image.png")
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype('Inter-Regular.ttf', size=50)
    content = "Weather Detector - Live Status"
    color = 'rgb(255, 255, 255)'
    (x, y) = (55,50)
    draw.text((x, y), content, color, font=font)

    font = ImageFont.truetype('Inter-Regular.ttf', size=30)
    content = date.today().strftime("%A - %B %d, %Y")
    color = 'rgb(255, 255, 255)'
    (x, y) = (55,145)
    draw.text((x, y), content, color, font=font)

    index = 0
    for city in country:
        url = " http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city,key) 
        response = requests.get(url)
        data = json.loads(response.text)

        font = ImageFont.truetype('Inter-Regular.ttf', size=50)
        color = 'rgb(0, 0, 0)'
        (x, y) = (135, position[index])
        draw.text((x, y), city, color, font=font)

        font = ImageFont.truetype('Inter-Regular.ttf', size=50)
        content = str(data['main']['temp']) + "\u00b0"
        color = 'rgb(255, 255, 255)'
        (x, y) = (600, position[index])
        draw.text((x, y), content, color, font=font)

        font = ImageFont.truetype('Inter-Regular.ttf', size=50)
        content = str(data['main']['humidity']) + "%"
        color = 'rgb(255, 255, 255)'
        (x, y) = (810, position[index])
        draw.text((x, y), content, color, font=font)

        index += 1
        
    image.save(str(date.today()) + country[0] + ".png")
    image_pdf = image.convert('RGB')
    image_pdf.save(str(date.today()) + country[0] + ".pdf")
