#!/usr/bin/env python3

import shutil
import subprocess
from datetime import datetime
from pathlib import Path

REPO_DIR = Path(__file__).resolve().parent
HOME = Path.home()

CONFIG_DIR = REPO_DIR / ".config"
WALLPAPER = REPO_DIR / "Wallpapers" / "wallpaper.png"

PACMAN_PACKAGES = [
    "git",
    "hyprland",
    "xdg-desktop-portal-hyprland",
    "hyprshutdown",
    "waybar",
    "rofi",
    "kitty",
    "dunst",
    "fish",
    "fastfetch",
    "ranger",
    "swaybg",
    "grim",
    "slurp",
    "wl-clipboard",
    "hyprpicker",
    "brightnessctl",
    "playerctl",
    "pavucontrol",
    "wireplumber",
    "bluetui",
    "eza",
    "papirus-icon-theme",
    "adw-gtk-theme",
]

AUR_PACKAGES = [
    "ttf-google-sans-code-nf",
    "hyprqt6engine",
]


def run(command: list[str]) -> None:
    print(f"\n:: Running: {' '.join(command)}\n")
    subprocess.run(command, check=True)


def confirm() -> None:
    print("mtskiyi Hyprland Dotfiles Installer")
    print()
    print("This will:")
    print("- install required pacman packages")
    print("- install AUR packages if yay or paru exists")
    print("- backup old configs")
    print("- copy new dotfiles")
    print("- copy wallpaper")
    print("- enable bluetooth service")
    print()

    answer = input("Continue? [y/N]: ").strip().lower()

    if answer not in ["y", "yes"]:
        print("Cancelled.")
        raise SystemExit(0)


def install_pacman_packages() -> None:
    run(["sudo", "pacman", "-Syu", "--needed", *PACMAN_PACKAGES])


def install_aur_packages() -> None:
    aur_helper = None

    for helper in ["yay", "paru"]:
        if shutil.which(helper):
            aur_helper = helper
            break

    if aur_helper is None:
        print("\n:: No AUR helper found. Skipping AUR packages.")
        print(":: Install yay or paru manually if you want AUR packages.")
        return

    run([aur_helper, "-S", "--needed", *AUR_PACKAGES])


def backup_and_copy_dotfiles() -> None:
    if not CONFIG_DIR.exists():
        print("Error: .config folder not found in repo.")
        raise SystemExit(1)

    backup_dir = HOME / f".config-backup-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    backup_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n:: Backup folder: {backup_dir}")

    (HOME / ".config").mkdir(parents=True, exist_ok=True)

    for item in CONFIG_DIR.iterdir():
        target = HOME / ".config" / item.name

        if target.exists():
            print(f":: Backing up: {target}")

            if target.is_dir():
                shutil.copytree(target, backup_dir / item.name, dirs_exist_ok=True)
                shutil.rmtree(target)
            else:
                shutil.copy2(target, backup_dir / item.name)
                target.unlink()

        print(f":: Installing: {item.name}")

        if item.is_dir():
            shutil.copytree(item, target, dirs_exist_ok=True)
        else:
            shutil.copy2(item, target)

    wallpapers_dir = HOME / "Wallpapers"
    wallpapers_dir.mkdir(parents=True, exist_ok=True)

    if WALLPAPER.exists():
        shutil.copy2(WALLPAPER, wallpapers_dir / "black-hole.png")
        print(":: Installed wallpaper to ~/Wallpapers/black-hole.png")
    else:
        print(":: Warning: Wallpapers/wallpaper.png not found.")

    print(f"\n:: Backup saved in: {backup_dir}")


def enable_services() -> None:
    run(["sudo", "systemctl", "enable", "--now", "bluetooth"])


def install_everything() -> None:
    confirm()
    install_pacman_packages()
    install_aur_packages()
    backup_and_copy_dotfiles()
    enable_services()

    print()
    print("Done. Reboot or log out and start Hyprland.")


if __name__ == "__main__":
    try:
        install_everything()
    except subprocess.CalledProcessError:
        print("\nError: command failed.")
        raise SystemExit(1)
    except KeyboardInterrupt:
        print("\nCancelled.")
        raise SystemExit(1)
