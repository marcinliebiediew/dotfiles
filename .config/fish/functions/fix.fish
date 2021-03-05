function fix
 setxkbmap pl -variant colemak
 setxkbmap -option keypad:pointerkeys 
 xdotool key Caps_Lock
 xmodmap ~/.Xmodmap
 sudo modprobe uvcvideo
 sudo modprobe i2c-dev
 python ~/.config/scrpits/breathe.py 3 &
 sudo powertop --auto-tune
end
