screen UI_Menu_Options():
    frame:
        background None
        xpadding 0
        ypadding 0
        xsize 620
        ysize 1080
        #xpos 100
        add AlphaMask(
            Fixed(
                Transform("images/UI/CellphoneBG/"+str(cellbg[0])+".webp",
                    zoom = 0.9 + (cellwz/25),
                    xalign = (cellwx/100),
                    yalign = (cellwy/100)),
                    xysize=(620, 1080)  # Size of the masked area
            ),
            "images/UI/CellphoneBG/Menu_Mask_2.webp"
        )
        add "images/UI/CellphoneBG/Menu_FG.webp"
        vbox:
            xalign 0.5
            yalign 0.125
            spacing 25
            vbox:
                xalign 0.5
                text "Day [gametimeday], [gametimeclock]" size 60
            vbox:
                xalign 0.5
                text "[fnamehero] [lnamehero]" size 30
        vpgrid:
            spacing 25
            cols 3
            xalign 0.5
            yalign 0.5
            imagebutton:
                idle "images/UI/SUBMENU_Option_Gallery.webp"
                hover "images/UI/SUBMENU_Option_Gallery.webp"
                action Jump("UI_Menu_Options_Gallery")
            imagebutton:
                idle "images/UI/SUBMENU_Option_Music.webp"
                hover "images/UI/SUBMENU_Option_Music.webp"
                action Jump("UI_Menu_Options_Music")
            imagebutton:
                idle "images/UI/SUBMENU_Option_Contacts.webp"
                hover "images/UI/SUBMENU_Option_Contacts.webp"
                action Jump("UI_Menu_Options_Contacts")
            imagebutton:
                idle "images/UI/SUBMENU_Option_Study.webp"
                hover "images/UI/SUBMENU_Option_Study.webp"
                action Jump("UI_Menu_Options_Skill")
            imagebutton:
                idle "images/UI/SUBMENU_Option_Code.webp"
                hover "images/UI/SUBMENU_Option_Code.webp"
                action Jump("inputcheat")
            imagebutton:
                idle "images/UI/SUBMENU_Option_Code.webp"
                hover "images/UI/SUBMENU_Option_Code.webp"
                action Jump("wolfitdm_inputcheat")
            imagebutton:
                idle "images/UI/SUBMENU_Option_KCC.webp"
                hover "images/UI/SUBMENU_Option_KCC.webp"
                action Jump("UI_Menu_Options_KCC")
        hbox:
            xalign 0.5
            yalign 0.9
            spacing 50
            imagebutton:
                idle "images/UI/SUBMENU_Option_BottomTriangle IDLE.webp"
                hover "images/UI/SUBMENU_Option_BottomTriangle HOVER.webp"
                action Jump("show_ui")
            imagebutton:
                idle "images/UI/SUBMENU_Option_BottomCircle IDLE.webp"
                hover "images/UI/SUBMENU_Option_BottomCircle HOVER.webp"
                action Jump("show_ui")
            imagebutton:
                idle "images/UI/SUBMENU_Option_BottomSquare IDLE.webp"
                hover "images/UI/SUBMENU_Option_BottomSquare HOVER.webp"
                action Jump("show_ui")

