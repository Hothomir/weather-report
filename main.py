#TO DO: - API key from Weather Underground to get weather info. - Output current temperature of home location onto Inky wHAT.

import os, sys

#Inky Libraries
from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw

# pyOWM Libraries
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

CURR_DIR = os.path.dirname(os.path.realpath(__file__)) + "/"
RESOURCES = CURR_DIR + "resources/"
PIXEL_FONT = RESOURCES + "fonts/Pixel12x10.ttf"

owm = OWM("c7f275b2d16f8329784620d02222e9ee")
mgr = owm.weather_manager()
weather = mgr.weather_at_place("Turnersville,US").weather

getTemp = weather.temperature('fahrenheit')
avgTemp =int(getTemp["temp"])

inky_display = InkyWHAT("yellow")
inky_display.set_border(inky_display.WHITE)

img = Image.open("/home/pi/weather-report/resources/background/test.png")
draw = ImageDraw.Draw(img)

font = ImageFont.truetype(PIXEL_FONT, 18)

message = "Current REAL Temp: "+str(avgTemp)+"F"
w, h = font.getsize(message)
#x = (inky_display.WIDTH / 2) - (w / 2)
#y = (inky_display.HEIGHT / 2) - (w / 2)

print("Current REAL Temp: "+str(avgTemp)+"F")

draw.text((20, 60), message, inky_display.YELLOW, font)

inky_display.set_image(img)
inky_display.show()
