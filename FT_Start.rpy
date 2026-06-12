# FTMod Start - Fetish Tracker Mod
# Fetish-focused evolution of VTMod

define config.name = _("Lab Rats 2 Reformulate - Fetish Edition")
define config.window_icon = "FTimages/mod_icon.png"
define FT_Game_Version = " + FTMod 1.0 (Fetish Tracker)"

init python:
    config.version += FT_Game_Version

    # ==================== FETISH FLAVOR TEXT LISTS ====================
    # Expanded and reorganized for deep fetish focus

    # --- Hypnosis / Mind Control ---
    FThypnoknowlist = [
        "Her eyes are so easy to get lost in...",
        "Would you like to watch her mind go blank?",
        "Want to see her eyes swirl for you?",
        "Ready to drop her into trance?",
        "Imagine how obedient she could become...",
        "Want to watch her thoughts melt away?",
        "How deep do you think you can take her?",
        "Ready to install some new triggers?"
    ]
    FThypnovirginlist = [
        "She's never been hypnotized before.",
        "Her mind is completely untouched... pure."],
        "No one has ever taken control of her thoughts.",
        "She's a hypnosis virgin - waiting to be programmed."
    ]
    FThypnoclaimlist = [
        "Her mind belongs to you now.",
        "You've claimed her thoughts completely.",
        "She obeys only you.",
        "Her will is yours to shape."
    ]

    # --- Breeding / Impregnation ---
    FTbreedingknowlist = [
        "Want to put a baby in her?",
        "Ready to breed her properly?",
        "Imagine her belly growing round with your child...",
        "Want to fill her womb until it takes?"
    ]
    FTbreedingvirginlist = [
        "She's never been bred before.",
        "Her womb is untouched and fertile."
    ]
    FTbreedingclaimlist = [
        "This womb is yours to fill.",
        "You've claimed her as breeding stock."
    ]

    # --- Exhibitionism ---
    FTexhibknowlist = [
        "Want everyone to see how slutty she is?",
        "Ready to show her off?",
        "Imagine her on display for others..."
    ]
    FTexhibvirginlist = [
        "She's never shown herself off before.",
        "Public exposure is completely new to her."
    ]
    FTexhibclaimlist = [
        "She loves being watched now.",
        "You've turned her into an exhibitionist."
    ]

    # --- Cumplay ---
    FTcumknowlist = [
        "Want to cover her in your cum?",
        "Ready to mark her with your load?",
        "Imagine her glazed and dripping..."
    ]
    FTcumvirginlist = [
        "She's never been properly covered before.",
        "Her skin has never known your cum."
    ]
    FTcumclaimlist = [
        "She craves being marked by you.",
        "You've made her a cumslut."
    ]

    # Keep original vaginal/oral/anal lists (abbreviated here for space - copy from your VT_Start.rpy)
    # You can expand these further
    FTvaginalknowlist = ["Want to be inside her pussy?", "Would you like to have vaginal sex with her?"]
    # ... (add the rest from your original file)

    # ==================== INDEXES & SHUFFLE FUNCTION ====================
    FThypnoknow_index = 0
    # ... add indexes for all new lists

    def FT_shuffle_and_update():
        import random
        # Shuffle all fetish lists here
        random.shuffle(FThypnoknowlist)
        # ... etc
        # Then assign to text variables
        pass  # Implement fully based on your original VT_shuffle_and_update

    FT_shuffle_and_update()


init -1 python:
    def ft_enabled():
        try:
            return FT_MOD
        except NameError:
            return False

    # Add more mod detection functions as needed


init 15 python:
    config.label_overrides["start"] = "FT_start"


label FT_start():
    scene bg paper_menu_background with fade
    "Lab Rats 2 contains adult content..."
    menu:
        "I am over 18":
            pass
        "I am not over 18":
            $ renpy.full_restart()

    "[config.version]"

    # Mod detection display (same style as original)
    $ modsinstalled = []
    if ft_enabled():
        $ modsinstalled.append("Fetish Tracker Mod")
    # ... other mods

    if modsinstalled:
        "[mod_message]"

    "Choose your starting fetish focus..."
    menu:
        "Balanced (all fetishes available)":
            $ persistent.starting_fetish_focus = "balanced"
        "Heavy Breeding & Pregnancy":
            $ persistent.starting_fetish_focus = "breeding"
        "Hypnosis & Mind Control Heavy":
            $ persistent.starting_fetish_focus = "hypno"
        "Exhibition & Public Play":
            $ persistent.starting_fetish_focus = "exhibition"
        "Cum & Marking Focused":
            $ persistent.starting_fetish_focus = "cumplay"

    # Call original pregnancy preference + game speed + mode menus (keep for compatibility)
    call screen VTMOD_setup_ui()  # You can rename/adapt this later

    # Character creation + game init (same as original)
    call screen character_create_screen()
    # ... rest of initialization logic from your VT_Start.rpy

    jump normal_start
