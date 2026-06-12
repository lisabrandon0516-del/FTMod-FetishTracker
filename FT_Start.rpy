# FTMod - Ultra Minimal Delayed Load Version (Option B)
# Goal: Touch as little as possible during early init to avoid breaking base game timing

define config.name = _("Lab Rats 2 Reformulate - Fetish Edition")
define config.window_icon = "FTimages/mod_icon.png"

init 100 python:
    config.version += " + FTMod 1.0 (Fetish Tracker)"
    
    def ft_enabled():
        try:
            return FT_MOD
        except NameError:
            return False

init 100 python:
    config.label_overrides["start"] = "FT_start"


label FT_start():
    scene bg paper_menu_background with fade
    "Lab Rats 2 contains adult content. If you are not over 18 or your country's equivalent age you should not view this content."
    menu:
        "I am over 18":
            pass
        "I am not over 18":
            $ renpy.full_restart()

    "[config.version]"

    if ft_enabled():
        "Fetish Tracker Mod is active."

    jump normal_start
