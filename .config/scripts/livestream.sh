#!/usr/bin/env sh
URL=$(xclip -o -selection clipboard)
echo $URL
echo $1
streamlink -p "mpv --hwdec=auto-safe --vo=vdpau --no-audio -wid $1" $URL best
