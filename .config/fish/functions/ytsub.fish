function ytsub
# downloads english transcript of youtube video
# url is passed from clipboard
# the content of clipboard is replaced with video transcript text
node ~/.config/scripts/youtube_transcript.mjs (xclip -o) | xclip -sel clip
end
