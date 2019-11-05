#!/bin/bash

# base dir for backlight class
basedir="/sys/class/backlight/"

# get the backlight handler
brightnessPath=$basedir$(ls $basedir)"/"

#Current brightness
current=$(cat $brightnessPath"brightness")
currentt= $(( $current / 100))

echo $currentt
#Max brightness
max=$(cat $brightnessPath"max_brightness")

# get current brightness %
old_brightness_p=$(( 100 * $current / $max ))

# calculate new brightness % 
new_brightness_p=$(($old_brightness_p $1))

# calculate new brightness value
new_brightness=$(( $max_brightness * $new_brightness_p / 100 ))

# set the new brightness value
sudo chmod 666 $brightnessPath"brightness"
echo $new_brightness > $brightnessPath"brightness"
