# You may need to comment out the next line to disable access control.
#xhost +SI:localuser:$USER



xrdb -merge /etc/X11/xinit/.Xresources


# Set themes, etc.
gnome-settings-daemon &

# Set fallback cursor.
xsetroot -cursor_name left_ptr

# Set keyboard repeat rate.
xset r rate 200 60

# If Emacs is started in server mode, `emacsclient` is a convenient way to
# edit files in place (used by e.g. `git commit`).
export VISUAL=emacsclient
export EDITOR="$VISUAL"

xrdb -merge /home/marcin/exwm.Xresources
#setxkbmap pl -variant colemak
#picom -b

# Finally launch emacs.
#exec dbus-launch --exit-with-session emacs --mm --debug-init
#exec dbus-launch --exit-with-session emacs --debug-init --eval "(exwm-enable)"
#exec dbus-launch emacsclient -nc --debug-init
#exec dbus-launch emacsclient -nc --eval "(exwm-enable)" #<goodone!
#exec dbus-launch emacsclient -c #--eval "(exwm-enable)" 
#exec dbus-launch emacs --eval "(exwm-enable)" --debug-init
exec dbus-launch emacs --eval "(exwm-enable)" 
#exec dbus-launch emacs 
