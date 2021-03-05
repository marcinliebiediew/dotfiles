function mouse_click_toggle
set p /home/marcin/.config/scrpits/mouse
if test -e $p/clicked
echo "clikced"
rm $p/clicked
xdotool mousedown 1
else 
touch $p/clicked
xdotool mouseup 1
end
end
