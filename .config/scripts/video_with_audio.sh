#!/usr/bin/env sh
URL=$(xclip -o -selection clipboard)
echo $URL
echo $1
mpv --hwdec=auto-safe --vo=vdpau -wid $1 $URL 
