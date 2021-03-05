function watson_menu
set selected (watson projects|rofi -dmenu)
watson stop    
watson start $selected
~/.config/scrpits/on-idle/on-idle.sh 300 pkill on-idle
watson stop
notify-send "stopped $selected"
end
