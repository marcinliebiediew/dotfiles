#!/usr/bin/env python3

import sys
import colorama

color = "%{F#f00}"
color_reset = "%{F-}"

# c* - current
# t* - total
# *w - workspace
# *t - tab
(
    current_workspace,
    total_workspaces,
    current_tab,
    all_tabs,
) = sys.stdin.readline().split(" / ")

current_indicator = "◆"
other_indicator = "◇"
separator = " "

workspace_indicator = [other_indicator] * (int(total_workspaces) + 1)
workspace_indicator[int(current_workspace)] = color + current_indicator + color_reset
workspace_indicator = separator.join(workspace_indicator).replace("\n", "")

tabs_indicator = all_tabs.replace(
    current_tab, f"{color}{current_tab}{color_reset}"
).replace("\n", "")

print(tabs_indicator, "\t", workspace_indicator)
