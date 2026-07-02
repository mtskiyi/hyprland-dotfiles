local config_home = os.getenv("XDG_CONFIG_HOME") or (os.getenv("HOME") .. "/.config")
local config_dir = config_home .. "/hypr/hyprland"

local function load_config(name, ...)
    return assert(loadfile(config_dir .. "/" .. name .. ".lua"))(...)
end

-- COLORS
local colors = load_config("colors")
-- VARIABLES
local variables = load_config("general", colors)
-- ENVIROMENT
load_config("env")
-- AUTOSTART
load_config("execs")
-- RULES
load_config("rules")
--KEYBINDS
load_config("keybinds", variables)
