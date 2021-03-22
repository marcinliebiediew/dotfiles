function zmk
 cd /home/marcin/Projects/keyboard/zmk/
 replay "source zephyr/zephyr-env.sh"
 cd app
 sudo mount --bind ~/.config/keyboard/bfk ~/Projects/keyboard/zmk/app/boards/shields/bfk
end

