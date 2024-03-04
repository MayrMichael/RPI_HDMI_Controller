#!/usr/bin/env python

import sys
import time
import RPi.GPIO as GPIO
import subprocess
from datetime import datetime


DETECTION_INTERVAL =  60
PIR_PIN = 25

TIME_SCHEDULE = {
    0: {'start_time': {'hour':16, 'minute':0, 'second':0}, 'end_time': {'hour':22, 'minute':0, 'second':0}},# Monday
    1: {'start_time': {'hour':16, 'minute':0, 'second':0}, 'end_time': {'hour':22, 'minute':0, 'second':0}},
    2: {'start_time': {'hour':16, 'minute':0, 'second':0}, 'end_time': {'hour':22, 'minute':0, 'second':0}},
    3: {'start_time': {'hour':16, 'minute':0, 'second':0}, 'end_time': {'hour':22, 'minute':0, 'second':0}},
    4: {'start_time': {'hour':16, 'minute':0, 'second':0}, 'end_time': {'hour':22, 'minute':0, 'second':0}},
    5: {'start_time': {'hour':9, 'minute':0, 'second':0}, 'end_time': {'hour':22, 'minute':0, 'second':0}},
    6: {'start_time': {'hour':9, 'minute':0, 'second':0}, 'end_time': {'hour':22, 'minute':0, 'second':0}}, # Sunday
}

DELAY_PIR = {'hour':1, 'minute':0, 'second':0}

monitor_on = False
pir_shutdown = datetime.now()

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIR_PIN, GPIO.IN)
    try:
        GPIO.add_event_detect(PIR_PIN , GPIO.RISING, callback=pir_detected_callback)
        while True:
            now = datetime.now()
            start_time = datetime.now().replace(**TIME_SCHEDULE[datetime.weekday(now)]['start_time'])
            end_time = datetime.now().replace(**TIME_SCHEDULE[datetime.weekday(now)]['end_time'])

            is_in_schedule = start_time <= now <= end_time

            if (is_in_schedule or now <= pir_shutdown) and not monitor_on:
                turn_on()
            elif (not is_in_schedule and now > pir_shutdown) and monitor_on:
                turn_off()

            time.sleep(DETECTION_INTERVAL)
    except KeyboardInterrupt:
        print("Exit...")
        GPIO.cleanup()

def pir_detected_callback(channel):
    print('There was a movement!')
    pir_shutdown = datetime.now() + datetime.timedelta(**DELAY_PIR)

def turn_on():
    monitor_on = True
    # subprocess.call("sh /home/pi/monitor_on.sh", shell=True)
    print('turn monitor on')

def turn_off():
    monitor_on = False
    # subprocess.call("sh /home/pi/monitor_off.sh", shell=True)
    print('turn monitor off')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
        # GPIO.cleanup()



 

 
