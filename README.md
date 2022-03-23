# Weather Report 🌡️🌤️

Weather display project, featuring a Inky wHAT e-ink display and a Raspberry Pi.
- The Weather Report is meant to display the weather in a more visually pleasing layout, which will combine assets such as hourly readings, date and time, and whatever comes along.

# Features
Current weather information
- Temperature
- Highs and Lows
- Weather conditions (rainy, sunny, etc.)
- Humidity
- Wind
- Icon depicting weather conditions

Hourly Weather Forecast (Every two hours, total of eight hours ahead)
- Temperature
- Future time of forecast
- One word weather conditions 

# Hardware / Software Used
- Raspberry Pi Zero W (Headers)
- Inky wHAT Display [(Pimoroni Link)](https://shop.pimoroni.com/products/inky-what?variant=21441988558931)
- Micro SD Card (min. 8GB)
- OpenWeatherMaps API
  -   One can get free API licenses by going to [this link](https://openweathermap.org/api)

![PXL_20220321_125707503](https://user-images.githubusercontent.com/10063060/159292479-1cd7e692-8db8-45ff-85c0-00bccddefe3d.jpg)

# Installation
1. Enable I2C and SPI under raspi-config
```
sudo raspi-config
```
2. Get and install git
```
sudo apt update
sudo apt install git
```
3. Install libraries for Inky wHAT display:
```
curl https://get.pimoroni.com/inky | bash
```
4. Install pyOWM. pyOWM is a python library that utilizes the OpenWeatherMaps APIs.
```
pip install pyowm
```
5. Copy the git repo for this project
```
git clone https://github.com/Hothomir/weather-report.git
```
6. Go to the weather-report directory
```
cd weather-report
```
7. Access configfile.ini using nano
```
nano configfile.ini
```
8. Change the values to what is preferred. Example for Philadelphia, PA:
```
[OWM_API]
api = 123456789abcdefg

[Location]
latitude = 39.952583
longitude = -75.165222
city = Philadelphia
country = US
```
9. Run the program while in the weather-report directory
```
python main.py
```
# Recurring Display Refreshes
To get new weather information in timed intervals, I've used crontab. Crontab schedules when to run the main.py file and is flexible with how often it should be run.

I've set up the crontab job to run every 30 minutes, so the display will refresh every 30 minutes. Example:
1. Open crontab in terminal
```
crontab -e
```
2. At the bottom of the crontab file, provide the following line:
```
*/30 * * * * python /home/pi/weather-report/main.py
```
3. To refresh the display every 60 mins (every hour):
```
*/60 * * * * python /home/pi/weather-report/main.py
```

# To-Do
- Where the weather condition prints "Clear" in the image, it would be better to print the detailed condition for the current weather. However, need to see how to wrap text, as the detailed conditions print as one line and get cut off by the edge of the display.

# Resources
pyOWM
https://pyowm.readthedocs.io/en/latest/#

Pimoroni Inky
https://github.com/pimoroni/inky
