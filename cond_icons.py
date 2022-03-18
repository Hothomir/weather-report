# Python file for icon library
# To Do:
	# - Create Icons from this list of conditions:
	# - clear sky, few clouds, scattered clouds, broken clouds, shower rain, rain, thunderstorm, snow, mist

	# - Call icons based on what the current condition is.
	# - Have main.py file call cond_icons.py file to draw current condition icon on display.
import os, sys
from datetime import datetime

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

currentCond = str(weather.status).title()

# When current Condition is given:
# output icon graphic based on condition

# else:
# print "N/A"
