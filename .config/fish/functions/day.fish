function day
 emacsclient -e "(load-theme 'leuven t)"&
 sudo ddcutil --bus=10 setvcp 10 100&
 light -S 100&
 bgchd -dir /home/marcin/Pictures/wallpapers/day -intv 5m -bcknd feh -rpl&
 sed -i 's/colors:\s\*gruvbox_[_a-z]*$/colors: \*gruvbox_light/g' ~/.config/alacritty/alacritty.yml&
end
