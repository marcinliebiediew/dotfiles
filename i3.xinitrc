#!/bin/sh

userresources=$HOME/.Xresources
usermodmap=$HOME/.Xmodmap
sysresources=/etc/X11/xinit/.Xresources
sysmodmap=/etc/X11/xinit/.Xmodmap

# merge in defaults and keymaps

if [ -f $sysresources ]; then
    xrdb -merge $sysresources
fi

if [ -f $sysmodmap ]; then
    xmodmap $sysmodmap
fi

if [ -f "$userresources" ]; then
    xrdb -merge "$userresources"
fi

if [ -f "$usermodmap" ]; then
    xmodmap "$usermodmap"
fi

# start some nice programs

xset r rate 200 60
if [ -d /etc/X11/xinit/xinitrc.d ] ; then
 for f in /etc/X11/xinit/xinitrc.d/?*.sh ; do
  [ -x "$f" ] && . "$f"
 done
 unset f
fi
# xinput set-prop "SynPS/2 Synaptics TouchPad" "Device Enabled" 0
# xrdb -merge ~/.Xresources
#xmodmap -e 'keycode 108 = Hyper_R'
#xmodmap -e 'add mod3 = Hyper_R'
#feh --reload 0.5 --bg-scale ~/.config/wall.png
#xmodmap "/home/marcin/.Xmodmap"
#/home/marcin/thinkmorse-rust/target/debug/thinkmorse siema!
picom -b
setxkbmap pl -variant colemak
setxkbmap -option keypad:pointerkeys
exec dbus-launch i3

