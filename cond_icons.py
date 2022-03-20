# Python file for icon library
# To Do:
	# - Create Icons from this list of conditions:
	# - clear sky, few clouds, scattered clouds, broken clouds, shower rain, rain, thunderstorm, snow, mist

	# - Call icons based on what the current condition is.
	# - Have main.py file call cond_icons.py file to draw current condition icon on display.
import os, sys
from datetime import datetime

#Inky Libraries
from inky import InkyWHAT
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
CurrCond = str(weather.status).title()
CurrCondDetail = str(weather.status).title()

ClearSun_ICON = Resources +"icons/sun.png"
ClearSunIconOutput = Image.open(ClearSun_ICON)

ClearMoon_ICON = Resources +"icons/moon.png"
ClearMoonIconOutput = Image.open(ClearMoon_ICON)

FewCloudsSun_ICON = Resources + "icons/few_clouds_sun.png"
FewCloudsSunIconOutput = Image.open(FewCloudsSun_ICON)

FewCloudsMoon_ICON = Resources + "icons/few_clouds_moon.png"
FewCloudsMoonIconOutput = Image.open(FewCloudsMoon_ICON)

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

Fog_ICON = Resources + "icons/fog.png"
FogIconOutput = Image.open(Fog_ICON)

def CurrCondIcon():
	if CurrCond == "Clear":
		if   CurrTime > "19:00" and CurrTime < "07:00":
			return ClearMoonIconOutput
		else:
			return ClearSunIconOutput

	elif CurrCondDetail == "Scattered Clouds" or "Broken Clouds" or "Overcast Clouds":
		return CloudsIconOutput

	elif CurrCondDetail == "Few Clouds":
		return FewCloudsSunIconOutput

	elif CurrCond == "Rain":
		return RainIconOutput

	elif CurrCond == "Thunderstorm":
		if CurrCondDetail == "Thunderstorm" or "Heavy Thunderstorm" or "Ragged Thunderstorm":
			return ThunderIconOutput
		else:
			return ThunderstormIconOutput

	elif CurrCond == "Snow":
		return SnowIconOutput 

	elif CurrCond == "Mist" or "Smoke" or "Haze" or "Dust" or "Fog" or "Sand" or "Dust" or "Ash" or "Squall" or "Tornado":
		return FogIconOutput
