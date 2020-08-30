from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
import requests
import os, sys

def ImageOpenURL(url):
    response = requests.get(url, stream=True).content
    img = Image.open(response)
    return img

def createPassport(Name, Surname, Middlename, Gender, Data_of_Birth, Place_of_Birth, Place_of_residence, Nation, Sexsual_Orientation, Photo=None):
    # Image Open
    shablon = Image.open('passportsr/shablon.jpg')
    shablondraw = ImageDraw.Draw(shablon)
    # Text and Font
    font = ImageFont.truetype("passportsr/19539.ttf", 100)
    #Text
    shablondraw.text((1100, 1290), Name, (0, 0, 0), font=font)
    shablondraw.text((1100, 1390), Surname, (0, 0, 0), font=font)
    shablondraw.text((1100, 1490), Middlename, (0, 0, 0), font=font)
    shablondraw.text((1100, 1590), Gender, (0, 0, 0), font=font)
    shablondraw.text((1100, 1690), Data_of_Birth, (0, 0, 0), font=font)
    shablondraw.text((1100, 1790), Place_of_Birth, (0, 0, 0), font=font)
    shablondraw.text((1100, 1890), Place_of_residence, (0, 0, 0), font=font)
    shablondraw.text((1100, 1990), Nation, (0, 0, 0), font=font)
    shablondraw.text((1170, 2090), Sexsual_Orientation, (0, 0, 0), font=font)
    # Add Photo
    Photo = ImageOpenURL(Photo)
    Photo = Photo.resize((657, 845))
    shablon.paste(Photo, (120, 1319))
    # Return Image
    shablon.save('passportsr/passport.jpg')
    img = open('passportsr/passport.jpg', 'rb')
    return img
