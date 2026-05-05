init 90000 python:
    def wolfidtm_can_fuck(i):
        if i in wear_get_chars():
           if not renpy.has_label("wolfidtm_fuck_" + i):
              return False
           return True
        else:
           return False

    def wolfidtm_interact_fuck_action(i):
        if wolfidtm_can_fuck(i):
           renpy.jump("wolfidtm_fuck_"+i)

        return

label wolfidtm_interact_fuck(i):
    $ wolfidtm_interact_fuck_action(i)

    return

label hine_interact:
    call hide_ui
    if "interacting_hero" not in hine_know:
        $ hine_know.append("interacting_hero")

    menu:
        "Chat" if not is_specialevent:
            jump hine_interact_chat
        "Touch" if not is_specialevent:
            jump hine_interact_touch
        "Hang out":
            jump hine_interact_hangout
        "Give item" if not is_specialevent:
            jump hine_interact_gift
        "Fuck" if wolfidtm_can_fuck("hine"):
            jump wolfidtm_interact_fuck("hine")
        "Return":
            jump hine_interact_end

label hprv_interact:
    call hide_ui
    if "interacting_hero" not in hprv_know:
        $ hprv_know.append("interacting_hero")

    menu:
        "Chat" if not is_specialevent:
            jump hprv_interact_chat
        "Touch" if not is_specialevent:
            jump hprv_interact_touch
        "Hang out":
            jump hprv_interact_hangout
        "Give item" if not is_specialevent:
            jump hprv_interact_gift
        "Fuck" if wolfidtm_can_fuck("hprv"):
            jump wolfidtm_interact_fuck("hprv")
        "Return":
            jump hprv_interact_end

label wcou_interact:
    call hide_ui
    if "interacting_hero" not in wcou_know:
        $ wcou_know.append("interacting_hero")

    menu:
        "Chat" if not is_specialevent:
            jump wcou_interact_chat
        "Touch" if not is_specialevent:
            jump wcou_interact_touch
        "Hang out" if Char_Data["hero"]["quest"]["A New Journey"] >= 3:
            jump wcou_interact_hangout
        "Give item" if not is_specialevent:
            jump wcou_interact_gift
        "Fuck" if wolfidtm_can_fuck("wcou"):
            jump wolfidtm_interact_fuck("wcou")
        "Return":
            jump wcou_interact_end

label wdel_interact:
    call hide_ui
    if "interacting_hero" not in wdel_know:
        $ wdel_know.append("interacting_hero")

    menu:
        "Chat" if not is_specialevent:
            jump wdel_interact_chat
        "Touch" if not is_specialevent:
            jump wdel_interact_touch
        "Hang out":
            jump wdel_interact_hangout
        "Give item" if not is_specialevent:
            jump wdel_interact_gift
        "Fuck" if wolfidtm_can_fuck("wdel"):
            jump wolfidtm_interact_fuck("wdel")
        "Return":
            jump wdel_interact_end

label wdis_interact:
    call hide_ui
    if "interacting_hero" not in wdis_know:
        $ wdis_know.append("interacting_hero")

    menu:
        "Chat" if not is_specialevent:
            jump wdis_interact_chat
        "Touch" if not is_specialevent:
            jump wdis_interact_touch
        "Hang out":
            jump wdis_interact_hangout
        "Give item" if not is_specialevent:
            jump wdis_interact_gift
        "Fuck" if wolfidtm_can_fuck("wdis"):
            jump wolfidtm_interact_fuck("wdis")
        "Return":
            jump wdis_interact_end

label wgal_interact:
    call hide_ui
    if "interacting_hero" not in wgal_know:
        $ wgal_know.append("interacting_hero")

    menu:
        "Chat" if not is_specialevent:
            jump wgal_interact_chat
        "Touch" if not is_specialevent:
            jump wgal_interact_touch
        "Hang out":
            jump wgal_interact_hangout
        "Give item" if not is_specialevent:
            jump wgal_interact_gift
        "Fuck" if wolfidtm_can_fuck("wgal"):
            jump wolfidtm_interact_fuck("wgal")
        "Return":
            jump wgal_interact_end

label wgot_interact:
    call hide_ui
    if "interacting_hero" not in wgot_know:
        $ wgot_know.append("interacting_hero")

    menu:
        "Chat" if not is_specialevent:
            jump wgot_interact_chat
        "Touch" if not is_specialevent:
            jump wgot_interact_touch
        "Hang out":
            jump wgot_interact_hangout
        "Give item" if not is_specialevent:
            jump wgot_interact_gift
        "Fuck" if wolfidtm_can_fuck("wgot"):
            jump wolfidtm_interact_fuck("wgot")
        "Return":
            jump wgot_interact_end

label wlaz_interact:
    call hide_ui
    if "interacting_hero" not in wlaz_know:
        $ wlaz_know.append("interacting_hero")

    menu:
        "Chat" if not is_specialevent:
            jump wlaz_interact_chat
        "Touch" if not is_specialevent:
            jump wlaz_interact_touch
        "Hang out":
            jump wlaz_interact_hangout
        "Give item" if not is_specialevent:
            jump wlaz_interact_gift
        "Fuck" if wolfidtm_can_fuck("wlaz"):
            jump wolfidtm_interact_fuck("wlaz")
        "Return":
            jump wlaz_interact_end