label wolfitdm_inputcheat:
    $ cheatvar = renpy.input("Input a code. Don't know how to use codes? then type [C_Dat]guide[C_Off]", length=12)

    python:
        givemeall = "givemeall"
        kcc_code = "DpBnD"
        codecheat = "Taj0T"
        codecheat2 = "TajOT"
        outfits = "outfits"
        kawaii = "kawaii"
        show_code = "show"
        gettheme = "gettheme"
        guide = "guide"
        guide2 = "Guide"
        guide3 = "GUIDE"
        changeimg = "changeimg"

        cheat_codes = [givemeall,kcc_code,codecheat,codecheat2,outfits,kawaii,show_code,gettheme,guide,guide2,guide3,changeimg]

        if cheatvar == givemeall:

           stat_cha += 500
           stat_int += 500
           stat_phy += 500
           perk += 500
           money += 10000
           Char_Data["hero"]["stat"]["int"] += 500
           Char_Data["hero"]["stat"]["cha"] += 500
           Char_Data["hero"]["stat"]["phy"] += 500
           Char_Data["hero"]["stat"]["ene"] += 500
           Char_Data["hero"]["stat"]["hyg"] += 500
           Char_Data["hero"]["stat"]["eat"] += 500
           Char_Data["hero"]["stat"]["lust"] += 500
           Char_Data["hero"]["stat"]["money"] += 10000
           msg.msg("500 charisma added")
           msg.msg("500 Intelligence added")
           msg.msg("500 Physics added")
           msg.msg("500 Perks added")
           msg.msg("10000 money added")

        elif cheatvar == outfits:

           for i in ["hero", "hriv", "hprv", "hine", "wsis", "wnei", "wmom", "wgma", "wcou", "wpre", "wgal", "wota", "wdis", "wric", "wuza", "wlaz", "wdel", "wgot", "wdan", "wkuu", "wrin", "wsuk"]:
               for j in ["home", "under", "sleep", "casual", "dressy", "formal", "sport", "swim", "school", "school_swim", "school_sport", "work", "soap"]:
                   if j not in Char_Data[i]["achiev"]["wear"]:
                      Char_Data[i]["achiev"]["wear"].append(j)

           for i in ["hero"]:
               if "my_kawaii_character" in Char_Data[i]["achiev"]["wear"]:
                   Char_Data[i]["achiev"]["wear"].remove("my_kawaii_character")

               for j in ["home", "under", "sleep", "casual", "dressy", "formal", "sport", "swim", "school", "school_swim", "school_sport", "work", "soap"]:
                   j = "kawaii_" + j
                   if j not in Char_Data[i]["achiev"]["wear"]:
                      Char_Data[i]["achiev"]["wear"].append(j)

           msg.msg("All outfits added")

        elif cheatvar == kawaii:

           if "my_kawaii_character" in Char_Data[i]["achiev"]["wear"]:
              Char_Data[i]["achiev"]["wear"].remove("my_kawaii_character")
   
           for i in ["hero"]:
               for j in ["home", "under", "sleep", "casual", "dressy", "formal", "sport", "swim", "school", "school_swim", "school_sport", "work", "soap"]:
                   j = "kawaii_" + j
                   if j not in Char_Data[i]["achiev"]["wear"]:
                      Char_Data[i]["achiev"]["wear"].append(j)

           msg.msg("kawaii outfit added")

        elif cheatvar == show_code:

           msg.msg("Give Me All code: givemeall")
           msg.msg("kawaii outfit: kawaii")
           msg.msg("All outfits code: outfits")
           msg.msg("Show All Codes: show")
           msg.msg("guide code: guide")
           msg.msg("kawaii code editor code (kcc_code): [kcc_code]")
           msg.msg("cheat mode code: [codecheat]")
           msg.msg("events code: gettheme")
           msg.msg("more images code: changeimg")

    if not cheatvar in cheat_codes:
       play SE1 "BeepWrong.ogg"
       $ msg.msg("No code was found")
       $ cheatvar = ""

    if cheatvar == guide or cheatvar == guide2 or cheatvar == guide3:
        jump UI_Menu_Guide_Code
    
    if cheatvar == codecheat or cheatvar == codecheat2:
        if preferences.cheatmode == False:
            play SE1 "BeepRight.ogg"
            $ preferences.cheatmode = True
            $ preferences.codecheatuse = preferences.codecheat
            $ msg.msg("Cheat Enabled")
        else:
            play SE1 "BeepWrong.ogg"
            $ msg.msg("This code is already activated")

    elif cheatvar == gettheme:
        menu:
            "Common":
                $ preferences.gametimeevent = None
            "Halloween":
                $ preferences.gametimeevent = "Halloween"
            "Christmas":
                $ preferences.gametimeevent = "XMAS"

    elif cheatvar == kcc_code:
        if not "KCC1" in cellbg:
            play SE1 "BeepRight.ogg"
            $ cellbg.insert(1, "KCC6")
            $ cellbg.insert(1, "KCC5")
            $ cellbg.insert(1, "KCC4")
            $ cellbg.insert(1, "KCC3")
            $ cellbg.insert(1, "KCC2")
            $ cellbg.insert(1, "KCC1")
            $ msg.msg("New photos added to phone Gallery")
        else:
            play SE1 "BeepWrong.ogg"
            $ msg.msg("This code is already activated")

    elif cheatvar == changeimg:
        if ("KCC1" in cellbg or "KCC1AI" in cellbg):
            play SE1 "BeepRight.ogg"
            if "KCC1" in cellbg:
                $ cellbg[cellbg.index("KCC1")] = "KCC1AI"
                $ cellbg[cellbg.index("KCC2")] = "KCC2AI"
                $ cellbg[cellbg.index("KCC3")] = "KCC3AI"
                $ cellbg[cellbg.index("KCC4")] = "KCC4AI"
                $ cellbg[cellbg.index("KCC5")] = "KCC5AI"
                $ cellbg[cellbg.index("KCC6")] = "KCC6AI"
                $ msg.msg("Arts changed to AI generated images")
            elif "KCC1AI" in cellbg:
                $ cellbg[cellbg.index("KCC1AI")] = "KCC1"
                $ cellbg[cellbg.index("KCC2AI")] = "KCC2"
                $ cellbg[cellbg.index("KCC3AI")] = "KCC3"
                $ cellbg[cellbg.index("KCC4AI")] = "KCC4"
                $ cellbg[cellbg.index("KCC5AI")] = "KCC5"
                $ cellbg[cellbg.index("KCC6AI")] = "KCC6"
                $ msg.msg("AI generated images changed to arts")
        else:
            play SE1 "BeepWrong.ogg"
            $ msg.msg("You need to activate the KCC code first")

    jump UI_Menu_Options