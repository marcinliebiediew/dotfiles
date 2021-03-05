function thinkpad_touchscreen
xinput list |  grep 'pointer' | grep 'Wacom' | grep -Po '(?<=[id=])\d+' | xargs -I{} sh -c 'xinput map-to-output {} eDP-1-1'
end
