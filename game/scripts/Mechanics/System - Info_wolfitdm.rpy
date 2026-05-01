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
                idle "images/UI/SUBMENU_Option_ContactsX.png"
                hover "images/UI/SUBMENU_Option_ContactsX.png"
                action Jump("UI_Menu_Options_Contacts_Redefine")
            imagebutton:
                idle "images/UI/SUBMENU_Option_Study.webp"
                hover "images/UI/SUBMENU_Option_Study.webp"
                action Jump("UI_Menu_Options_Skill")
            imagebutton:
                idle "images/UI/SUBMENU_Option_Code.webp"
                hover "images/UI/SUBMENU_Option_Code.webp"
                action Jump("inputcheat")
            imagebutton:
                idle "images/UI/SUBMENU_Option_CodeX.png"
                hover "images/UI/SUBMENU_Option_CodeX.png"
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

screen UI_Menu_Options_Contacts_Redefine():
    hbox:
        #xpos 100
        frame:
            background None
            xpadding 0
            ypadding 0
            xsize 620
            ysize 1080

            add AlphaMask(
                Fixed(
                    Transform("images/UI/CellphoneBG/"+str(cellbg[a_menu_3])+".webp",
                        zoom = 0.9 + (cellwz/25),
                        xalign = (cellwx/100),
                        yalign = (cellwy/100)),
                        xysize=(620, 1080)  # Size of the masked area
                ),
                "images/UI/CellphoneBG/Menu_Mask_2.webp"
            )

            add "images/UI/CellphoneBG/Menu_MG_2A.webp"

            if a_menu_1 != "none":
                image "[a_menu_1!u] STYLE":
                    xalign 0.5 yalign 0.0 zoom 0.75 xpos 312 ypos 100
            else:
                image AlphaMask(
                Fixed(
                    Transform("NONE",
                        xalign = 0.5,
                        yalign = 0.0,
                        zoom = 0.47,
                        xpos = 312,
                        ypos = 100),
                        xysize=(620, 1080)
                ),
                "images/UI/CellphoneBG/Menu_Mask_2.webp"
                )

            add "images/UI/CellphoneBG/Menu_MG_1.webp"

            if a_menu_1 != "none":
                vbox:
                    spacing 10 xalign 0.5 yalign 0.15
                    if a_menu_1 in ["wsis", "wmom"]:
                        label str(getattr(store, f"fname{a_menu_1}") + " [lnamestep]") xalign 0.5
                    elif a_menu_1 in ["wcou", "wgma", "waun"]:
                        label str(getattr(store, f"fname{a_menu_1}") + " [lnamerela]") xalign 0.5
                    else:
                        label str(getattr(store, f"fname{a_menu_1}") + " " + getattr(store, f"lname{a_menu_1}")) xalign 0.5
                    hbox:
                        xalign 0.5
                        if len(Char_Data[a_menu_1]["achiev"]["wear"]) >= 2:
                            textbutton "{size=60}◀{/size}" action [SetVariable("a_menu_8", (a_menu_8 - 1) % max(1, len(Char_Data[a_menu_1]["achiev"]["wear"]))), Function(set_wear_var, a_menu_1, a_menu_8)]
                        else:
                            textbutton "{size=60}◀{/size}" action None
                        text "{size=60} Style {/size}"
                        if len(Char_Data[a_menu_1]["achiev"]["wear"]) >= 2:
                            textbutton "{size=60}▶{/size}" action [SetVariable("a_menu_8", (a_menu_8 + 1) % max(1, len(Char_Data[a_menu_1]["achiev"]["wear"]))), Function(set_wear_var, a_menu_1, a_menu_8)]
                        else:
                            textbutton "{size=60}▶{/size}" action None
            else:
                vbox:
                    spacing 10 xalign 0.5 yalign 0.15
                    label "Select a Character" xalign 0.5 yalign 0.15
                    textbutton "{size=40}Style{/size}" action None xalign 0.5


            add "images/UI/CellphoneBG/Menu_FG.webp"
            
            hbox:
                xalign 0.5
                yalign 0.9
                spacing 50
                imagebutton:
                    idle "images/UI/SUBMENU_Option_BottomTriangle IDLE.webp"
                    hover "images/UI/SUBMENU_Option_BottomTriangle HOVER.webp"
                    action Jump("UI_Menu_Options_Triangle")
                imagebutton:
                    idle "images/UI/SUBMENU_Option_BottomCircle IDLE.webp"
                    hover "images/UI/SUBMENU_Option_BottomCircle HOVER.webp"
                    action Jump("show_ui")
                imagebutton:
                    idle "images/UI/SUBMENU_Option_BottomSquare IDLE.webp"
                    hover "images/UI/SUBMENU_Option_BottomSquare HOVER.webp"
                    action Jump("show_ui")

        frame:
            xysize(1200, 1080)
            xpadding 25
            ypadding 25
            hbox:
                spacing 50
                side ("c l"):
                    area (0, 0, 200, 1030)
                    vpgrid id "ScrollOCButton":
                        draggable True mousewheel True
                        xoffset 20
                        spacing 25
                        cols 1
                        if a_menu_2 in ["Any", 0]:
                            if gametimeday >= 2:
                                imagebutton:
                                    idle At("images/UI/OC_NONE.webp", ButtonIdle)
                                    hover At("images/UI/OC_NONE.webp", ButtonHover)
                                    action [SetVariable("a_menu_1", "none"), SetVariable("a_menu_8", 0)]
                            imagebutton:
                                idle At("images/UI/OC_HERO.webp", ButtonIdle)
                                hover At("images/UI/OC_HERO.webp", ButtonHover)
                                action [SetVariable("a_menu_1", "hero"), SetVariable("a_menu_8", 0)]
                        if a_menu_2 in ["Dateable", "Any"]:
                            imagebutton:
                                idle At("images/UI/OC_WMOM.webp", ButtonIdle)
                                hover At("images/UI/OC_WMOM.webp", ButtonHover)
                                action [SetVariable("a_menu_1", "wmom"), SetVariable("a_menu_8", 0)]
                            imagebutton:
                                idle At("images/UI/OC_WSIS.webp", ButtonIdle)
                                hover At("images/UI/OC_WSIS.webp", ButtonHover)
                                action [SetVariable("a_menu_1", "wsis"), SetVariable("a_menu_8", 0)]
                            imagebutton:
                                idle At("images/UI/OC_WNEI.webp", ButtonIdle)
                                hover At("images/UI/OC_WNEI.webp", ButtonHover)
                                action [SetVariable("a_menu_1", "wnei"), SetVariable("a_menu_8", 0)]
                    vbar value YScrollValue("ScrollOCButton")

                vbox:
                    xysize(850, 980)
                    xalign 0.5
                    yalign 0.0
                    spacing 50

                    hbox:
                        spacing 10
                        xalign 0.5
                        yalign 0.0
                        imagebutton:
                            idle At("images/UI/SUBMENU_Option_Stat.webp", ButtonIdle)
                            hover At("images/UI/SUBMENU_Option_Stat.webp", ButtonHover)
                            action SetVariable("a_menu_4", 0)
                        imagebutton:
                            idle At("images/UI/SUBMENU_Option_List.webp", ButtonIdle)
                            hover At("images/UI/SUBMENU_Option_List.webp", ButtonHover)
                            action SetVariable("a_menu_4", 1)
                        imagebutton:
                            idle At("images/UI/SUBMENU_Option_Quest.webp", ButtonIdle)
                            hover At("images/UI/SUBMENU_Option_Quest.webp", ButtonHover)
                            action SetVariable("a_menu_4", 2)
                        if persistent.debug == True or perk_int_obs >= 1:
                            imagebutton:
                                idle At("images/UI/QUICK_Time.webp", ButtonIdle)
                                hover At("images/UI/QUICK_Time.webp", ButtonHover)
                                action SetVariable("a_menu_4", 3)


label UI_Menu_Options_Contacts_Redefine:
    call gamecheck
    $ a_menu_1 = "none"
    $ a_menu_2 = "Any"
    $ a_menu_3 = 0
    $ a_menu_4 = 0
    $ a_menu_8 = 0
    call hide_ui
    call screen UI_Menu_Options_Contacts_Redefine
    jump show_ui

label wolfitdm_inputcheat:
    $ cheatvar = renpy.input("Input a code. To show all codes, type [C_Dat]show[C_Off] or type nothing and press enter", length=12)

    if cheatvar == "":
       $ cheatvar = "show"

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