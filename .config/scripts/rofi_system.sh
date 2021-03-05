#!/usr/bin/bash

# If there was a selection, find its path from the src file and launch vscode.
if [ -z "$1" ]; then
    # jq -r "sort_by(.name) | .[].name" < $SRC 
    echo audio_laptop
    echo audio_dock
    echo boom_and_were_live
    echo reset_hdmi
    echo brightness_high_hdmi
    echo brightness_medium_hdmi
    echo brightness_low_hdmi
    echo brightness_emit_hdmi
else
    fish -c $1
fi
