#!/usr/bin/python3
from blinkt import set_brightness, set_pixel, show, set_all, clear
from datetime import datetime as dt
import requests
import time
from random import random
# todo: add a flask route to clear errors. otherwise age out as necessary

urls = {
	0: "http://voidrunner.m45.space/pebble-weather/fuck-test/39.0437,-77.4875?units=us",
	1: "https://box.spacewalkpublishing.us/",
	2: "https://spacewalkpublishing.us/",
	3: "https://teammaia.us/",
	4: "http://eval.m45.space/evaluationsui/",	
}
while True:
	t = dt.now()
	clear()
	set_all(148,0,211)
	show()
	if t.hour > 22 or t.hour < 6:
		set_brightness(0.04)
	else:
		set_brightness(1.0)
	for key in urls:
		start = dt.now()
		result = requests.get(urls[key])
		finish = dt.now()
		if result.status_code != 200:
			set_pixel(key, 255, 0, 0)
		elif (finish - start).seconds > 5:
			set_pixel(key, 255, 100, 0)
		else:
			if random() > 0.5:
				set_pixel(key, 0, 0, 255)
			else:
				set_pixel(key, 0, 255, 0)
		show()			
	time.sleep(60)
