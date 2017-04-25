#!/usr/bin/python3
from blinkt import set_brightness, set_pixel, show, set_all, clear
from datetime import timedelta, datetime as dt
import requests
import time
from random import random
# todo: add a flask route to clear errors. otherwise age out as necessary

def fade_pixel(pix, r, g, b, time_secs, max_brightness=1.0):
	start = dt.now()
	span = timedelta(seconds=time_secs)
	end = start + span
	while dt.now() < end:
		scaled_brightness =  ( 1 - ( ( end - dt.now() ) / span ) ) * max_brightness
		set_pixel(pix, r, g, b, scaled_brightness)
		show()
		# print(scaled_brightness)
		time.sleep(0)
urls = {
	0: "http://voidrunner.m45.space/pebble-weather/fuck-test/39.0437,-77.4875?units=us",
	1: "https://box.spacewalkpublishing.us/",
	2: "https://spacewalkpublishing.us/",
	3: "https://teammaia.us/",
	4: "http://eval.m45.space/evaluationsui/",
	5: "https://pilamacademy.m45.space/",
	#6: "https://wrencheffect.local/",
}
while True:
	t = dt.now()
	clear()
	# set_all(148,0,211)
	if t.hour > 22 or t.hour < 6:
		brightness = 0.04
	else:
		brightness = 0.6
	show()
	set_all(0,0,0)
	for key in urls:
		start = dt.now()
		try:
			result = requests.get(urls[key])
			finish = dt.now()
			if result.status_code != 200:
				set_pixel(key, 255, 0, 0, brightness)
			elif (finish - start).seconds > 5:
				set_pixel(key, 255, 100, 0, brightness)
			else:
				set_pixel(key, 0,0,0, brightness)
			show()
		except Exception:
			set_pixel(key, 255, 69, 0, brightness)
			show()		
	fade_pixel(7,148,0,211,60, brightness)
