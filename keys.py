import serial
import json
import ast
#import os
from subprocess import Popen

ser = serial.Serial('/dev/cu.usbserial-023E572B', 115200)

def script(sc):
    p = Popen(['osascript', '-e', sc])

while(True):
    json_input = str(ser.readline().strip(), "ascii")
    json_data = json.loads(json_input)

    if (json_data['leftValue'] == 0 and json_data['rightValue'] != 0):
        script('tell application "Music" to play previous track')
        #cmd = """osascript -e 'tell application "System Events" to key code 98'"""
        #os.system(cmd)
    elif (json_data['leftValue'] != 0 and json_data['rightValue'] == 0):
        script('tell application "Music" to play next track')
        #cmd = """osascript -e 'tell application "System Events" to key code 100'"""
        #os.system(cmd)
    elif (json_data['leftValue'] == 0 and json_data['rightValue'] == 0):
        script('tell application "Music" to playpause')
        #cmd = """osascript -e 'tell application "System Events" to key code 101'"""
        #os.system(cmd)
    elif (json_data['leftValue'] != 0 and json_data['rightValue'] != 0):
        continue
    print(json_data)