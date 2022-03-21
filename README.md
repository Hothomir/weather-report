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

# Hardware Used
- Raspberry Pi Zero W (Headers)
- Inky wHAT Display [(Pimoroni Link)](https://shop.pimoroni.com/products/inky-what?variant=21441988558931)
![weather-report-v1](https://user-images.githubusercontent.com/10063060/158103174-c091a3f5-3b8e-4444-bc4c-e6175d5da4e5.jpg)
- Micro SD Card (min. 8GB)

# Installation
1. Install libraries for Inky wHAT display:
```
curl https://get.pimoroni.com/inky | bash
```
2. Install pyOWM. pyOWM is a python library that utilizes the OpenWeatherMaps APIs.
```
pip install pyowm
```
3. Copy the git repo for this project
```
git clone https://github.com/Hothomir/weather-report.git
```

# To-Do
- The location printed is just a string, would be nice if the lat and lon coordinates grabbed a location to print there instead.
- Where the weather condition prints "Clear" in the image, it would be better to print the detailed condition for the current weather. However, need to see how to wrap text, as the detailed conditions print as one line and get cut off by the edge of the display.
