import os
import sys
import time


def breathe_laptop(t=0.005, ticks=200, change=0.1, pause=0.5):
    for up in range(ticks):
        os.popen('light -A {}'.format(change))
        time.sleep(t)

    time.sleep(pause)

    for down in range(ticks):
        os.popen('light -U {}'.format(change))
        time.sleep(t)

    time.sleep(pause+0.55)


def breathe_hdmi(bus, current, t=0.35, ticks=200, change=8, spread=40, pause=0.1):
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


if len(sys.argv) > 2:
    loop = int(sys.argv[1])
    bus = int(sys.argv[2])
    current = int(sys.argv[3].strip(','))
    for _ in range(loop):
        breathe_hdmi(bus, current)
else:
    loop = int(sys.argv[1])
    for _ in range(loop):
        breathe_laptop()
