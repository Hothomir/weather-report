# Python file for icon library
# To Do:
	# - Show moon/sun specific icons for specific times (moon from 19:00-07:00)
import os, sys
from datetime import datetime, time

from PIL import Image, ImageFont, ImageDraw

#pyOWM Libraries
from pyowm.owm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

CurrDir = os.path.dirname(os.path.realpath(__file__)) + "/"
Resources = CurrDir + "resources/"

begin = time(19,0)	#begins at 7:00 PM (19:00)
end = time(7,0)		#ends at 7:00 AM

#OpenWeatherMap Integration
owm = OWM("c7f275b2d16f8329784620d02222e9ee")
mgr = owm.weather_manager()
weather = mgr.weather_at_place("TOWN/CITY, COUNTRY").weather
one_call = mgr.one_call(lat="PROVIDE COORDINATES", lon="PROVIDE COORDINATES")

CurrCond = str(weather.status).title()
CurrCondDetail = str(weather.detailed_status).title()

#icon directory
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

def NightTime(begin, end, currTime=None):
	currTime = currTime or datetime.now().time()
	if begin < end:
		return currTime >= begin and currTime <= end
	else:
		return currTime >= begin or currTime <= end

def CurrCondIcon():
	if CurrCond == "Clear":
		if NightTime == False:
			return ClearSunIconOutput
		else:
			return ClearMoonIconOutput

	if CurrCondDetail == "Few Clouds":
		if NightTime == False:
			return FewCloudsSunIconOutput
		else:
			return FewCloudsMoonIconOutput

	if CurrCondDetail == "Scattered Clouds" or "Broken Clouds" or "Overcast Clouds":
		return CloudsIconOutput

	if CurrCond == "Rain":
		return RainIconOutput

	if CurrCond == "Thunderstorm":
		if CurrCondDetail == "Thunderstorm" or "Heavy Thunderstorm" or "Ragged Thunderstorm":
			return ThunderIconOutput
		else:
			return ThunderstormIconOutput

	if CurrCond == "Snow":
		return SnowIconOutput 

	if CurrCond == "Mist" or "Smoke" or "Haze" or "Dust" or "Fog" or "Sand" or "Dust" or "Ash" or "Squall" or "Tornado":
		return FogIconOutput
