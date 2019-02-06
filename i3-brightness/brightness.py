from subprocess import call
import sys

brightness_path = "/sys/class/backlight/intel_backlight/"
current_brightness = float(open(brightness_path + "actual_brightness", "r").readline().replace("\n", ""))
max_brightness = float(open(brightness_path + "max_brightness", "r").readline().replace("\n", ""))

brightness_pourcentage = current_brightness / max_brightness

if len(sys.argv) != 2:
    print "Insert the parameter '+' or '-' to increase or decrease the brightness"
    exit()
else:
    if sys.argv[1] == "+":
        if current_brightness != max_brightness:
            print "+"
            print current_brightness / max_brightness
            file_brightness = open(brightness_path + "brightness","w") 
            print current_brightness
            brightness_upgraded = int(current_brightness + (max_brightness * 0.10))
            file_brightness.write(str(brightness_upgraded))
    elif sys.argv[1] == "-":
        if current_brightness > 0:
            print "-"
            print current_brightness / max_brightness
            file_brightness = open(brightness_path + "brightness","w") 
            print current_brightness
            brightness_upgraded = int(current_brightness - (max_brightness * 0.10))
            file_brightness.write(str(brightness_upgraded))
    else:
        print "Insert the parameter '+' or '-' to increase or decrease the brightness"
        exit()