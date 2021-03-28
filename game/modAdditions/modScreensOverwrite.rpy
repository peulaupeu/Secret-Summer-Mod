screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background

    #code
    if main_menu:

        imagebutton idle "gui/start_idle.png" hover "gui/start_hover.png" focus_mask True action Start()

        imagebutton idle "gui/load_idle.png" hover "gui/load_hover.png" focus_mask True action ShowMenu("load")

        imagebutton idle "gui/option_idle.png" hover "gui/option_hover.png" focus_mask True action ShowMenu("preferences")

        imagebutton idle "gui/patreon_idle.png" hover "gui/patreon_hover.png" focus_mask True action OpenURL ("https://www.patreon.com")

        imagebutton idle "gui/discord_idle.png" hover "gui/discord_hover.png" focus_mask True action OpenURL ("https://www.patreon.com")

        imagebutton idle "gui/logo_idle.png" hover "gui/logo_hover.png" focus_mask True action OpenURL ("https://www.patreon.com")

        textbutton "Scene Gallery" action [ui.callsinnewcontext("galleryNameChange"), Show("sceneGalleryMenu")] text_style "modTextButtonHeader"

        if renpy.variant("pc"):
            imagebutton idle "gui/quit_idle.png" hover "gui/quit_hover.png" focus_mask True action Quit(confirm=not main_menu)

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"

    # imagebutton:
    #     action [ui.callsinnewcontext("galleryNameChange"), Show("sceneCharacterMenu")]
    #     idle Transform("modAdditions/images/cloud.png", zoom=0.4)
    #     hover Transform(im.MatrixColor("modAdditions/images/cloud.png", im.matrix.brightness(0.2)), zoom=0.4)
    #     align (1.0, 0.025)
    #     background None
    #     hover_background None

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')
            if KoGa3ModMenuButtonPressed == False:
                textbutton "Mod Menu": #KoGa3
                    selected False
                    action [
                    SetVariable ("KoGa3ModMenuButtonPressed", True),
                    SetVariable ("nptsTemp", npts),
                    SetVariable ("cptsTemp", cpts),
                    SetVariable ("lptsTemp", lpts),
                    SetVariable ("iptsTemp", ipts),
                    SetVariable ("zptsTemp", zpts),
                    Show("KoGa3ScreenModMenu") ]
            if KoGa3ModMenuButtonPressed == True:
                textbutton "Close Mod Menu": #KoGa3
                    selected False
                    action [
                    SetVariable ("KoGa3ModMenuButtonPressed", False),
                    Hide("KoGa3ScreenCheatMore1"),
                    Hide("KoGa3ScreenJukebox"),
                    Hide("KoGa3ScreenModMenu") ]

screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()
            if KoGa3ModMenuButtonPressed == False:
                textbutton "Mod Menu": #KoGa3
                    selected False
                    action [
                    SetVariable ("KoGa3ModMenuButtonPressed", True),
                    SetVariable ("nptsTemp", npts),
                    SetVariable ("cptsTemp", cpts),
                    SetVariable ("lptsTemp", lpts),
                    SetVariable ("iptsTemp", ipts),
                    SetVariable ("zptsTemp", zpts),
                    Show("KoGa3ScreenModMenu") ]
            if KoGa3ModMenuButtonPressed == True:
                textbutton "Close Mod Menu": #KoGa3
                    selected False
                    action [
                    SetVariable ("KoGa3ModMenuButtonPressed", False),
                    Hide("KoGa3ScreenCheatMore1"),
                    Hide("KoGa3ScreenJukebox"),
                    Hide("KoGa3ScreenModMenu") ]
