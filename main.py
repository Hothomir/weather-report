
#TO DO:
# - Weather icons for weather conditions
# - Display location, precipitation
import os, sys
from datetime import datetime, timedelta

#Inky Libraries
from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw

# pyOWM Libraries
from pyowm.owm import OWM
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

TimeDate = datetime.now()
TwoHrsTime = (datetime.now()+timedelta(hours=2)).strftime("%H:00")
FourHrsTime = (datetime.now()+timedelta(hours=4)).strftime("%H:00")
SixHrsTime = (datetime.now()+timedelta(hours=6)).strftime("%H:00")
EightHrsTime = (datetime.now()+timedelta(hours=8)).strftime("%H:00")

degreeSign = u"\N{DEGREE SIGN}"

#OpenWeatherMap Integration
owm = OWM("c7f275b2d16f8329784620d02222e9ee")
mgr = owm.weather_manager()
weather = mgr.weather_at_place("Turnersville,US").weather
one_call = mgr.one_call(lat=39.7729, lon=-75.0519)

getTemp = weather.temperature("fahrenheit") #enables temp in fahrenheit
curTemp = int(getTemp["temp"]) #get current temp

#current high and low temps
hiTemp = int(getTemp["temp_max"])
loTemp = int(getTemp["temp_min"])

#Current wind speeds
getWind = weather.wind(unit="miles_hour")
curWind = int(getWind["speed"])

inky_display = InkyWHAT("yellow")
inky_display.set_border(inky_display.WHITE)

img = Image.open("/home/pi/weather-report/resources/background/weather-report-bg.png")
draw = ImageDraw.Draw(img)

font = ImageFont.truetype(PIXEL_FONT, 12)
font_tiny = ImageFont.truetype(VG5000_FONT, 12)
font_small = ImageFont.truetype(VG5000_FONT, 17)
font_medium = ImageFont.truetype(VG5000_FONT, 32)
font_big = ImageFont.truetype(VG5000_FONT, 64)
font2 = ImageFont.truetype(VG5000_FONT, 10)

currentTemp = str(curTemp)+degreeSign

currentHiTemp = "H: "+str(hiTemp)+degreeSign #current temp max
currentLoTemp ="L: "+str(loTemp)+degreeSign #current temp min

TwoHrTemp = str(int(one_call.forecast_hourly[2].temperature("fahrenheit").get("temp", 0))) #get temp in 2 hrs
TwoHrCond = str(one_call.forecast_hourly[2].status)
FourHrTemp = str(int(one_call.forecast_hourly[4].temperature("fahrenheit").get("temp", 0))) #get temp in 4 hrs
FourHrCond = str(one_call.forecast_hourly[4].status)
SixHrTemp = str(int(one_call.forecast_hourly[6].temperature("fahrenheit").get("temp", 0))) #get temp in 6 hrs
SixHrCond = str(one_call.forecast_hourly[6].status)
EightHrTemp = str(int(one_call.forecast_hourly[8].temperature("fahrenheit").get("temp", 0))) #get temp in 8 hrs
EightHrCond = str(one_call.forecast_hourly[8].status)

currentCond = str(weather.detailed_status)

currentHumidity = "HUMIDITY: "+str(one_call.current.humidity)+"%"
currentWind = "WIND: "+str(curWind)+"MPH"

#draw data and text onto display
draw.text((5, 4),TimeDate.strftime("%m-%d-%Y"), inky_display.WHITE, font2)	#Time
draw.text((368, 4),TimeDate.strftime("%H:%M"), inky_display.WHITE, font2)	#Date
draw.text((155, 4),"WEATHER REPORT", inky_display.WHITE, font2)			#project name

draw.text((150, 60), currentTemp, inky_display.BLACK, font_big)			#Current temp
draw.text((155, 140), currentHiTemp, inky_display.BLACK, font)			#Current high temp
draw.text((155, 155), currentLoTemp, inky_display.BLACK, font)			#Current low temp

draw.text((15, 245), TwoHrTemp+degreeSign, inky_display.BLACK, font_medium)	#Temp in 2 hrs
draw.text((120, 245),FourHrTemp+degreeSign, inky_display.BLACK, font_medium)	#Temp in 4 hrs
draw.text((230, 245), SixHrTemp+degreeSign, inky_display.BLACK, font_medium)	#Temp in 6 hrs
draw.text((330, 245), EightHrTemp+degreeSign, inky_display.BLACK, font_medium)	#Temp in 8 hrs

draw.text((16, 280), TwoHrCond, inky_display.BLACK, font_tiny)			#Condition in 2 hrs
draw.text((126, 280), FourHrCond, inky_display.BLACK, font_tiny)		#Condition in 4 hrs
draw.text((236, 280), SixHrCond, inky_display.BLACK, font_tiny)			#Condition in 6 hrs
draw.text((336, 280), EightHrCond, inky_display.BLACK, font_tiny)		#Condition in 8 hrs

draw.text((16, 236), TwoHrsTime, inky_display.BLACK, font_tiny)			#Time in 2 hrs
draw.text((126, 236), FourHrsTime, inky_display.BLACK, font_tiny)		#Time in 4 hrs
draw.text((236, 236), SixHrsTime, inky_display.BLACK, font_tiny)		#Time in 6 hrs
draw.text((336, 236), EightHrsTime, inky_display.BLACK, font_tiny)		#Time in 8 hrs

draw.text((280, 100), currentHumidity, inky_display.BLACK, font_small)		#Current humidity in percentage
draw.text((280, 120), currentWind, inky_display.BLACK, font_small)		#Current wind speed in MPH

draw.text((5, 200), currentCond, inky_display.BLACK, font_small)		#Current weather conditions, short

inky_display.set_image(img)
inky_display.show()
