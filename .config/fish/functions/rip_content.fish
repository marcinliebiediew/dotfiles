function rip_content
    set dir (echo people\nquotes_and_wisdom\ninspiration\nfunny_and_memes\nfuture\nbeautiful_art_nature | rofi -dmenu)
    set rofi_path ~/.config/scripts/rofi_rip_content.sh
set dest ~/Dropbox/Pictures/$dir/screenshot_(date +%F_%T).png
    scrot --focused $dest
end
