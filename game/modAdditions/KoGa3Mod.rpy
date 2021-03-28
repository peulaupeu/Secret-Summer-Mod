#Mod for the game Secret Summer / KoGa3#

#-------------------new audio channel for the game
init python:
    renpy.music.register_channel("sound1", mixer="sfx")
    renpy.music.register_channel("sound2", mixer="sfx")


#-------------------Textbutton Colors------------------#
init python:
    style.KoGa3_button_text.color = "#ffdf00"
    style.KoGa3_button_text.hover_color = "#c90016"
    style.KoGa3_button_text.selected_color = "#ff0000"
    style.KoGa3_button_text.size = 32

    style.KoGa3_1_button_text.color = "#888888"
    style.KoGa3_1_button_text.hover_color = "#888888"
    style.KoGa3_1_button_text.selected_color = "#888888"

    style.KoGa3_2_button_text.color = "#ff9999"
    style.KoGa3_2_button_text.hover_color = "#800000"
    style.KoGa3_2_button_text.selected_color = "#ff9999"
    style.KoGa3_2_button_text.size = 25
    style.KoGa3_2_button_text.outlines = [ (absolute(2), "#000000", absolute(0), absolute(0)) ]

    style.KoGa3_3_button_text.color = "#98fb98"
    style.KoGa3_3_button_text.hover_color = "#2a8000"
    style.KoGa3_3_button_text.selected_color = "#98fb98"
    style.KoGa3_3_button_text.size = 25
    style.KoGa3_3_button_text.outlines = [ (absolute(2), "#000000", absolute(0), absolute(0)) ]

    style.KoGa3_4_button_text.color = "#87cefa"
    style.KoGa3_4_button_text.hover_color = "#0000cd"
    style.KoGa3_4_button_text.selected_color = "#87cefa"
    style.KoGa3_4_button_text.size = 25
    style.KoGa3_4_button_text.outlines = [ (absolute(2), "#000000", absolute(0), absolute(0)) ]

    style.KoGa3_5_button_text.color = "#ffffff"
    style.KoGa3_5_button_text.hover_color = "#696969"
    style.KoGa3_5_button_text.selected_color = "#ffffff"
    style.KoGa3_5_button_text.size = 25
    style.KoGa3_5_button_text.outlines = [ (absolute(2), "#000000", absolute(0), absolute(0)) ]

default KoGa3_status_button_text = "KoGa3_5_button_text"

#---------------------blank screen---------------------#
screen KoGa3ScreenBlank:
    add "/modAdditions/images/KoGa3MenuBack.png"
    modal True

#---------------------set stats icon---------------------#
screen KoGa3ScreenStats():
    hbox:
        xalign 0.5
        yalign 0.0
        if KoGa3ScreenStatsFull == 1 or KoGa3ScreenStatsFull == 2:
            if KoGa3OscarSix == 1:
                if KoGa3ChoiceOption == 1:
                    textbutton ("WT:ON   "):
                        text_style KoGa3_status_button_text
                        selected False
                        action [
                        SetVariable("gr", KoGa3ChoiceTextOFF),
                        SetVariable("NorahPath", KoGa3ChoiceTextOFF),
                        SetVariable("ZoePath", KoGa3ChoiceTextOFF),
                        SetVariable("CoralPath", KoGa3ChoiceTextOFF),
                        SetVariable("LeannePath", KoGa3ChoiceTextOFF),
                        SetVariable("IrenePath", KoGa3ChoiceTextOFF),
                        SetVariable("ZoePeek", KoGa3ChoiceTextOFF),
                        SetVariable("OscarSixModText1", KoGa3ChoiceTextOFF),
                        SetVariable("Leanne_raw", KoGa3ChoiceTextOFF),
                        SetVariable("KoGa3ChoiceView1", KoGa3ChoiceTextOFF),#not used
                        SetVariable("KoGa3ChoiceView2", KoGa3ChoiceTextOFF),#not used
                        SetVariable("KoGa3ChoiceView3", KoGa3ChoiceTextOFF),#not used
                        SetVariable("KoGa3ChoiceOption", 0) ]
                if KoGa3ChoiceOption == 0:
                    textbutton ("WT:OFF  "):
                        text_style KoGa3_status_button_text
                        selected False
                        action [
                        SetVariable("gr", "{color=#0f0}"),
                        SetVariable("NorahPath", "{color=#0f0}[Norah Path]"),
                        SetVariable("ZoePath", "{color=#0f0}[Zoe Path]"),
                        SetVariable("CoralPath", "{color=#0f0}[Coral Path]"),
                        SetVariable("LeannePath", "{color=#0f0}[Leanne Path]"),
                        SetVariable("IrenePath", "{color=#0f0}[Irene Path]"),
                        SetVariable("ZoePeek", "{color=#0f0}[Zoe Peek]"),
                        SetVariable("OscarSixModText1", " [Coral points >= 3 recommended]"),
                        SetVariable("Leanne_raw", "{color=#0f0}[Leanne raw]"),
                        SetVariable("KoGa3ChoiceView1", KoGa3ChoiceText1),  #not used
                        SetVariable("KoGa3ChoiceView2", KoGa3ChoiceText2),  #not used
                        SetVariable("KoGa3ChoiceView3", KoGa3ChoiceText3),  #not used
                        SetVariable("KoGa3ChoiceOption", 1) ]
        if KoGa3ScreenStatsFull == 1:
            textbutton ("Norah:[npts] Coral:[cpts] Leanne:[lpts] Irene:[ipts] Zoe:[zpts]"):
                text_style KoGa3_status_button_text
                selected True
                action [
                SetVariable ("nptsTemp", npts),
                SetVariable ("cptsTemp", cpts),
                SetVariable ("lptsTemp", lpts),
                SetVariable ("iptsTemp", ipts),
                SetVariable ("zptsTemp", zpts),
                SetVariable ("KoGa3ModMenuButtonPressed", True),
                Show("KoGa3ScreenModMenu") ]


