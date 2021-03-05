function voice
if [ (audio-recorder -c status) = "not running" ] 
audio-recorder -c start
audio-recorder -c hide
else 
audio-recorder -c stop
sudo pkill audio-recorder
end
end
