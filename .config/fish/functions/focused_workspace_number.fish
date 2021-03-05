function focused_workspace_number
 i3-msg -t get_workspaces \
    | jq '.[] | select(.focused==true).name' \
    | cut -d"\"" -f2 | string split : | head -n 1
end