#---------------------set Mod menu---------------------#

define rel_points = [
  ["Norah", "npts"],
  ["Coral", "cpts"],
  ["Leanne", "lpts"],
  ["Irene", "ipts"],
  ["Zoe", "zpts"],
]

define choices = [
  ["nshower", "EP2: \"nshower\" (Norah shower):"],
  ["croute", "EP3: \"croute\" (Coral route):"],
  ["Cpanties", "EP4: \"Cpanties\" (Coral panties):"],
  ["Cbf", "EP4: \"Cbf\" (Coral boyfriend):"],
  ["nroute", "EP5: \"nroute\" (Norah route):"],
  ["zsecret", "EP5: \"zsecret\" (Zoe secret):"],
  ["zroute", "EP5: \"zroute\" (Zoe route):"],
  ["Imf", "EP6: \"Imf\" (Irene mother fig.):"],
  ["Lraw", "EP7: \"Lraw\": (Leanne raw sex)"],
]

screen KoGa3ScreenModMenu:
    add "/modAdditions/images/KoGa3MenuBack.png"
    modal True
    vbox:
        xalign 0.5
        #yalign 0.5
        #text " "
        text " "
        text "=============== Mod menu ============="
        hbox:
            spacing 5
            textbutton "{color=#808080}Relationship points:{/color}":
                text_style "KoGa3_button_text"
                selected True
                sensitive False
                action NullAction()
        text "---------------------------------------------------------------------------"

        if KoGa3CheatButton == 1:
            for r in rel_points:
                hbox:
                    hbox:
                        xsize 475
                        textbutton "{color=#808080}"+ r[0] +" points:{/color}":
                            text_style "KoGa3_button_text"
                            selected True
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize 122
                        textbutton "{color=#ffffff}"+ str(eval(r[1])) +"{/color}":
                            text_style "KoGa3_button_text"
                            selected True
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize 115
                        textbutton _("+1"):
                            text_style "KoGa3_button_text"
                            action SetVariable(r[1], eval(r[1]) +1)
                    hbox:
                        xsize 115
                        if eval(r[1]) >= 1:
                            textbutton _("-1"):
                                text_style "KoGa3_button_text"
                                action SetVariable(r[1], eval(r[1]) -1)
                    hbox:
                        xsize 125
                        if eval(r[1]) != eval(r[1] +"Temp"):
                            textbutton ("Reset"):
                                text_style "KoGa3_button_text"
                                action SetVariable(r[1], eval(r[1] +"Temp"))


        text "---------------------------------------------------------------------------"
        if KoGa3ScreenStatsFull == 1:
            hbox:
                #xsize 400
                spacing 5
                textbutton ("Status infos:"):
                    text_style "KoGa3_button_text"
                    action SetVariable("KoGa3ScreenStatsFull", 0), Hide("KoGa3ScreenStats")
                textbutton ("ON"):
                    text_style "KoGa3_button_text"
                    selected True
                    #sensitive False
                    action NullAction()
                textbutton "{color=#808080}     color:{/color}":
                    text_style "KoGa3_button_text"
                    selected True
                    sensitive False
                    action NullAction()
                textbutton ("{size=29}red{/size}"):
                    text_style "KoGa3_2_button_text"
                    action SetVariable("KoGa3_status_button_text", "KoGa3_2_button_text")
                textbutton ("{size=29}green{/size}"):
                    text_style "KoGa3_3_button_text"
                    action SetVariable("KoGa3_status_button_text", "KoGa3_3_button_text")
                textbutton ("{size=29}blue{/size}"):
                    text_style "KoGa3_4_button_text"
                    action SetVariable("KoGa3_status_button_text", "KoGa3_4_button_text")
                textbutton ("{size=29}gray{/size}"):
                    text_style "KoGa3_5_button_text"
                    action SetVariable("KoGa3_status_button_text", "KoGa3_5_button_text")
        if KoGa3ScreenStatsFull == 0:
            hbox:
                #xsize 400
                spacing 5
                textbutton ("Status infos:"):
                    text_style "KoGa3_button_text"
                    action SetVariable("KoGa3ScreenStatsFull", 1), Show("KoGa3ScreenStats")
                textbutton ("OFF"):
                    text_style "KoGa3_button_text"
                    selected True
                    #sensitive False
                    action NullAction()
        if KoGa3OscarSix == 1:
            if KoGa3ChoiceOption == 1:
                textbutton ("Walkthrough by OscarSix:  {color=#ff0000}ON {/color} {color=#808080}(if installed){/color}"):
                    text_style "KoGa3_button_text"
                    selected False
                    action [
                    SetVariable("gr", KoGa3ChoiceTextOFF),
                    SetVariable("NorahPath", KoGa3ChoiceTextOFF),
                    SetVariable("ZoePath", KoGa3ChoiceTextOFF),
                    SetVariable("CoralPath", KoGa3ChoiceTextOFF),
                    SetVariable("LeannePath", KoGa3ChoiceTextOFF),
                    SetVariable("IrenePath", KoGa3ChoiceTextOFF),
                    SetVariable("ZoePeek", KoGa3ChoiceTextOFF),
                    SetVariable("OscarSixModText1", KoGa3ChoiceTextOFF),
                    SetVariable("Leanne_raw", KoGa3ChoiceTextOFF),
                    SetVariable("KoGa3ChoiceView1", KoGa3ChoiceTextOFF),#not used
                    SetVariable("KoGa3ChoiceView2", KoGa3ChoiceTextOFF),#not used
                    SetVariable("KoGa3ChoiceView3", KoGa3ChoiceTextOFF),#not used
                    SetVariable("KoGa3ChoiceOption", 0) ]
            if KoGa3ChoiceOption == 0:
                textbutton ("Walkthrough by OscarSix:  {color=#ff0000}OFF{/color}"):
                    text_style "KoGa3_button_text"
                    selected False
                    action [
                    SetVariable("gr", "{color=#0f0}"),
                    SetVariable("NorahPath", "{color=#0f0}[Norah Path]"),
                    SetVariable("ZoePath", "{color=#0f0}[Zoe Path]"),
                    SetVariable("CoralPath", "{color=#0f0}[Coral Path]"),
                    SetVariable("LeannePath", "{color=#0f0}[Leanne Path]"),
                    SetVariable("IrenePath", "{color=#0f0}[Irene Path]"),
                    SetVariable("ZoePeek", "{color=#0f0}[Zoe Peek]"),
                    SetVariable("OscarSixModText1", " [Mod makes sures you have enough points]"),
                    SetVariable("Leanne_raw", "{color=#0f0}[Leanne raw]"),
                    SetVariable("KoGa3ChoiceView1", KoGa3ChoiceText1),  #not used
                    SetVariable("KoGa3ChoiceView2", KoGa3ChoiceText2),  #not used
                    SetVariable("KoGa3ChoiceView3", KoGa3ChoiceText3),  #not used
                    SetVariable("KoGa3ChoiceOption", 1) ]
        else:
            textbutton ("Walkthrough by ShaddyModda: n/a"):
                text_style "KoGa3_button_text"
                selected True
                sensitive False
                action NullAction()
        textbutton _("Show/change game choices..."):
            text_style "KoGa3_button_text"
            action Hide("KoGa3ScreenModMenu"), Show("KoGa3ScreenCheatMore1")
        textbutton _("change MC name/relationships..."):
            text_style "KoGa3_button_text"
            action [
            Hide("KoGa3ScreenModMenu"),
            Show("KoGa3ScreenBlank"),
            Call("KoGa3NameChange") ]

        text "==================================="
        textbutton _("Done"):
            text_style "KoGa3_button_text"
            selected False
            action [
            SetVariable ("KoGa3ModMenuButtonPressed", False),
            Hide("KoGa3ScreenModMenu") ]



