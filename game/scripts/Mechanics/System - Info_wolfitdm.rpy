default check_playermap_var = False

default a_menu_1 = "none"
default a_menu_2 = "Any"
default a_menu_3 = ""
default a_menu_4 = 0
default a_menu_8 = 0

default cellbg = ["00"]

default incest_patch_on = True

default wolfitdm_image_hero = "HERO DEFAULT"
default wolfitdm_image_hero_style = "HERO STYLE DEFAULT"
default wolfitdm_hero_name = "hero"

default wolfitdm_image = "HERO DEFAULT"
default wolfitdm_image_style = "HERO STYLE DEFAULT"

default wolfitdm_full_nudist = False

default transform_incest_patch = False

default wolfitdm_hero_talk_gender = "brother"

default wolfitdm_hero_talk_gender_wsis = "Big Bro"

default wolfitdm_hero_talk_gender2 = "Brother"

default wolfitdm_hero_talk_gender_male = "brother"

default wolfitdm_hero_talk_gender_wsis_male = "Big Bro"

default wolfitdm_hero_talk_gender2_male = "Brother"

default wolfitdm_hero_talk_gender_female = "brother"

default wolfitdm_hero_talk_gender_wsis_female = "Big Sis"

default wolfitdm_hero_talk_gender2_female = "Sister"

default override_check_playermap_wolfitdm_inject = False

default wolfitdm_original_player_map = None

default wolfitdm_override_map = {}

default wolfitdm_cheat = False

default Char_Data = {}

