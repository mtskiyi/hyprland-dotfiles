#!/usr/bin/env python3

import shutil
import subprocess
import tempfile
from datetime import datetime
from pathlib import Path

REPO_DIR = Path(__file__).resolve().parent
HOME = Path.home()

CONFIG_DIR = REPO_DIR / ".config"
WALLPAPER = REPO_DIR / "Wallpapers" / "wallpaper.png"

PACMAN_PACKAGES = [
    "git",
    "base-devel",
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


def run(command: list[str], cwd: Path | None = None) -> None:
    print(f"\n:: Running: {' '.join(command)}\n")
    subprocess.run(command, check=True, cwd=cwd)


def ask_before_start() -> None:
    print("mtskiyi Hyprland Dotfiles Installer")
    print()
    print("This will:")
    print("- install official Arch packages")
    print("- install yay if no AUR helper is found")
    print("- install AUR packages")
    print("- backup existing configs")
    print("- copy dotfiles to ~/.config")
    print("- copy wallpaper to ~/Wallpapers/wallpaper.png")
    print()

    answer = input("Continue? [y/N]: ").strip().lower()

    if answer not in ["y", "yes"]:
        print("Cancelled.")
        raise SystemExit(0)


def install_pacman_packages() -> None:
    run(["sudo", "pacman", "-Syu", "--needed", *PACMAN_PACKAGES])


def install_yay() -> str:
    print("\n:: No AUR helper found. Installing yay...")

    run(["sudo", "pacman", "-S", "--needed", "git", "base-devel"])

    with tempfile.TemporaryDirectory() as temp_dir:
        yay_dir = Path(temp_dir) / "yay"

        run(["git", "clone", "https://aur.archlinux.org/yay.git", str(yay_dir)])
        run(["makepkg", "-si", "--noconfirm"], cwd=yay_dir)

    return "yay"


def get_aur_helper() -> str:
    for helper in ["yay", "paru"]:
        if shutil.which(helper):
            return helper

    return install_yay()


def install_aur_packages() -> None:
    aur_helper = get_aur_helper()
    run([aur_helper, "-S", "--needed", *AUR_PACKAGES])


def backup_and_copy_dotfiles() -> None:
    if not CONFIG_DIR.exists():
        print("Error: .config folder not found in repo.")
        raise SystemExit(1)

    backup_dir = HOME / f".config-backup-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    backup_dir.mkdir(parents=True, exist_ok=True)

    config_target_dir = HOME / ".config"
    config_target_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n:: Backup folder: {backup_dir}")

    for item in CONFIG_DIR.iterdir():
        target = config_target_dir / item.name

        if target.exists():
            print(f":: Backing up {target}")

            if target.is_dir():
                shutil.copytree(target, backup_dir / item.name, dirs_exist_ok=True)
                shutil.rmtree(target)
            else:
                shutil.copy2(target, backup_dir / item.name)
                target.unlink()

        print(f":: Installing {item.name}")

        if item.is_dir():
            shutil.copytree(item, target, dirs_exist_ok=True)
        else:
            shutil.copy2(item, target)

    wallpapers_dir = HOME / "Wallpapers"
    wallpapers_dir.mkdir(parents=True, exist_ok=True)

    if WALLPAPER.exists():
        shutil.copy2(WALLPAPER, wallpapers_dir / "wallpaper.png")
        print(":: Installed wallpaper to ~/Wallpapers/wallpaper.png")
    else:
        print(":: Warning: Wallpapers/wallpaper.png not found.")

    print("\n:: Dotfiles installed.")
    print(f":: Backup saved in: {backup_dir}")


def main() -> None:
    ask_before_start()
    install_pacman_packages()
    install_aur_packages()
    backup_and_copy_dotfiles()

    print()
    print("Done.")
    print("Log out and start Hyprland.")


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError:
        print("\nError: command failed.")
        raise SystemExit(1)
    except KeyboardInterrupt:
        print("\nCancelled.")
        raise SystemExit(1)
