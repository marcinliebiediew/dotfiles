function boomandwerelive
echo $argv
streamlink -p "mpv --hwdec=auto-safe --vo=vdpau -wid $argv" "https://www.youtube.com/watch?v=5qap5aO4i9A" best
end
