import threading
import subprocess
import RPi.GPIO as GPIO
import time
time.sleep(10)

power_switch_pin = 40

print('power switch script is running')
print("gound pin number {} on the board to shut down".format(power_switch_pin))

try:
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(power_switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	time.sleep(1)
	GPIO.wait_for_edge(power_switch_pin, GPIO.RISING)
	
	print('shutting down...')
	time.sleep(5)
	
	subprocess.call('sudo shutdown -h now', shell=True)

finally:
	GPIO.cleanup()