#-------------------set cheat more menu------------------#
screen KoGa3ScreenCheatMore1():
    add "/modAdditions/images/KoGa3MenuBack.png"
    modal True
    vbox:
        xalign 0.5
        #yalign 0.4
        text ""
        text "============= game choices ============="
        for c in choices:
            hbox:
                hbox:
                    xsize 650
                    textbutton (c[1]):
                        text_style "KoGa3_1_button_text"
                        selected False
                        sensitive False
                        action NullAction()
                hbox:
                    xsize 200
                    textbutton (str(eval(c[0]))):
                        text_style "KoGa3_button_text"
                        selected False
                        action ToggleVariable(c[0])

        text "==================================="
        hbox:
            spacing 30
            textbutton _("Back"):
                text_style "KoGa3_button_text"
                selected False
                action Hide("KoGa3ScreenCheatMore1"), Show("KoGa3ScreenModMenu")
            textbutton _("Done"):
                text_style "KoGa3_button_text"
                selected False
                action [
                SetVariable ("KoGa3ModMenuButtonPressed", False),
                Hide("KoGa3ScreenCheatMore1") ]


#-------------------set MC name------------------#
label KoGa3NameChange:
    menu:
        "MC name: [p_name] ":
            $ p_name = renpy.input("What is your name?", default=p_name)
            jump KoGa3NameChange
        "The relationship of the younger girl(s) to you: [rel_s] ":
            $ rel_s = renpy.input("What is their relationship to you (hint: s*ster)?", default=rel_s)
            jump KoGa3NameChange
        "You are their: [rel_b] ":
            $ rel_b = renpy.input("What is your relationship to them? (hint: bro**er)", default=rel_b)
            jump KoGa3NameChange
        "The ex wife of the older man is your?: [rel_m] / [m_nik]":
            $ rel_m = renpy.input("What is your relationship to her? (hint: mo**er)", default=rel_m)
            $ m_nik = renpy.input("What do you call her? (hint: M.m)", default=m_nik)
            jump KoGa3NameChange
        "The new wife of the older man is your?: [rel_sm]":
            $ rel_sm = renpy.input("What is her relationship to you? (hint: stepm**er)", default=rel_sm)
            jump KoGa3NameChange
        "The older man in the house is your?: [rel_f] ":
            $ rel_f = renpy.input("What is his relationship to you? (hint: fa**er)", default=rel_f)
            jump KoGa3NameChange
        "The people in the house are?: [rel_fam] ":
            $ rel_fam = renpy.input("What are they called together? (hint: fa*ily)", default=rel_fam)
            jump KoGa3NameChange
        "Done":
            hide screen KoGa3ScreenBlank
            show screen KoGa3ScreenModMenu
            pause
            return



