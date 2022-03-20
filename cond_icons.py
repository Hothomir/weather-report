# Python file for icon library
# To Do:
	# - Create Icons from this list of conditions:
	# - clear sky, few clouds, scattered clouds, broken clouds, shower rain, rain, thunderstorm, snow, mist

	# - Call icons based on what the current condition is.
	# - Have main.py file call cond_icons.py file to draw current condition icon on display.
import os, sys
from datetime import datetime

from PIL import Image, ImageFont, ImageDraw

#pyOWM Libraries
from pyowm.owm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

CurrDir = os.path.dirname(os.path.realpath(__file__)) + "/"
Resources = CurrDir + "resources/"

#OpenWeatherMap Integration
owm = OWM("c7f275b2d16f8329784620d02222e9ee")
mgr = owm.weather_manager()
weather = mgr.weather_at_place("Turnersville,US").weather
one_call = mgr.one_call(lat=39.7729, lon=-75.0519)

#icon directory
FewClouds_ICON = Resources + "icons/few_clouds.png"
FewCloudsIconOutput = Image.open(FewClouds_ICON)

Clouds_ICON = Resources + "icons/clouds.png"
CloudsIconOutput = Image.open(Clouds_ICON)

Sun_ICON = Resources + "icons/sun.png"
SunIconOutput = Image.open(Sun_ICON)

Rain_ICON = Resources + "icons/rain.png"
RainIconOutput = Image.open(Rain_ICON)

Drizzle_ICON = Resources + "icons/light_rain.png"
DrizzleIconOutput = Image.open(Drizzle_ICON)

Thunder_ICON = Resources + "icons/thunder.png"
ThunderIconOutput = Image.open(Thunder_ICON)

Thunderstorm_ICON = Resources + "icons/thunderstorm.png"
ThunderstormIconOutput = Image.open(Thunderstorm_ICON)

Snow_ICON = Resources + "icons/snow.png"
SnowIconOutput = Image.open(Snow_ICON)

CurrCond = str(weather.status).title()
print(CurrCond)
CurrCondDetail = str(weather.status).title()

# When current Condition is given:
# output icon graphic based on condition
def CurrCondIcon():
	if CurrCond == "Clear":
		return SunIconOutput

	elif CurrCond == "Clouds":
			if CurrCondDetail == "Few Clouds":
				return FewCloudsIconOutput
			else:
				return CloudsIconOutput

	elif CurrCond == "Rain":
		return RainIconOutput

	elif CurrCond == "Thunderstorm":
			if CurrCondDetail == "Thunderstorm" or "Heavy Thunderstorm" or "Ragged Thunderstorm":
				return ThunderIconOutput
			else:
				return ThunderstormIconOutput

	elif CurrCond == "Snow":
		return SnowIconOutput 
#SNOW

#MIST/FOG

# else:
# print "N/A"
