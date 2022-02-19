# Weather Report
    # Raspberry Pi Project, featuring a Inky wHAT e-ink display.
    # The Weather Report is meant to display the weather in a more visually pleasing layout,
    # which will combine assets such as hourly readings, date and time, and whatever comes along.
    
    # The idea is to create a UI that resembles something like a dashboard that you'd see on TV or in a car.

#TO DO:
# - API key from Weather Underground to get weather info.
# - Output current temperature of home location onto Inky wHAT.

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = OWM("c7f275b2d16f8329784620d02222e9ee")
mgr = owm.weather_manager()

one_call = mgr.one_call(lat=39.77317, lon=-75.051277)
# Here put your city and Country ISO 3166 country codes
one_call.forecast_daily[0].temperature('fahrenheit').get('feels_like_morn', None)

print(one_call.forecast_daily)