#---------------------set variable game beginning---------------------#

#default for cheat menu#
default KoGa3ModStart = 1
default KoGa3ModMenuButtonPressed = False
default KoGa3ScreenStatsFull = 0
default KoGa3MainMenu = 0
default KoGa3CheatButton = 1
default KoGa3MusicChannel = 0
default KoGa3JukeboxButton = 1
#default KoGa3CurrentMusic = MusicMenu1
#default KoGa3Music = 1    #variable music
#default KoGa3SSound = 1   #variable sound effects              (bump, knock, ...)
#default KoGa3HSound = 1   #variable human sounds               (haha, sigh, shh,...)
#default KoGa3ESound = 1   #variable human erotic               (moaning and kissing)

default p_name = "John"
default rel_s = "roommate"
default rel_b = "roommate"
default rel_sm = "landlady"
default rel_f = "landlord"

default iptsTemp = 0
default zptsTemp = 0
default lptsTemp = 0
default nptsTemp = 0
default cptsTemp = 0


#---------------------set variable name setting---------------------#


#--------------settings best choice option---------------#
default KoGa3ChoiceOption = 0
default KoGa3OscarSix = 1       #WT Mod from OscarSix
default KoGa3ChoiceText1 = "\n{color=#008000}recommended{/color}"
default KoGa3ChoiceText2 = "\n{color=#0000ff}choice is not essential{/color}"
default KoGa3ChoiceText3 = "\n{color=#ff0000}bad choice{/color}"
default KoGa3ChoiceTextOFF = ""
default KoGa3ChoiceView1 = KoGa3ChoiceTextOFF
default KoGa3ChoiceView2 = KoGa3ChoiceTextOFF
default KoGa3ChoiceView3 = KoGa3ChoiceTextOFF

default ZoePeek = "{color=#0f0}[Zoe Peek]"
default OscarSixModText1 = " [Coral points >= 3 recommended]"
default Leanne_raw = "{color=#0f0}[Leanne raw]"


define KoGa3Color1 = "#c4aead"     #{color=#c4aead}     {/color}
define KoGa3Color2 = "#ffffff"     #{color=#ffffff}     {/color}
