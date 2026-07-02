#!/bin/bash

options="Toggle Music Bar\nRestart Waybar\nClose Menu"


chosen=$(echo -e "$options" | rofi -dmenu -i -p "Waybar Settings" -theme-str 'window { width: 300px; border-radius: 10px; }')

case "$chosen" in
    "Toggle Music Bar")
                if [ -f "$HOME/.config/waybar/scripts/.hide_music" ]; then
            rm "$HOME/.config/waybar/scripts/.hide_music"
        else
            touch "$HOME/.config/waybar/scripts/.hide_music"
        fi
        killall -SIGUSR2 waybar
        ;;
    "Restart Waybar")
        killall waybar && waybar &
        ;;
    *)
        exit 0
        ;;
esac
