# Hyprland Dotfiles

My personal Arch Linux Hyprland dotfiles.

## Screenshots

![Desktop](screenshots/desktop.png)

![Ranger](screenshots/ranger.png)

![Rofi](screenshots/rofi.png)

## Setup

- OS: Arch Linux
- WM: Hyprland
- Bar: Waybar
- Launcher: Rofi
- Terminal: Kitty
- Shell: Fish
- Notifications: Dunst
- File manager: Ranger
- Fetch: Fastfetch

## Structure

```txt
.config/
├── hypr/
├── waybar/
├── rofi/
├── kitty/
├── dunst/
├── fish/
├── fastfetch/
├── ranger/
├── gtk-3.0/
└── gtk-4.0/

Wallpapers/
screenshots/
```

## Install

## Install

```bash
git clone https://github.com/mtskiyi/hyprland-dotfiles.git
cd hyprland-dotfiles
cp -r .config/* ~/.config/
```

## Packages

```bash
sudo pacman -S hyprland waybar rofi kitty dunst fish fastfetch ranger
```

## Notes

These configs are made for my own setup, so some paths may need editing.
