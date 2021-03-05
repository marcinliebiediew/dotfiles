function dell_touchscreen
xinput list |  grep 'pointer' | grep 'FlatFrog FlatFrog' | grep -Po '(?<=[id=])\d+' | xargs -I{} sh -c 'xinput map-to-output {} DP-1.1'
xinput list |  grep 'pointer' | grep 'FlatFrog FlatFrog' | grep -Po '(?<=[id=])\d+' | xargs -I{} sh -c 'xinput map-to-output {} HDMI-0'
end
