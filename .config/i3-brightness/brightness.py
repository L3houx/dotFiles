from subprocess import call
import sys

brightness_path = "/sys/class/backlight/intel_backlight/"
current_brightness = float(open(brightness_path + "actual_brightness", "r").readline().replace("\n", ""))
max_brightness = float(open(brightness_path + "max_brightness", "r").readline().replace("\n", ""))

brightness_pourcentage = current_brightness / max_brightness

def information():
	print "Insert the parameter '+' or '-' to increase or decrease the brightness"
	print "Example: python brightness.py + to increase the brightness by 10%"
	print "Example: python brightness.py - to decrease the brightness by 10%"

if len(sys.argv) != 2:
	information()
	exit()
else:
	if sys.argv[1] == "+" and current_brightness != max_brightness:
		print "+"
		file_brightness = open(brightness_path + "brightness","w")
		brightness_upgraded = int(current_brightness + (max_brightness * 0.10))
		print brightness_upgraded / max_brightness
		file_brightness.write(str(brightness_upgraded))
	elif sys.argv[1] == "-" and current_brightness > 0:
		print "-"
		file_brightness = open(brightness_path + "brightness","w")
		brightness_upgraded = int(current_brightness - (max_brightness * 0.10))
		print brightness_upgraded / max_brightness
		file_brightness.write(str(brightness_upgraded))
	else:
		information()
		exit()
