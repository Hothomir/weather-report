#TO DO: - API key from Weather Underground to get weather info.
# - Output current temperature of home location onto Inky wHAT.
# - Display location, humidity, wind, precipitation
# - Future weather at bottom of display, showing 2 hour periods

import os, sys
import datetime

#Inky Libraries
from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw

# pyOWM Libraries
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

CURR_DIR = os.path.dirname(os.path.realpath(__file__)) + "/"
RESOURCES = CURR_DIR + "resources/"

# Fonts
PIXEL_FONT = RESOURCES + "fonts/Pixel12x10.ttf"
Terminal_FONT = RESOURCES + "fonts/terminal-grotesque.ttf"
Mister_Pixel_FONT = RESOURCES + "fonts/Mister_Pixel_Regular.otf"
B_FONT = RESOURCES + "fonts/04B_03.ttf"
VG5000_FONT = RESOURCES + "fonts/VG5000-Regular.otf"


TimeDate = datetime.datetime.now()
degreeSign = u'\N{DEGREE SIGN}'

#OpenWeatherMap Integration
owm = OWM("c7f275b2d16f8329784620d02222e9ee")
mgr = owm.weather_manager()
weather = mgr.weather_at_place("Turnersville,US").weather

getTemp = weather.temperature('fahrenheit')
avgTemp = int(getTemp["temp"]) #get current temp

hiTemp = int(getTemp["temp_max"])
loTemp = int(getTemp["temp_min"])

one_call = mgr.one_call(lat=39.7729, lon=75.0519)

one_call.current.humidity #get current humidity

inky_display = InkyWHAT("yellow")
inky_display.set_border(inky_display.WHITE)

img = Image.open("/home/pi/weather-report/resources/background/weather-report-bg.png")
draw = ImageDraw.Draw(img)

font = ImageFont.truetype(PIXEL_FONT, 10)
font_medium = ImageFont.truetype(VG5000_FONT, 17)
font_big = ImageFont.truetype(VG5000_FONT, 64)
font2 = ImageFont.truetype(VG5000_FONT, 10)

currentTemp = str(avgTemp)+degreeSign

currentHiTemp = "MAX: "+str(hiTemp)+degreeSign #current temp max
currentLoTemp ="MIN: "+str(loTemp)+degreeSign #current temp min

currentHumidity = "HUMIDITY: "+str(one_call.current.humidity)+"%"
currentWind = "WIND: N/A"

w, h = font.getsize(currentTemp)
#x = (inky_display.WIDTH / 2) - (w / 2)
#y = (inky_display.HEIGHT / 2) - (w / 2)

#draw data and text onto display
draw.text((5, 3),TimeDate.strftime("%m-%d-%Y"), inky_display.WHITE, font2) #Time
draw.text((370, 3),TimeDate.strftime("%H:%M"), inky_display.WHITE, font2) #Date

draw.text((20, 60), currentTemp, inky_display.BLACK, font_big)
draw.text((20, 130), currentHiTemp, inky_display.BLACK, font)
draw.text((20, 140), currentLoTemp, inky_display.BLACK, font)
 
draw.text((200, 100), currentHumidity, inky_display.BLACK, font_medium)
draw.text((200,120), currentWind, inky_display.BLACK, font_medium)


inky_display.set_image(img)
inky_display.show()
