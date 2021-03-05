function change_workspace_name
i3-input -F 'rename workspace to "'(focused_workspace_number)':%s"' -P 'New name for this workspace: '  
end
