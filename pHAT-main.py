
# WEATHER DISPLAY - Bartosz Jaskulski
#
#
# --- PLEASE READ ---
# This script is for Pimoroni Inky *pHAT* Displays ONLY
# Please use impression-main.py if you have an Inky Impression
# Please use mainpy if you have an Inky wHAT
# --- PLEASE READ ---
#
#

import os, sys
from datetime import datetime, timedelta
import cond_icons

import configparser

#config.ini file
configObj = configparser.ConfigParser()
configObj.read("/home/pi/weather-report/configfile.ini")
OWMAPI = configObj["OWM_API"]
UserLoc = configObj["Location"]

api = OWMAPI["api"]

lat =float(UserLoc["latitude"])
lon = float(UserLoc["longitude"])
city = str(UserLoc["city"])
country = str(UserLoc["country"])

#Inky Libraries
from inky import InkyPHAT
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
FT88Reg_FONT = RESOURCES + "fonts/FT88-Regular.otf"
 
TimeDate = datetime.now()
TwoHrsTime = (datetime.now()+timedelta(hours=2)).strftime("%H:00")
FourHrsTime = (datetime.now()+timedelta(hours=4)).strftime("%H:00")
SixHrsTime = (datetime.now()+timedelta(hours=6)).strftime("%H:00")
EightHrsTime = (datetime.now()+timedelta(hours=8)).strftime("%H:00")

degreeSign = u"\N{DEGREE SIGN}"

#OpenWeatherMap Integration
owm = OWM(api)
mgr = owm.weather_manager()
weather = mgr.weather_at_place(city+","+country).weather
one_call = mgr.one_call(lat, lon)

getTemp = weather.temperature("fahrenheit") #enables temp in fahrenheit
curTemp = int(getTemp["temp"]) #get current temp

#Current "feels like" Temperature
feelsLike = int(getTemp["feels_like"])
currentFeelsLike = "Feels: "+str(feelsLike)+degreeSign

#current max and min temps
maxTemp = int(getTemp["temp_max"])
minTemp = int(getTemp["temp_min"])

#Current wind speeds
getWind = weather.wind(unit="miles_hour")
curWind = int(getWind["speed"])

inky_display = InkyPHAT("yellow")
inky_display.set_border(inky_display.WHITE)

Location_ICON = RESOURCES + "icons/location.png"
LocationIcon = Image.open(Location_ICON)

img = Image.open("/home/pi/weather-report/resources/background/weather-report-bg-phat.png")
draw = ImageDraw.Draw(img)

font_tiny = ImageFont.truetype(FT88Reg_FONT, 12)
font_small = ImageFont.truetype(FT88Reg_FONT, 12)
font_medium = ImageFont.truetype(VG5000_FONT, 32)
font_medium2 = ImageFont.truetype(FT88Reg_FONT, 18)
font_big = ImageFont.truetype(VG5000_FONT, 70)
font2 = ImageFont.truetype(VG5000_FONT, 10)

currentTemp = str(curTemp)+degreeSign

currentMaxTemp = "Max: "+str(maxTemp)+degreeSign #current temp max
currentMinTemp = "Min: "+str(minTemp)+degreeSign #current temp min

TwoHrTemp = str(int(one_call.forecast_hourly[2].temperature("fahrenheit").get("temp", 0))) #get temp in 2 hrs
TwoHrCond = str(one_call.forecast_hourly[2].status)
FourHrTemp = str(int(one_call.forecast_hourly[4].temperature("fahrenheit").get("temp", 0))) #get temp in 4 hrs
FourHrCond = str(one_call.forecast_hourly[4].status)
SixHrTemp = str(int(one_call.forecast_hourly[6].temperature("fahrenheit").get("temp", 0))) #get temp in 6 hrs
SixHrCond = str(one_call.forecast_hourly[6].status)
EightHrTemp = str(int(one_call.forecast_hourly[8].temperature("fahrenheit").get("temp", 0))) #get temp in 8 hrs
EightHrCond = str(one_call.forecast_hourly[8].status)

