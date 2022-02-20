#TO DO:
# - API key from Weather Underground to get weather info.
# - Output current temperature of home location onto Inky wHAT.

#Inky Libraries
from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw

# pyOWM Libraries
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = OWM("c7f275b2d16f8329784620d02222e9ee")
mgr = owm.weather_manager()

one_call = mgr.one_call(lat=39.77317, lon=-75.051277)
# Here put your city and Country ISO 3166 country codes
one_call.forecast_daily[0].temperature('fahrenheit').get('feels_like_morn', None)

img = Image.new("P", (inky_display.WIDTH, inky.display.HEIGHT))
draw = ImageDraw.Draw(img)

font = ImageFont.truetype(FredokaOne, 24)

message = "Current Temp: 26 F"
w, h = font.getsize(message)
x = (inky,display.WIDTH / 2) - (w / 2)
y = (inky,display.HEIGHT / 2) - (w / 2)

#print(one_call.forecast_daily)

draw.text((x, y), message, inky_display.YELLOW, font)
inky_display.set_image(img)
inky_display.show()