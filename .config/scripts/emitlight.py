import os
import sys
import time


def breathe_hdmi(bus, current, t=2, change=1, spread=40, pause=1.1):
    if current > 85:
        uprange = range(current, current-spread, -1*change)
        downrange = range(spread-50, current, change)
    else:
        uprange = range(current, current+spread, change)
        downrange = range(current+spread, current, -1*change)

    for up in uprange:
        os.popen(f'sudo ddcutil --bus={bus} setvcp 10 {up}')
        time.sleep(t)

    time.sleep(pause)

    for down in downrange:
        os.popen(f'sudo ddcutil --bus={bus} setvcp 10 {down}')
        time.sleep(t)

    time.sleep(pause)


bus = int(sys.argv[1])
current = int(sys.argv[2].strip(','))
try:
    spread = int(sys.argv[3])
except:
    spread = 40
while True:
    breathe_hdmi(bus, current, spread=spread)
