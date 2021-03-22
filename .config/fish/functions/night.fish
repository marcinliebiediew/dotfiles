function night
 emacsclient -e "(load-theme 'doom-acario-dark t)"&
 sudo ddcutil --bus=10 setvcp 10 1&
 light -S 10&
 bgchd -dir /home/marcin/Pictures/wallpapers/night -intv 5m -bcknd feh -rpl&
 sed -i 's/colors:\s\*gruvbox_[a-z]*$/colors: \*gruvbox_super_dark/g' ~/.config/alacritty/alacritty.yml&
end
