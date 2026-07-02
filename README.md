# Hyprland Dotfiles

My personal Arch Linux Hyprland dotfiles.

These configs are made for my own setup. Some paths, monitor settings, keyboard layout, and wallpapers may need editing.

## Screenshots

<p align="center">
  <img src="screenshots/desktop.png" width="200">
  <img src="screenshots/ranger.png" width="200">
  <img src="screenshots/rofi.png" width="200">
  <img src="screenshots/dunst.png" width="200">
</p>

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

## Required packages

The installer installs these packages automatically.

### Official Arch packages

```bash
sudo pacman -Syu --needed \
  git \
  hyprland xdg-desktop-portal-hyprland hyprshutdown \
  waybar rofi kitty dunst fish fastfetch ranger \
  swaybg \
  grim slurp wl-clipboard hyprpicker \
  brightnessctl playerctl pavucontrol \
  wireplumber \
  bluetui \
  eza \
  papirus-icon-theme adw-gtk-theme
```

### AUR packages

The installer installs these automatically if `yay` or `paru` is installed.

```bash
yay -S --needed ttf-google-sans-code-nf hyprqt6engine
```

or:

```bash
paru -S --needed ttf-google-sans-code-nf hyprqt6engine
```

## Install

Clone the repo:

```bash
git clone https://github.com/mtskiyi/hyprland-dotfiles.git
cd hyprland-dotfiles
```

Run the installer:

```bash
chmod +x install.sh installer.py
./install.sh
```

The installer asks once before running.

After confirmation, it will:

- install required Arch packages
- install AUR packages if `yay` or `paru` exists
- backup existing configs
- copy dotfiles to `~/.config`
- copy wallpaper to `~/Wallpapers/wallpaper.png`

Backups are saved as:

```txt
~/.config-backup-YYYYMMDD-HHMMSS
```

## Manual install

If you do not want to use the installer:

```bash
git clone https://github.com/mtskiyi/hyprland-dotfiles.git
cd hyprland-dotfiles

mkdir -p ~/.config
cp -r .config/* ~/.config/

mkdir -p ~/Wallpapers
cp Wallpapers/wallpaper.png ~/Wallpapers/wallpaper.png
```

## Optional: set Fish as default shell

```bash
chsh -s /usr/bin/fish
```

Log out and log back in after changing shell.

## Structure

```txt
hyprland-dotfiles/
├── .config/
│   ├── hypr/
│   ├── waybar/
│   ├── rofi/
│   ├── kitty/
│   ├── dunst/
│   ├── fish/
│   ├── fastfetch/
│   ├── ranger/
│   ├── gtk-3.0/
│   └── gtk-4.0/
├── Wallpapers/
│   └── wallpaper.png
├── screenshots/
│   ├── desktop.png
│   ├── ranger.png
│   ├── rofi.png
│   └── dunst.png
├── install.sh
├── installer.py
└── README.md
```

## Notes

- These configs use Hyprland Lua-style config files.
- Wallpaper is copied as `~/Wallpapers/wallpaper.png` because the Hyprland config uses that path.
- Keyboard layout is set to `us` by default.
- Change keyboard layout or monitor settings in `.config/hypr/hyprland/general.lua`.
- Existing configs are backed up when using the installer.
- Some configs are made for my personal setup, so edit paths and settings if something does not match your system.
