init 90000 python:
    def wolfidtm_can_fuck(i):
        if i in wear_get_chars():
           if not renpy.has_label("wolfitdm_fuck_" + i):
              return False

           if WChar.gvar(i, "love") >= 100:
              return True
           else:
              return False
        else:
           return False

    def wolfidtm_interact_fuck_action(i):
        if wolfidtm_can_fuck(i):
           renpy.call("wolfitdm_fuck_"+i)

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
            call wolfidtm_interact_fuck("hine")
            jump hine_interact
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
            call wolfidtm_interact_fuck("hprv")
            jump hprv_interact
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
        "Hang out" if WChar.gvar("hero", "A New Journey") >= 3:
            jump wcou_interact_hangout
        "Give item" if not is_specialevent:
            jump wcou_interact_gift
        "Fuck" if wolfidtm_can_fuck("wcou"):
            call wolfidtm_interact_fuck("wcou")
            jump wcou_interact
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
            call wolfidtm_interact_fuck("wdel")
            jump wdel_interact
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
            call wolfidtm_interact_fuck("wdis")
            jump wdis_interact
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
            call wolfidtm_interact_fuck("wgal")
            jump wgal_interact
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
            call wolfidtm_interact_fuck("wgot")
            jump wgot_interact
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
            call wolfidtm_interact_fuck("wlaz")
            jump wlaz_interact
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
            call wolfidtm_interact_fuck("wmom")
            jump wmom_interact
        "Return":
            jump wmom_interact_end

label wnei_interact:
    call hide_ui
    if "interacting_hero" not in wnei_know:
        $ wnei_know.append("interacting_hero")

    menu:
        "Chat" if not is_specialevent:
            if sum(1 for get_id in wnei_know if get_id =="Talk") >= 2:
                $ WChar.svar("wnei", "mood", "O1")
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
            call wolfidtm_interact_fuck("wnei")
            jump wnei_interact
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
            call wolfidtm_interact_fuck("wota")
            jump wota_interact
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
            call wolfidtm_interact_fuck("wpre")
            jump wpre_interact
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
            call wolfidtm_interact_fuck("wric")
            jump wric_interact
        "Return":
            jump wric_interact_end

label wsis_interact:
    call hide_ui
    $ current_wsis_know = WChar.gvar("wsis", "know")
    $ current_wsis_forgiveness = WChar.gvar("wsis", "Forgiveness")
    if "interacting_hero" not in current_wsis_know:
        $ current_wsis_know.append("interacting_hero")
        $ WChar.svar("wsis", "know", current_wsis_know)

    menu:
        "Chat" if not is_specialevent:
            if sum(1 for buceta in current_wsis_know if buceta =="Talk") >= 3 and current_wsis_forgiveness == 0:
                $ WChar.svar("wsis", "mood", "O1")
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
            call wolfidtm_interact_fuck("wsis")
            jump wsis_interact
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
            call wolfidtm_interact_fuck("wuza")
            jump wuza_interact
        "Return":
            jump wuza_interact_end