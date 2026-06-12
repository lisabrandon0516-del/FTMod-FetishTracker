# FTMod Start - Minimal Safe Version for Testing
# Only essential code to avoid load order conflicts

define config.name = _("Lab Rats 2 Reformulate - Fetish Edition")
define config.window_icon = "FTimages/mod_icon.png"
define FT_Game_Version = " + FTMod 1.0 (Fetish Tracker)"

init python:
    config.version += FT_Game_Version

    def ft_enabled():
        try:
            return FT_MOD
        except NameError:
            return False

init 15 python:
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

    $ modsinstalled = []
    if ft_enabled():
        $ modsinstalled.append("Fetish Tracker Mod")

    if modsinstalled:
        $ mod_message = "{image=ftcherries_small} Fetish Tracker Mod is active."
        "[mod_message]"

    jump normal_start
