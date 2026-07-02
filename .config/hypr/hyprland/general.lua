local colors = ...

hl.config({
    general = {
        gaps_in = 2,
        gaps_out = 3,
        border_size = 1,
        colors = colors.active_border,
        resize_on_border = false,
        allow_tearing = false,
        layout = "dwindle",
    },

    decoration = {
        -- rounding = 0,
        -- rounding_power = 0,
        active_opacity = 1.0,
        inactive_opacity = 1.0,
        -- shadow = {
        --     enabled = false,
        --     range = 4,
        --     render_power = 3,
        --     color = 0xee1a1a1a,
        -- },
        
        blur = {
            enabled = false,
            size = 3,
            passes = 1,
            vibrancy = 0.1696,
        },
    },

    animations = {
        enabled = true,
    },
})

hl.curve("expressiveFastSpatial", {
    type = "bezier",
    points = { { 0.42, 1.67 }, { 0.21, 0.90 } },
})
hl.curve("expressiveSlowSpatial", {
    type = "bezier",
    points = { { 0.39, 1.29 }, { 0.35, 0.98 } },
})
hl.curve("expressiveDefaultSpatial", {
    type = "bezier",
    points = { { 0.38, 1.21 }, { 0.22, 1.00 } },
})
hl.curve("emphasizedDecel", {
    type = "bezier",
    points = { { 0.05, 0.7 }, { 0.1, 1 } },
})
hl.curve("emphasizedAccel", {
    type = "bezier",
    points = { { 0.3, 0 }, { 0.8, 0.15 } },
})
hl.curve("standardDecel", {
    type = "bezier",
    points = { { 0, 0 }, { 0, 1 } },
})
hl.curve("menu_decel", {
    type = "bezier",
    points = { { 0.1, 1 }, { 0, 1 } },
})
hl.curve("menu_accel", {
    type = "bezier",
    points = { { 0.52, 0.03 }, { 0.72, 0.08 } },
})
hl.curve("stall", {
    type = "bezier",
    points = { { 1, -0.1 }, { 0.7, 0.85 } },
})

hl.animation({
    leaf = "windowsIn",
    enabled = true,
    speed = 3,
    bezier = "emphasizedDecel",
    style = "popin 80%",
})
hl.animation({
    leaf = "fadeIn",
    enabled = true,
    speed = 3,
    bezier = "emphasizedDecel",
})
hl.animation({
    leaf = "windowsOut",
    enabled = true,
    speed = 2,
    bezier = "emphasizedDecel",
    style = "popin 90%",
})
hl.animation({
    leaf = "fadeOut",
    enabled = true,
    speed = 2,
    bezier = "emphasizedDecel",
})
hl.animation({
    leaf = "windowsMove",
    enabled = true,
    speed = 3,
    bezier = "emphasizedDecel",
    style = "slide",
})
hl.animation({
    leaf = "border",
    enabled = true,
    speed = 10,
    bezier = "emphasizedDecel",
})
hl.animation({
    leaf = "layersIn",
    enabled = true,
    speed = 3,
    bezier = "emphasizedDecel",
    style = "popin 93%",
})
hl.animation({
    leaf = "layersOut",
    enabled = true,
    speed = 4,
    bezier = "menu_accel",
    style = "popin 94%",
})
hl.animation({
    leaf = "fadeLayersIn",
    enabled = true,
    speed = 0.5,
    bezier = "menu_decel",
})
hl.animation({
    leaf = "fadeLayersOut",
    enabled = true,
    speed = 2.7,
    bezier = "stall",
})
hl.animation({
    leaf = "workspaces",
    enabled = true,
    speed = 7,
    bezier = "menu_decel",
    style = "slide",
})
hl.animation({
    leaf = "specialWorkspaceIn",
    enabled = true,
    speed = 2.8,
    bezier = "emphasizedDecel",
    style = "slidevert",
})
hl.animation({
    leaf = "specialWorkspaceOut",
    enabled = true,
    speed = 1.2,
    bezier = "emphasizedAccel",
    style = "slidevert",
})
hl.animation({
    leaf = "zoomFactor",
    enabled = true,
    speed = 3,
    bezier = "standardDecel",
})

hl.config({
    dwindle = {
        preserve_split = true,
    },
})

hl.config({
    master = {
        new_status = "master",
    },
})

hl.config({
    scrolling = {
        fullscreen_on_one_column = true,
    },
})

hl.config({
    misc = {
        -- force_default_wallpaper = -1,
        -- disable_hyprland_logo = true,
    },
})

hl.config({
    input = {
        kb_layout = "us",
        kb_variant = "",
        kb_model = "",
        kb_options = "caps:none",
        kb_rules = "",

        follow_mouse = 1,

        sensitivity = -0.8,
    },
})

hl.gesture({
    fingers = 3,
    direction = "horizontal",
    action = "workspace",
})

return {
    terminal = "kitty",
    file_manager = "kitty ranger",
    main_mod = "SUPER",
}
