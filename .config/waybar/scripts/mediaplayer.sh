#!/bin/bash

playerctl --player=spotify,mpd,vlc,firefox,chromium,brave,helium metadata --format '{"text": "{{artist}} - {{title}}", "alt": "{{status}}", "class": "{{status}}"}' --follow 2>/dev/null | while read -r line; do
    # IF THE USER TOGGLED IT OFF -> HIDE EVERYTHING IMMEDIATELY
    if [ -f "$HOME/.config/waybar/scripts/.hide_music" ]; then
        echo '{"text": "", "alt": "stopped", "class": "stopped"}'
    elif [[ "$line" == *'""'* ]]; then
        echo '{"text": "", "alt": "stopped", "class": "stopped"}'
    else
        echo "$line" | sed 's/Playing/playing/g' | sed 's/Paused/paused/g'
    fi
done