label wmom_interact:
    call hide_ui
    call wmom_screen_check
    if "interacting_hero" not in wmom_know:
        $ wmom_know.append("interacting_hero")

    menu:
        "Chat" if not is_specialevent:
            jump wmom_interact_chat
        "Touch" if not is_specialevent:
            jump wmom_interact_touch
        "Hang out":
            jump wmom_interact_hangout
        "Give item" if not is_specialevent:
            jump wmom_interact_gift
        "Fuck" if wolfidtm_can_fuck("wmom"):
            jump wolfidtm_interact_fuck("wmom")
        "Return":
            jump wmom_interact_end

label wnei_interact:
    call hide_ui
    if "interacting_hero" not in wnei_know:
        $ wnei_know.append("interacting_hero")

    menu:
        "Chat" if not is_specialevent:
            if sum(1 for get_id in wnei_know if get_id =="Talk") >= 2:
                $ Char_Data["wnei"]["mood"] = "O1"
                wnei "Ehhh...?{w=[wt2]} Enough of chatting! Let's do something fun!"
                jump wnei_interact
            else:
                jump wnei_interact_chat
        "Touch" if not is_specialevent:
            jump wnei_interact_touch
        "Hang out":
            jump wnei_interact_hangout
        "Give item" if not is_specialevent:
            jump wnei_interact_gift
        "Fuck" if wolfidtm_can_fuck("wnei"):
            jump wolfidtm_interact_fuck("wnei")
        "Return":
            jump wnei_interact_end

label wota_interact:
    call hide_ui
    if "interacting_hero" not in wota_know:
        $ wota_know.append("interacting_hero")

    menu:
        "Chat" if not is_specialevent:
            jump wota_interact_chat
        "Touch" if not is_specialevent:
            jump wota_interact_touch
        "Hang out":
            jump wota_interact_hangout
        "Give item" if not is_specialevent:
            jump wota_interact_gift
        "Fuck" if wolfidtm_can_fuck("wota"):
            jump wolfidtm_interact_fuck("wota")
        "Return":
            jump wota_interact_end

label wpre_interact:
    call hide_ui
    if "interacting_hero" not in wpre_know:
        $ wpre_know.append("interacting_hero")

    menu:
        "Chat" if not is_specialevent:
            jump wpre_interact_chat
        "Touch" if not is_specialevent:
            jump wpre_interact_touch
        "Hang out":
            jump wpre_interact_hangout
        "Give item" if not is_specialevent:
            jump wpre_interact_gift
        "Fuck" if wolfidtm_can_fuck("wpre"):
            jump wolfidtm_interact_fuck("wpre")
        "Return":
            jump wpre_interact_end

label wric_interact:
    call hide_ui
    if "interacting_hero" not in wric_know:
        $ wric_know.append("interacting_hero")

    menu:
        "Chat" if not is_specialevent:
            jump wric_interact_chat
        "Touch" if not is_specialevent:
            jump wric_interact_touch
        "Hang out":
            jump wric_interact_hangout
        "Give item" if not is_specialevent:
            jump wric_interact_gift
        "Fuck" if wolfidtm_can_fuck("wric"):
            jump wolfidtm_interact_fuck("wric")
        "Return":
            jump wric_interact_end

label wsis_interact:
    call hide_ui
    if "interacting_hero" not in Char_Data["wsis"]["know"]:
        $ Char_Data["wsis"]["know"].append("interacting_hero")

    menu:
        "Chat" if not is_specialevent:
            if sum(1 for buceta in Char_Data["wsis"]["know"] if buceta =="Talk") >= 3 and Char_Data["wsis"]["quest"]["Forgiveness"] == 0:
                $ Char_Data["wsis"]["mood"] = "O1"
                wsis "Enough of chitchatting{w=[wt1]}, don't you think?"
                jump wsis_interact
            else:
                jump wsis_interact_chat
        "Touch" if not is_specialevent:
            jump wsis_interact_touch
        "Hang out":
            jump wsis_interact_hangout
        "Give item" if not is_specialevent:
            jump wsis_interact_gift
        "Fuck" if wolfidtm_can_fuck("wsis"):
            jump wolfidtm_interact_fuck("wsis")
        "Return":
            jump wsis_interact_end

label wuza_interact:
    call hide_ui
    if "interacting_hero" not in wuza_know:
        $ wuza_know.append("interacting_hero")

    menu:
        "Chat" if not is_specialevent:
            jump wuza_interact_chat
        "Touch" if not is_specialevent:
            jump wuza_interact_touch
        "Hang out":
            jump wuza_interact_hangout
        "Give item" if not is_specialevent:
            jump wuza_interact_gift
        "Fuck" if wolfidtm_can_fuck("wuza"):
            jump wolfidtm_interact_fuck("wuza")
        "Return":
            jump wuza_interact_end