init -9000 python:
    def rewrite_check_playermap_jumps():

        jump_check_playermap = "check_playermap_new"

        if check_playermap_var:
           jump_check_playermap = "check_playermap_new"
           config.label_overrides["check_playermap_original"] = "check_playermap"
           store.config.label_overrides["check_playermap_original"] = "check_playermap"
           config.label_overrides["check_playermap_override"] = "check_playermap_new"
           store.config.label_overrides["check_playermap_override"] = "check_playermap_new"
        else:
           jump_check_playermap = "check_playermap"
           config.label_overrides["check_playermap_original"] = "check_playermap"
           store.config.label_overrides["check_playermap_original"] = "check_playermap"
           config.label_overrides["check_playermap_override"] = "check_playermap"
           store.config.label_overrides["check_playermap_override"] = "check_playermap"

        if override_check_playermap_wolfitdm_inject:
           if renpy.has_label("wolfitdm_check_playermap"):
              jump_check_playermap = "wolfitdm_check_playermap"

        config.label_overrides["check_playermap"] = jump_check_playermap
        store.config.label_overrides["check_playermap"] = jump_check_playermap

    def get_incest_patch_on():
        return incest_patch_on

    def wolfitdm_change_gender(m2f, messagesoff):
        if m2f:
           transform_incest_patch = True
           store.transform_incest_patch = True
           wolfitdm_hero_talk_gender = wolfitdm_hero_talk_gender_female
           store.wolfitdm_hero_talk_gender = store.wolfitdm_hero_talk_gender_female
           wolfitdm_hero_talk_gender_wsis = wolfitdm_hero_talk_gender_wsis_female
           store.wolfitdm_hero_talk_gender_wsis = store.wolfitdm_hero_talk_gender_wsis_female
           wolfitdm_hero_talk_gender2 = wolfitdm_hero_talk_gender2_female
           store.wolfitdm_hero_talk_gender2 = store.wolfitdm_hero_talk_gender2_female
 
           if messagesoff:
              return

           msg.msg("change gender from male to female")
        else:
           transform_incest_patch = False
           store.transform_incest_patch = False
           wolfitdm_hero_talk_gender = wolfitdm_hero_talk_gender_male
           store.wolfitdm_hero_talk_gender = store.wolfitdm_hero_talk_gender_male
           wolfitdm_hero_talk_gender_wsis = wolfitdm_hero_talk_gender_wsis_male
           store.wolfitdm_hero_talk_gender_wsis = store.wolfitdm_hero_talk_gender_wsis_male
           wolfitdm_hero_talk_gender2 = wolfitdm_hero_talk_gender2_male
           store.wolfitdm_hero_talk_gender2 = store.wolfitdm_hero_talk_gender2_male

           if messagesoff:
              return

           msg.msg("change gender from female to male")

    def wolfitdm_change_gender_menu(messagesoff):
        menu_items = []

        menu_items.append(("male -> female", True))
        menu_items.append(("female -> male", False))
        
        choice = renpy.display_menu(menu_items)

        wolfitdm_change_gender(choice, messagesoff)

    def wolfitdm_change_gender_menu_new():
        renpy.invoke_in_new_context(wolfitdm_change_gender_menu, False)

    def wolfitdm_change_outfits_all_menu(messagesoff):
        menu_items = []

        for i in wear_get_clothes():
            menu_items.append((i, i))
        
        choice_cloth = renpy.display_menu(menu_items)

        for i in wear_get_chars():
            arr_var = WChar.gvar(i, "achiev_wear")
            for j in wear_get_clothes():
                if not j in arr_var:
                   arr_var.append(j)
                   WChar.svar(i, "achiev_wear", arr_var)

        for i in ["hero"]:
            arr_var = WChar.gvar(i, "achiev_wear")
            if "my_kawaii_character" in arr_var:
               arr_var.remove("my_kawaii_character")
               WChar.svar(i, "achiev_wear", arr_var)

            for j in wear_kawaii_get_clothes():
                if not j in arr_var:
                   arr_var.append(j)
                   WChar.svar(i, "achiev_wear", arr_var)

        for i in wear_get_chars():
            arr_var = WChar.gvar(i, "achiev_wear")
            for j, cloth in enumerate(arr_var):
                if cloth == choice_cloth:
                   set_wear_var(i, j)
                   continue

        if messagesoff:
           return
        
        msg.msg("change clothes from all chars to " + choice_cloth)

    def wolfitdm_change_outfits_all_menu_new():
        renpy.invoke_in_new_context(wolfitdm_change_outfits_all_menu, False)

    def wolfitdm_change_style(i):
        if i in wear_get_chars():
           if i == "hero":
              _wolfitdm_image = wolfitdm_image_hero
              _wolfitdm_image_style = wolfitdm_image_hero_style
           else:
              _wolfitdm_image = i.upper()
              _wolfitdm_image_style = _wolfitdm_image + " STYLE"

           wolfitdm_image, wolfitdm_image_style, wolfitdm_hero_name = (_wolfitdm_image, _wolfitdm_image_style, i)
      
           store.wolfitdm_image, store.wolfitdm_image_style, store.wolfitdm_hero_name = (_wolfitdm_image, _wolfitdm_image_style, i)

           msg.msg("Style changed to " + i)

    def wolfitdm_best_cheats(messagesoff):
        preferences.cheatmode = True
        preferences.codecheatuse = preferences.codecheat
        incest_patch_on = True
        check_playermap_var = True
        wolfitdm_full_nudist = True

        store.check_playermap_var, store.incest_patch_on, store.preferences.cheatmode, store.preferences.codecheatuse = (True, True, True, store.preferences.codecheat)

        store.wolfitdm_full_nudist = True

        rewrite_check_playermap_jumps()

        for i in wear_get_chars():
            arr_var = WChar.gvar(i, "achiev_wear")
            for j in wear_get_clothes():
                if j not in arr_var:
                   arr_var.append(j)

            WChar.svar(i, "achiev_wear", arr_var)

        for i in ["hero"]:
            arr_var = WChar.gvar(i, "achiev_wear")

            if "my_kawaii_character" in arr_var:
               arr_var.remove("my_kawaii_character")

            for j in wear_kawaii_get_clothes():
                if j not in arr_var:
                   arr_var.append(j)

            WChar.svar(i, "achiev_wear", arr_var)

        if not "KCC1" in cellbg:
           cellbg.insert(1, "KCC6")
           cellbg.insert(1, "KCC5")
           cellbg.insert(1, "KCC4")
           cellbg.insert(1, "KCC3")
           cellbg.insert(1, "KCC2")
           cellbg.insert(1, "KCC1")

        if messagesoff:
           return

        msg.msg("Incest Patch On")
        msg.msg("nudist/fullnudist on")
        msg.msg("kcc code executed")
        msg.msg("Cheat Mode Enabled")
        msg.msg("All Outfits added")
        msg.msg("Best Cheats Executed")

    def wolfitdm_give_me_all(messagesoff):
        for i in [stat_cha, stat_int, stat_phy, perk]:
            if i == None:
               continue

            if isinstance(i, int):
               i += 500
 
        for i in [money]:
            if i == None:
               continue

            if isinstance(i, int):
               i += 10000

        for i in wear_get_chars():
            WChar.inc_cheat_vars(i, 500, 10000)

        if messagesoff:
           return

        msg.msg("500 charisma to all chars added")
        msg.msg("500 Intelligence to all chars added")
        msg.msg("500 Physics to all chars added")
        msg.msg("500 Energy, Hygiene, Eat, Lust, Love added")
        msg.msg("500 Perks to all chars added")
        msg.msg("10000 money to all chars added")
        msg.msg("Give Me All Cheat Executed")

    def wolfitdm_cheat_menu(cheatvar,messagesoff):

        wolfitdm_return = False

        if cheatvar == "":
           cheatvar = "cheatmenu"

        givemeall = "givemeall"
        kcc_code = "DpBnD"
        codecheat = "Taj0T"
        codecheat2 = "TajOT"
        outfits = "outfits"
        kawaii = "kawaii"
        show_code = "show"
        show_code2 = "show2"
        gettheme = "gettheme"
        guide = "guide"
        guide2 = "Guide"
        guide3 = "GUIDE"
        changeimg = "changeimg"
        nudist = "nudist"
        nonudist = "nonudist"
        incest = "incest"
        noincest = "noincest"
        inceststatus = "inceststatus"
        nudiststatus = "nudiststatus"
        fullnudist = "fullnudist"
        nofullnudist = "nofullnudist"
        changestyle = "changestyle"
        best = "best"
        changegender = "changegender"
        changeoutfitsall = "changeoutfitsall"
        wolfitdm_cheats = "wolfitdm_cheat"

        cheat_codes = [givemeall,kcc_code,codecheat,codecheat2,outfits,kawaii,show_code,show_code2,gettheme,guide,guide2,guide3,changeimg,nudist,nonudist,incest,noincest,inceststatus,nudiststatus,changestyle,fullnudist,nofullnudist,best,changegender,changeoutfitsall,wolfitdm_cheats]

        if cheatvar == "cheatmenu":

           menu_items = []

           for i in cheat_codes:
               menu_items.append((i, i))

           menu_items.append(("Return (No Cheat Code Executed)", "nocode"))

           cheatvar = renpy.display_menu(menu_items)  

        if cheatvar == wolfitdm_cheats:

           if store.wolfitdm_cheat:
              store.wolfitdm_cheat = False
           else:
              store.wolfitdm_cheat = True

           if messagesoff:
              wolfitdm_return = True

           if not wolfitdm_return:
              if store.wolfitdm_cheat:
                 msg.msg("wolfitdm_cheat: on")
              else:
                 msg.msg("wolfitdm_cheat: off")

        elif cheatvar == changeoutfitsall:

           wolfitdm_change_outfits_all_menu(messagesoff)      

        elif cheatvar == changegender:
           
           wolfitdm_change_gender_menu(messagesoff)

        elif cheatvar == best:

           wolfitdm_best_cheats(messagesoff)

        elif cheatvar == givemeall:

           wolfitdm_give_me_all(messagesoff)

        elif cheatvar == outfits:
           for i in wear_get_chars():
               arr_var = WChar.gvar(i, "achiev_wear")
               for j in wear_get_clothes():
                   if not j in arr_var:
                      arr_var.append(j)

               WChar.svar(i, "achiev_wear", arr_var)

           for i in ["hero"]:
               arr_var = WChar.gvar(i, "achiev_wear")

               if "my_kawaii_character" in arr_var:
                  arr_var.remove("my_kawaii_character")

               for j in wear_kawaii_get_clothes():
                   if not j in arr_var:
                      arr_var.append(j)

               WChar.svar(i, "achiev_wear", arr_var)

           if messagesoff:
              wolfitdm_return = True

           if not wolfitdm_return:
              msg.msg("All outfits added")

        elif cheatvar == kawaii:   

           if not wear_all_chars_init:
              wear_get_chars()

           for i in ["hero"]:
               arr_var = WChar.gvar(i, "achiev_wear")

               if "my_kawaii_character" in arr_var:
                  arr_var.remove("my_kawaii_character")

               for j in wear_kawaii_get_clothes():
                   if not j in arr_var:
                      arr_var.append(j)

               WChar.svar(i, "achiev_wear", arr_var)

           if messagesoff:
              wolfitdm_return = True

           if not wolfitdm_return:
              msg.msg("kawaii outfit added")

        elif cheatvar == nudist:

           check_playermap_var = True
           store.check_playermap_var = True

           rewrite_check_playermap_jumps()

           if messagesoff:
              wolfitdm_return = True

           if not wolfitdm_return:
              msg.msg("clothes checks off")

        elif cheatvar == nonudist:

           check_playermap_var = False
           store.check_playermap_var = False

           rewrite_check_playermap_jumps()

           if messagesoff:
              wolfitdm_return = True

           if not wolfitdm_return:
              msg.msg("clothes checks off")

        elif cheatvar == incest:

           incest_patch_on = True
           store.incest_patch_on = True

           if messagesoff:
              wolfitdm_return = True

           if not wolfitdm_return:
              msg.msg("incest on")

        elif cheatvar == noincest:

           incest_patch_on = False
           store.incest_patch_on = False

           if messagesoff:
              wolfitdm_return = True

           if not wolfitdm_return:
              msg.msg("incest off")

        elif cheatvar == fullnudist:

           wolfitdm_full_nudist = True
           store.wolfitdm_full_nudist = True

           if messagesoff:
              wolfitdm_return = True

           if not wolfitdm_return:
              msg.msg("fullnudist on")

        elif cheatvar == nofullnudist:

           wolfitdm_full_nudist = False
           store.wolfitdm_full_nudist = False

           if messagesoff:
              wolfitdm_return = True

           if not wolfitdm_return:
              msg.msg("fullnudist off")

        elif cheatvar == show_code:

           if messagesoff:
              wolfitdm_return = True

           if not wolfitdm_return:

              msg.msg("Give Me All code: givemeall")
              msg.msg("kawaii outfit: kawaii")
              msg.msg("All outfits code: outfits")
              msg.msg("Change Style: changestyle")
              msg.msg("fullnudist: fullnudist on")
              msg.msg("nofullnudist: fullnudist off")
              msg.msg("changegender: change gender")
              msg.msg("cheatmenu: cheat menu")
              msg.msg("changeall: change all")
              msg.msg("guide code: guide")
              msg.msg("kawaii code editor code (kcc_code): [kcc_code]")
              msg.msg("Show All Codes 1: show")
              msg.msg("Show All Codes 2: show2")

        elif cheatvar == show_code2:

           if messagesoff:
              wolfitdm_return = True

           if not wolfitdm_return:

              msg.msg("cheat mode code: [codecheat]")
              msg.msg("cheat mode code: [codecheat2]")
              msg.msg("events code: gettheme")
              msg.msg("more images code: changeimg")
              msg.msg("clothes checks off code: nudist")
              msg.msg("clothes checks on code: nonudist")
              msg.msg("incest on code: incest")
              msg.msg("noincest: noincest")
              msg.msg("best: nudist,outfits,kcc,incest,cheatmode")
              msg.msg("inceststatus: incest status")
              msg.msg("nudiststatus: nudist status")

        elif cheatvar == inceststatus:
           if messagesoff:
              wolfitdm_return = True

           if not wolfitdm_return:
              if get_incest_patch_on():
                 msg.msg("incest: on")
              else:
                 msg.msg("incest: off")

        elif cheatvar == nudiststatus:

           if messagesoff:
              wolfitdm_return = True

           if not wolfitdm_return:
              if check_playermap_var:
                 msg.msg("nudist: on")
              else:
                 msg.msg("nudist: off")

              if wolfitdm_full_nudist:
                 msg.msg("fullnudist: on")
              else:
                 msg.msg("fullnudist: off")

        elif cheatvar == guide or cheatvar == guide2 or cheatvar == guide3:

            if messagesoff:
               return

            renpy.jump("UI_Menu_Guide_Code")

        elif cheatvar == codecheat or cheatvar == codecheat2:

            if preferences.cheatmode == False:

               preferences.cheatmode = True
               preferences.codecheatuse = preferences.codecheat

               if messagesoff:
                  return

               msg.msg("Cheat Enabled")

            else:

               if messagesoff:
                  return

               msg.msg("This code is already activated")

        elif cheatvar == gettheme:

            if messagesoff:
               return

            menu_items = []

            for i in ["Common", "Halloween", "Christmas"]:

                if i == "Christmas":
                   menu_items.append((i, "XMAS"))
                else:
                   menu_items.append((i, i))

            choice = renpy.display_menu(menu_items)

            if choice == "Common":
               choice = None

            preferences.gametimeevent = choice
            store.preferences.gametimeevent = choice

        elif cheatvar == changestyle:

            if messagesoff:
               return

            menu_items = []

            for i in wear_get_chars():
                if i == "hero":
                   _wolfitdm_menu_entry = "DEFAULT: "
                else:
                   _wolfitdm_menu_entry = i.upper() + ": "
                
                fname, lname = WChar.get_name(i)                  

                _wolfitdm_menu_entry = _wolfitdm_menu_entry + fname + " " + lname

                menu_items.append((_wolfitdm_menu_entry, i))

            choice = renpy.display_menu(menu_items)

            wolfitdm_change_style(choice)

        elif cheatvar == kcc_code:

            if not "KCC1" in cellbg:
               cellbg.insert(1, "KCC6")
               cellbg.insert(1, "KCC5")
               cellbg.insert(1, "KCC4")
               cellbg.insert(1, "KCC3")
               cellbg.insert(1, "KCC2")
               cellbg.insert(1, "KCC1")

               if messagesoff:
                  return

               msg.msg("New photos added to phone Gallery")

            else:

               if messagesoff:
                  return

               msg.msg("This code is already activated")

        elif cheatvar == changeimg:

            if ("KCC1" in cellbg or "KCC1AI" in cellbg):
               if "KCC1" in cellbg:
                  cellbg[cellbg.index("KCC1")] = "KCC1AI"
                  cellbg[cellbg.index("KCC2")] = "KCC2AI"
                  cellbg[cellbg.index("KCC3")] = "KCC3AI"
                  cellbg[cellbg.index("KCC4")] = "KCC4AI"
                  cellbg[cellbg.index("KCC5")] = "KCC5AI"
                  cellbg[cellbg.index("KCC6")] = "KCC6AI"
           
                  if messagesoff:
                     return

                  msg.msg("Arts changed to AI generated images")
               elif "KCC1AI" in cellbg:
                  cellbg[cellbg.index("KCC1AI")] = "KCC1"
                  cellbg[cellbg.index("KCC2AI")] = "KCC2"
                  cellbg[cellbg.index("KCC3AI")] = "KCC3"
                  cellbg[cellbg.index("KCC4AI")] = "KCC4"
                  cellbg[cellbg.index("KCC5AI")] = "KCC5"
                  cellbg[cellbg.index("KCC6AI")] = "KCC6"

                  if messagesoff:
                     return

                  msg.msg("AI generated images changed to arts")
            else:

               if messagesoff:
                  return

               msg.msg("You need to activate the KCC code first")
        else:
            if messagesoff:
               return

            msg.msg("No code was found")

        return

    def wolfitdm_cheat_menu_new():
        renpy.invoke_in_new_context(wolfitdm_cheat_menu, "cheatmenu", False)

    def wolfitdm_incest_off():
        incest_patch_on = False
        store.incest_patch_on = False
        msg.msg("Incest Patch Off")

    def wolfitdm_nudist_off():
        check_playermap_var = False
        store.check_playermap_var = False
        wolfitdm_full_nudist = False
        store.wolfitdm_full_nudist = False
        rewrite_check_playermap_jumps()
        msg.msg("nudist/fullnudist off")

    def wolfitdm_map_check(i):
        if i == None:
           return False

        if i in wear_get_chars():
           if not WChar.get_old_version():
              return True

           if i in Char_Data and "map" in Char_Data[i]:
              if "hero" in Char_Data and "map" in Char_Data["hero"]:
                 return True

        return False

    wolfitdm_original_maps = {} 

    def wolfitdm_change_map_to_me(i):

        if i == "none" or i == "hero":

           del_keys = []

           if "hero" in wolfitdm_original_maps:
              wolfitdm_original_player_map = wolfitdm_original_maps["hero"]
              store.wolfitdm_original_player_map = wolfitdm_original_maps["hero"]

           for key in wolfitdm_original_maps:

               wolfitdm_override_map[key] = None
               store.wolfitdm_override_map[key] = None
               WChar.svar(key, "map", wolfitdm_original_maps[key])
               msg.msg("change map from " + key + " to " +  wolfitdm_original_maps[key])
               del_keys.append(key)

           for key in del_keys:

               del wolfitdm_original_maps[key]

           override_check_playermap_wolfitdm_inject = False
           store.override_check_playermap_wolfitdm_inject = False

           return

        if wolfitdm_map_check(i):

           if not "hero" in wolfitdm_original_maps:
              wolfitdm_original_maps["hero"] = WChar.gvar("hero", "map")

           if "hero" in wolfitdm_original_maps:
              wolfitdm_original_player_map = wolfitdm_original_maps["hero"]
              store.wolfitdm_original_player_map = wolfitdm_original_maps["hero"]

           map = WChar.gvar(i, "map")

           if map == None:
              return

           WChar.svar("hero", "map", map)

           if not map in wolfitdm_get_maps():
              override_check_playermap_wolfitdm_inject = True
              store.override_check_playermap_wolfitdm_inject = True

           msg.msg("change map to " + map)

           if renpy.has_label("hide_ui"):
              renpy.jump("hide_ui")

           if renpy.has_label("show_ui"):
              renpy.jump("show_ui")

        return

    wolfitdm_original_maps = {}

    def wolfitdm_change_map_to_him(i):

        global wolfitdm_original_maps 

        if i == "none" or i == "hero":

           del_keys = []

           if "hero" in wolfitdm_original_maps:
              wolfitdm_original_player_map = wolfitdm_original_maps["hero"]
              store.wolfitdm_original_player_map = wolfitdm_original_maps["hero"]

           for key in wolfitdm_original_maps:

               wolfitdm_override_map[key] = None
               store.wolfitdm_override_map[key] = None
               WChar.svar(key, "map", wolfitdm_original_maps[key])
               msg.msg("change map from " + key + " to " +  wolfitdm_original_maps[key])

           for key in del_keys:
               del wolfitdm_original_maps[key]

           override_check_playermap_wolfitdm_inject = False
           store.override_check_playermap_wolfitdm_inject = False

           if renpy.has_label("hide_ui"):
              renpy.jump("hide_ui")

           if renpy.has_label("show_ui"):
              renpy.jump("show_ui")

           return

        if wolfitdm_map_check(i):
           if not "hero" in wolfitdm_original_maps:
              wolfitdm_original_maps["hero"] = WChar.gvar("hero", "map")

           if "hero" in wolfitdm_original_maps:
              wolfitdm_original_player_map = wolfitdm_original_maps["hero"]
              store.wolfitdm_original_player_map = wolfitdm_original_maps["hero"]

           if not i in wolfitdm_original_maps:
              wolfitdm_original_maps[i] = WChar.gvar(i, "map")

           map = WChar.gvar("hero", "map")

           if map == None:
              return

           wolfitdm_override_map[i] = map
           store.wolfitdm_override_map[i] = map

           WChar.svar(i, "map", map)

           if not map in wolfitdm_get_maps():
              override_check_playermap_wolfitdm_inject = True
              store.override_check_playermap_wolfitdm_inject = True

           msg.msg("change map from " + i + " to " + map)

           if renpy.has_label("hide_ui"):
              renpy.jump("hide_ui")

           if renpy.has_label("show_ui"):
              renpy.jump("show_ui")

        return

    def wolfitdm_get_maps():
        wolfitdm_maps = []

        wolfitdm_maps.append(Map_Data["city"]["name"])
        wolfitdm_maps.append(Map_Data["home"]["name"] + " - " + Map_Data["home"]["map"]["facade"]["name"])
        wolfitdm_maps.append(Map_Data["home"]["name"] + " - " + Map_Data["home"]["map"]["living_room"]["name"])
        wolfitdm_maps.append(Map_Data["home"]["name"] + " - " + Map_Data["home"]["map"]["hallway"]["name"])
        wolfitdm_maps.append(Map_Data["home"]["name"] + " - " + Map_Data["home"]["map"]["bedroom_hero"]["name"])
        wolfitdm_maps.append(Map_Data["home"]["name"] + " - " + Map_Data["home"]["map"]["bedroom_wsis"]["name"])
        wolfitdm_maps.append(Map_Data["home"]["name"] + " - " + Map_Data["home"]["map"]["bedroom_wmom"]["name"])
        wolfitdm_maps.append(Map_Data["home"]["name"] + " - " + Map_Data["home"]["map"]["bathroom"]["name"])
        wolfitdm_maps.append(Map_Data["office"]["name"] + " - " + Map_Data["office"]["map"]["facade"]["name"])
        wolfitdm_maps.append(Map_Data["office"]["name"] + " - " + Map_Data["office"]["map"]["office_wcou"]["name"])
        wolfitdm_maps.append(Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["facade"]["name"])
        wolfitdm_maps.append(Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["courtyard"]["name"])
        wolfitdm_maps.append(Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["frontyard"]["name"])
        wolfitdm_maps.append(Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["locker_m"]["name"])
        wolfitdm_maps.append(Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["hallway_1"]["name"])
        wolfitdm_maps.append(Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["hallway_2"]["name"])
        wolfitdm_maps.append(Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["class_1a"]["name"])
        wolfitdm_maps.append(Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["class_1b"]["name"])
        wolfitdm_maps.append(Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["class_3a"]["name"])
        wolfitdm_maps.append(Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["library"]["name"])
        wolfitdm_maps.append(Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["swimming_pool"]["name"])
        wolfitdm_maps.append(Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["sports_court"]["name"])
        wolfitdm_maps.append(Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["club_coun"]["name"])

        return wolfitdm_maps

    def wolfitdm_map_menu():
        menu_items = []
        for i in wolfitdm_get_maps():
            menu_items.append((i,i))

        choice = renpy.display_menu(menu_items)

        WChar.svar("hero", "map", choice)

        if renpy.has_label("hide_ui"):
           renpy.jump("hide_ui")

        if renpy.has_label("show_ui"):
           renpy.jump("show_ui")

        return

    def wolfitdm_map_menu_new():
        renpy.invoke_in_new_context(wolfitdm_map_menu)

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
                idle "images/UI/SUBMENU_Option_Map.png"
                hover "images/UI/SUBMENU_Option_Map.png"
                action Function(wolfitdm_map_menu_new)
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
                       if hasattr(store, f"fname{a_menu_1}") and hasattr(store, "lnamestep"):
                          label str(getattr(store, f"fname{a_menu_1}") + " [lnamestep]") xalign 0.5
                       else:
                          label "UNKNOWN UNKNOWN" xalign 0.5
                    elif a_menu_1 in ["wcou", "wgma", "waun"]:
                       if hasattr(store, f"fname{a_menu_1}") and hasattr(store, "lnamerela"):
                          label str(getattr(store, f"fname{a_menu_1}") + " [lnamerela]") xalign 0.5
                       else:
                          label "UNKNOWN UNKNOWN" xalign 0.5
                    elif a_menu_1 in ["wmam", "hpap"]:
                       if hasattr(store, f"fname{a_menu_1}") and hasattr(store, "lnamewnei"):
                          label str(getattr(store, f"fname{a_menu_1}") + " [lnamewnei]") xalign 0.5
                       else:
                          label "UNKNOWN UNKNOWN" xalign 0.5
                    else:
                       if hasattr(store, f"fname{a_menu_1}") and hasattr(store, f"lname{a_menu_1}"):
                          label str(getattr(store, f"fname{a_menu_1}") + " " + getattr(store, f"lname{a_menu_1}")) xalign 0.5
                       else:
                          label "UNKNOWN UNKNOWN" xalign 0.5                       
                    hbox:
                        xalign 0.5
                        if len(WChar.gvar(a_menu_1, "achiev_wear")) >= 2:
                            textbutton "{size=60}◀{/size}" action [SetVariable("a_menu_8", (a_menu_8 - 1) % max(1, len(WChar.gvar(a_menu_1, "achiev_wear")))), Function(set_wear_var, a_menu_1, a_menu_8)]
                        else:
                            textbutton "{size=60}◀{/size}" action None
                        text "{size=60} Style {/size}"
                        if len(WChar.gvar(a_menu_1, "achiev_wear")) >= 2:
                            textbutton "{size=60}▶{/size}" action [SetVariable("a_menu_8", (a_menu_8 + 1) % max(1, len(WChar.gvar(a_menu_1, "achiev_wear")))), Function(set_wear_var, a_menu_1, a_menu_8)]
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
                    idle "images/UI/SUBMENU_Option_BottomTriangleMapIdle.png"
                    hover "images/UI/SUBMENU_Option_BottomTriangleMapHover.png"
                    action Function(wolfitdm_change_map_to_him, a_menu_1)
                imagebutton:
                    idle "images/UI/SUBMENU_Option_BottomCircle IDLE.webp"
                    hover "images/UI/SUBMENU_Option_BottomCircle HOVER.webp"
                    action Jump("show_ui")
                imagebutton:
                    idle "images/UI/SUBMENU_Option_BottomSquareMapIdle.png"
                    hover "images/UI/SUBMENU_Option_BottomSquareMapHover.png"
                    action Function(wolfitdm_change_map_to_me, a_menu_1)

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
                        imagebutton:
                            idle At("images/UI/SUBMENU_Option_Cheats.png", ButtonIdle)
                            hover At("images/UI/SUBMENU_Option_Cheats.png", ButtonHover)
                            action [Function(wolfitdm_cheat_menu_new)]

                        imagebutton:
                            idle At("images/UI/SUBMENU_Option_Gender.png", ButtonIdle)
                            hover At("images/UI/SUBMENU_Option_Gender.png", ButtonHover)
                            action [Function(wolfitdm_change_gender_menu_new)]

                        imagebutton:
                            idle At("images/UI/SUBMENU_Option_ChangeOutfitsAll.png", ButtonIdle)
                            hover At("images/UI/SUBMENU_Option_ChangeOutfitsAll.png", ButtonHover)
                            action [Function(wolfitdm_change_outfits_all_menu_new)]

                        if True:
                            if gametimeday >= 2:
                                imagebutton:
                                    idle At("images/UI/OC_NONE.webp", ButtonIdle)
                                    hover At("images/UI/OC_NONE.webp", ButtonHover)
                                    action [SetVariable("a_menu_1", "none"), SetVariable("a_menu_8", 0)]

                        for i in wear_get_chars():
                            imagebutton:
                                idle At("images/UI/OC_" + i.upper() +".webp", ButtonIdle)
                                hover At("images/UI/OC_" + i.upper() +".webp", ButtonHover)
                                action [SetVariable("a_menu_1", i), SetVariable("a_menu_8", 0)]

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
                            idle At("images/UI/SUBMENU_Option_Change_Avatar.png", ButtonIdle)
                            hover At("images/UI/SUBMENU_Option_Change_Avatar.png", ButtonHover)
                            action Function(wolfitdm_change_style, a_menu_1)
                        imagebutton:
                            idle At("images/UI/SUBMENU_Option_Best_Cheats.png", ButtonIdle)
                            hover At("images/UI/SUBMENU_Option_Best_Cheats.png", ButtonHover)
                            action Function(wolfitdm_best_cheats, False)
                        imagebutton:
                            idle At("images/UI/SUBMENU_Option_GiveMeAll.png", ButtonIdle)
                            hover At("images/UI/SUBMENU_Option_GiveMeAll.png", ButtonHover)
                            action Function(wolfitdm_give_me_all, False)
                        imagebutton:
                            idle At("images/UI/SUBMENU_Option_IncestOff.png", ButtonIdle)
                            hover At("images/UI/SUBMENU_Option_IncestOff.png", ButtonHover)
                            action Function(wolfitdm_incest_off)
                        imagebutton:
                            idle At("images/UI/SUBMENU_Option_NudistOff.png", ButtonIdle)
                            hover At("images/UI/SUBMENU_Option_NudistOff.png", ButtonHover)
                            action Function(wolfitdm_nudist_off)

                    vbox:
                        xalign 0.5
                        yalign 0.0
                        spacing 10

                        if True:
                            side ("c r"):
                                area (25, 0, 1000, 850)
                                viewport id "ScrollOCData":
                                    draggable True mousewheel True xoffset -10
                                    vbox:
                                        spacing 10
                                        if not a_menu_1 in ["none"]: 
                                           text "{b}Name:{/b} " + str(a_menu_1)
                                           text "{b}Map:{/b} " + str(WChar.gvar(a_menu_1, "map"))
                                           text "{b}Wear:{/b} " + str(WChar.gvar(a_menu_1, "wear"))
                                           if a_menu_1 == "hero":
                                              if transform_incest_patch:
                                                 text "{b}Gender:{/b} Female"
                                              else:
                                                 text "{b}Gender:{/b} Male"

                                              if hasattr(preferences, "codecheat"):
                                                 text "Codecheat: [preferences.codecheat]"

                                           if a_menu_1 == "hero" and wolfitdm_cheat:
                                              label "{image=icon_hero} [C_Nam][fnamehero][C_Off]"
                                              hbox:
                                                  spacing 10
                                                  text "{image=images/UI/ICON_StatInt.webp}"
                                                  if config.version == "0.36.1":
                                                     bar value DictValue(Char_Data["hero"]["stat"], "int", 100) xmaximum 300
                                                     text str(Char_Data["hero"]["stat"]["int"]) + "%"
                                                  else:
                                                     bar value VariableValue("stat_int", 100) xmaximum 300
                                                     text str(stat_int) + "%"
                                              hbox:
                                                  spacing 10
                                                  text "{image=images/UI/ICON_StatCha.webp}"
                                                  if config.version == "0.36.1":
                                                     bar value DictValue(Char_Data["hero"]["stat"], "cha", 100) xmaximum 300
                                                     text str(Char_Data["hero"]["stat"]["cha"]) + "%"
                                                  else:
                                                     bar value VariableValue("stat_cha", 100) xmaximum 300
                                                     text str(stat_cha) + "%"
                                              hbox:
                                                  spacing 10
                                                  text "{image=images/UI/ICON_StatPhy.webp}"
                                                  if config.version == "0.36.1":
                                                     bar value DictValue(Char_Data["hero"]["stat"], "phy", 100) xmaximum 300
                                                     text str(Char_Data["hero"]["stat"]["phy"]) + "%"
                                                  else:
                                                     bar value VariableValue("stat_phy", 100) xmaximum 300
                                                     text str(stat_phy) + "%"
                                              if config.version == "0.36.1":
                                                 textbutton "Money: "+str(round(Char_Data["hero"]["stat"]["money"], 2)) action SetDict(Char_Data["hero"]["stat"], "money", math.inf)
                                                 textbutton "Perks: [perk]" action SetVariable("perk", math.inf)
                                              else:
                                                 textbutton "Money: "+str(round(money, 2)) action SetVariable("money", math.inf)
                                                 textbutton "Perks: [perk]" action SetVariable("perk", math.inf)
                                              text ""
                                           elif wolfitdm_cheat:
                                              for i in [a_menu_1]:
                                                  $ label_str = "{image=icon_" + i + "} [C_Nam][fname" + i + "][C_Off]"
                                                  label str(label_str)
                                                  hbox:
                                                      spacing 10
                                                      text "{image=images/UI/ICON_StatInti.webp}"
                                                      if config.version == "0.36.1":
                                                         bar value DictValue(Char_Data[i]["stat"], "inti", 100) xmaximum 300
                                                         text str(Char_Data[i]["stat"]["inti"]) + "%"
                                                      else:
                                                         bar value VariableValue(i + "_inti", 100) xmaximum 300
                                                         text str(getattr(store,i+"_inti")) + "%"
                                                  hbox:
                                                      spacing 10
                                                      text "{image=images/UI/ICON_StatLove.webp}"
                                                      if config.version == "0.36.1":
                                                         bar value DictValue(Char_Data[i]["stat"], "love", 100) xmaximum 300
                                                         text str(Char_Data[i]["stat"]["love"]) + "%"
                                                      else:
                                                         bar value VariableValue(i + "_love", 100) xmaximum 300
                                                         text str(getattr(store,i+"_love")) + "%"
                                                  hbox:
                                                      spacing 10
                                                      text "{image=images/UI/ICON_StatLust.webp}"
                                                      if config.version == "0.36.1":
                                                         bar value DictValue(Char_Data[i]["stat"], "lust", 100) xmaximum 300
                                                         text str(Char_Data[i]["stat"]["love"]) + "%"
                                                      else:
                                                         bar value VariableValue(i + "_lust", 100) xmaximum 300
                                                         text str(getattr(store,i+"_lust")) + "%"
                                                  hbox:
                                                      spacing 10
                                                      text "{image=images/UI/ICON_StatInt.webp}"
                                                      if config.version == "0.36.1":
                                                         bar value DictValue(Char_Data[i]["stat"], "int", 100) xmaximum 300
                                                         text str(Char_Data[i]["stat"]["int"]) + "%"
                                                      else:
                                                         bar value VariableValue(i + "_int", 100) xmaximum 300
                                                         text str(getattr(store,i+"_int")) + "%"
                                                  hbox:
                                                      spacing 10
                                                      text "{image=images/UI/ICON_StatCha.webp}"
                                                      if config.version == "0.36.1":
                                                         bar value DictValue(Char_Data[i]["stat"], "cha", 100) xmaximum 300
                                                         text str(Char_Data[i]["stat"]["cha"]) + "%"
                                                      else:
                                                         bar value VariableValue(i + "_cha", 100) xmaximum 300
                                                         text str(getattr(store,i+"_cha")) + "%"
                                                  hbox:
                                                      spacing 10
                                                      text "{image=images/UI/ICON_StatPhy.webp}"
                                                      if config.version == "0.36.1":
                                                         bar value DictValue(Char_Data[i]["stat"], "phy", 100) xmaximum 300
                                                         text str(Char_Data[i]["stat"]["phy"]) + "%"
                                                      else:
                                                         bar value VariableValue(i + "_phy", 100) xmaximum 300
                                                         text str(getattr(store,i+"_phy")) + "%"
                                                  hbox:
                                                      spacing 10
                                                      text "{image=images/UI/ICON_StatHyg.webp}"
                                                      if config.version == "0.36.1":
                                                         bar value DictValue(Char_Data[i]["stat"], "hyg", 100) xmaximum 300
                                                         text str(Char_Data[i]["stat"]["hyg"]) + "%"
                                                      else:
                                                         bar value VariableValue(i + "_hyg", 100) xmaximum 300
                                                         text str(getattr(store,i+"_hyg")) + "%"
                                                  hbox:
                                                      spacing 10
                                                      text "{image=images/UI/ICON_StatPer.webp}"
                                                      if config.version == "0.36.1":
                                                         bar value DictValue(Char_Data[i]["stat"], "eat", 100) xmaximum 300
                                                         text str(Char_Data[i]["stat"]["eat"]) + "%"
                                                      else:
                                                         bar value VariableValue(i + "_eat", 100) xmaximum 300
                                                         text str(getattr(store,i+"_eat")) + "%"
                                                  hbox:
                                                      spacing 10
                                                      text "{image=images/UI/ICON_StatEne.webp}"
                                                      if config.version == "0.36.1":
                                                         bar value DictValue(Char_Data[i]["stat"], "ene", 100) xmaximum 300
                                                         text str(Char_Data[i]["stat"]["ene"]) + "%"
                                                      else:
                                                         bar value VariableValue(i + "_ene", 100) xmaximum 300
                                                         text str(getattr(store,i+"_ene")) + "%"

                                                  if config.version == "0.36.1":
                                                     textbutton "Money: "+str(round(Char_Data[i]["stat"]["money"], 2)) action SetDict(Char_Data[i]["stat"], "money", math.inf)
                                                  else:
                                                     textbutton "Money: "+str(round(getattr(store, i+"_money"), 2)) action SetVariable(i+"_money", math.inf)
                                                  text ""
                                vbar value YScrollValue("ScrollOCData")


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

label wolfitdm_nav_map:
    show screen wolfitdm_nav_map

label wolfitdm_inputcheat:
    $ cheatvar = renpy.input("Input a code. To show all codes, type [C_Dat]cheatmenu[C_Off] or type nothing and press enter", length=12)

    $ wolfitdm_cheat_menu(cheatvar, False)

    jump UI_Menu_Options