currentCond = str(weather.status)
currentDetailCond = str(weather.detailed_status).title()

currentHumidity = "Hum:"+str(one_call.current.humidity)+"%"
currentWind = "Wind:"+str(curWind)+" MPH"
currentLoc = ": " + city

#proper text placement

w_TwoHrTemp, h_TwoHrTemp = font_medium.getsize(TwoHrTemp)
x_TwoHrTemp = (50) - (w_TwoHrTemp/2)
w_TwoHrsTime, h_TwoHrsTime = font_tiny.getsize(TwoHrsTime)
x_TwoHrsTime = 50 - (w_TwoHrsTime/2)
w_TwoHrCond, h_TwoHrCond = font_tiny.getsize(TwoHrCond)
x_TwoHrCond = 50 - (w_TwoHrCond/2)

w_FourHrTemp, h_FourHrTemp = font_medium.getsize(FourHrTemp)
x_FourHrTemp = (150) - (w_FourHrTemp/2)
w_FourHrsTime, h_FourHrsTime = font_tiny.getsize(FourHrsTime)
x_FourHrsTime = 150 - (w_FourHrsTime/2)
w_FourHrCond, h_FourHrCond = font_tiny.getsize(FourHrCond)
x_FourHrCond = 150 - (w_FourHrCond/2)

w_SixHrTemp, h_SixHrTemp = font_medium.getsize(SixHrTemp)
x_SixHrTemp = (250) - (w_SixHrTemp/2)
w_SixHrsTime, h_SixHrsTime = font_tiny.getsize(SixHrsTime)
x_SixHrsTime = 250 - (w_SixHrsTime/2)
w_SixHrCond, h_SixHrCond = font_tiny.getsize(SixHrCond)
x_SixHrCond = 250 - (w_SixHrCond/2)

w_EightHrTemp, h_EightHrTemp = font_medium.getsize(EightHrTemp)
x_EightHrTemp = (350) - (w_EightHrTemp/2)
w_EightHrsTime, h_EightHrsTime = font_tiny.getsize(EightHrsTime)
x_EightHrsTime = 350 - (w_EightHrsTime/2)
w_EightHrCond, h_EightHrCond = font_tiny.getsize(EightHrCond)
x_EightHrCond = 350 - (w_EightHrCond/2)

#draw data and text onto display

#draw.text((155, 65), currentTemp, inky_display.BLACK, font_big)				#Current temp
 
draw.text((x_TwoHrTemp, 246), TwoHrTemp+degreeSign, inky_display.BLACK, font_medium)		#Temp in 2 hrs
draw.text((x_FourHrTemp, 246),FourHrTemp+degreeSign, inky_display.BLACK, font_medium)		#Temp in 4 hrs
draw.text((x_SixHrTemp, 246), SixHrTemp+degreeSign, inky_display.BLACK, font_medium)		#Temp in 6 hrs
draw.text((x_EightHrTemp, 246), EightHrTemp+degreeSign, inky_display.BLACK, font_medium)	#Temp in 8 hrs

draw.text((x_TwoHrsTime, 239), TwoHrsTime, inky_display.BLACK, font_tiny)			#Time in 2 hrs
draw.text((x_FourHrsTime, 239), FourHrsTime, inky_display.BLACK, font_tiny)			#Time in 4 hrs
draw.text((x_SixHrsTime, 239), SixHrsTime, inky_display.BLACK, font_tiny)			#Time in 6 hrs
draw.text((x_EightHrsTime, 239), EightHrsTime, inky_display.BLACK, font_tiny)			#Time in 8 hrs

#draw.text((10, 190), currentDetailCond, inky_display.BLACK, font_medium2)		#Current weather conditions, detailed
#img.paste(cond_icons.CurrCondIcon(), (15, 60))                                  #Current Weather Icon

inky_display.set_image(img)
inky_display.show()
