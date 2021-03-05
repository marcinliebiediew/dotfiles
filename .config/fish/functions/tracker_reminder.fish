function tracker_reminder
set val (cat .config/watson/state | jq .project)
if not test "$val" = "null"
      echo ":)"
else
      echo "FUCKING TRACK THINGS"
end
end
