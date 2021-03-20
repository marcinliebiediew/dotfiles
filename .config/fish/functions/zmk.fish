function zmk
 cd /home/marcin/tools/zmk/
 replay "source zephyr/zephyr-env.sh"
 cd app
 sudo mount --bind ~/.config/keyboard/bfk ~/tools/zmk/app/boards/shields/bfk
end

