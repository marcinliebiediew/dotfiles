function toggle_keymap
set current (  setxkbmap -v | awk -F "+" '/symbols/ {print $2}')
if test $current = "pl(colemak)"
notify-send "qwerty"
 setxkbmap pl 
else if test $current = "pl" 
notify-send "colemak"
setxkbmap pl -variant colemak 
else
notify-send "setting colemak"
 setxkbmap pl -variant colemak
end
end
