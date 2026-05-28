default Char_Data = {}

# ----------------------------------------------------------------------------------------------------
# Check Player Current Map
# ----------------------------------------------------------------------------------------------------

label check_playermap_new:
    $ the_hero_map = WChar.gvar("hero", "map")

    if the_hero_map == None:
        $ Get_MapName("hero")

    elif the_hero_map == Map_Data["city"]["name"]:
        call goto_map
        scene bg_map at Zoom_X(0.5)
        show screen nav_map

    elif the_hero_map == Map_Data["home"]["name"] + " - " + Map_Data["home"]["map"]["facade"]["name"]:
        call goto_home_facade
        scene bg_home facade
        show screen nav_home_facade

    elif the_hero_map == Map_Data["home"]["name"] + " - " + Map_Data["home"]["map"]["living_room"]["name"]:
        call goto_home_livingroom
        scene bg_home livingroom
        show screen nav_home_livingroom

    elif the_hero_map == Map_Data["home"]["name"] + " - " + Map_Data["home"]["map"]["hallway"]["name"]:
        call goto_home_hallway
        scene bg_home hallway
        show screen nav_home_hallway

    elif the_hero_map == Map_Data["home"]["name"] + " - " + Map_Data["home"]["map"]["bedroom_hero"]["name"]:
        call goto_home_bedroom_hero
        scene bg_home bedroom hero
        show screen nav_home_bedroom_hero

    elif the_hero_map == Map_Data["home"]["name"] + " - " + Map_Data["home"]["map"]["bedroom_wsis"]["name"]:
        call goto_home_bedroom_wsis
        scene bg_home bedroom wsis
        show screen nav_home_bedroom_wsis

    elif the_hero_map == Map_Data["home"]["name"] + " - " + Map_Data["home"]["map"]["bedroom_wmom"]["name"]:
        call goto_home_bedroom_wmom
        scene bg_home bedroom wmom
        show screen nav_home_bedroom_wmom

    elif the_hero_map == Map_Data["home"]["name"] + " - " + Map_Data["home"]["map"]["bathroom"]["name"]:
        call goto_home_bathroom
        scene bg_home bathroom
        show screen nav_home_bathroom

    elif the_hero_map == Map_Data["office"]["name"] + " - " + Map_Data["office"]["map"]["facade"]["name"]:
        call goto_office_facade
        scene bg_office facade
        show screen nav_office_facade

    elif the_hero_map == Map_Data["office"]["name"] + " - " + Map_Data["office"]["map"]["office_wcou"]["name"]:
        call goto_office_room
        scene bg_office_room
        show screen nav_office_room

    elif the_hero_map == Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["facade"]["name"]:
        call goto_school_facade
        scene bg_school facade
        show screen nav_school_facade

    elif the_hero_map == Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["courtyard"]["name"]:
        call goto_school_courtyard
        scene bg_school courtyard
        show screen nav_school_courtyard

    elif the_hero_map == Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["frontyard"]["name"]:
        call goto_school_frontyard
        scene bg_school frontyard
        show screen nav_school_frontyard

    elif the_hero_map == Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["locker_m"]["name"]:
        call goto_school_locker_m
        scene bg_school locker_m
        show screen nav_school_locker_m

    elif the_hero_map == Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["hallway_1"]["name"]:
        call goto_school_hallway1
        scene bg_school hallway1
        show screen nav_school_hallway1

    elif the_hero_map == Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["hallway_2"]["name"]:
        call goto_school_hallway2
        scene bg_school hallway2
        show screen nav_school_hallway2

    elif the_hero_map == Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["class_1a"]["name"]:
        call goto_school_classroom_1a
        scene bg_school classroom_1a
        show screen nav_school_classroom_1a

    elif the_hero_map == Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["class_1b"]["name"]:
        call goto_school_classroom_1b
        scene bg_school classroom_1b
        show screen nav_school_classroom_1b

    elif the_hero_map == Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["class_3a"]["name"]:
        call goto_school_classroom_3a
        scene bg_school classroom_3a
        show screen nav_school_classroom_3a

    elif the_hero_map == Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["library"]["name"]:
        call goto_school_library
        scene bg_school library
        show screen nav_school_library

    elif the_hero_map == Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["swimming_pool"]["name"]:
        call goto_school_pool
        scene bg_school pool
        show screen nav_school_pool

    elif the_hero_map == Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["sports_court"]["name"]:
        call goto_school_sportcourt
        scene bg_school sportcourt
        show screen nav_school_sportcourt

    elif the_hero_map == Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["club_coun"]["name"]:
        call goto_school_club_council
        scene bg_school club_council
        show screen nav_school_club_council
    else:
        python:
            if renpy.has_label("check_playermap_original"):
               renpy.jump("check_playermap_original")

    # ----------------------------------------------------------------------------------------------------
    # Check if there's an available scene on the current map
    # ----------------------------------------------------------------------------------------------------

    call check_availablescene

    # --------------------------------------------------
    # Default notification timer
    # --------------------------------------------------

    $ persistent.notice1 = 0.5  # FadeIn
    $ persistent.notice2 = 5.5  # Duration
    $ persistent.notice3 = 0.5  # FadeOut

    return

label check_playermap_new_wolfitdm(map):
    if map == None:
        $ Get_MapName("hero")

    elif map == Map_Data["city"]["name"]:
        scene bg_map at Zoom_X(0.5)
        show screen nav_map

    elif map == Map_Data["home"]["name"] + " - " + Map_Data["home"]["map"]["facade"]["name"]:
        scene bg_home facade
        show screen nav_home_facade

    elif map == Map_Data["home"]["name"] + " - " + Map_Data["home"]["map"]["living_room"]["name"]:
        scene bg_home livingroom
        show screen nav_home_livingroom

    elif map == Map_Data["home"]["name"] + " - " + Map_Data["home"]["map"]["hallway"]["name"]:
        scene bg_home hallway
        show screen nav_home_hallway

    elif map == Map_Data["home"]["name"] + " - " + Map_Data["home"]["map"]["bedroom_hero"]["name"]:
        scene bg_home bedroom hero
        show screen nav_home_bedroom_hero

    elif map == Map_Data["home"]["name"] + " - " + Map_Data["home"]["map"]["bedroom_wsis"]["name"]:
        scene bg_home bedroom wsis
        show screen nav_home_bedroom_wsis

    elif map == Map_Data["home"]["name"] + " - " + Map_Data["home"]["map"]["bedroom_wmom"]["name"]:
        scene bg_home bedroom wmom
        show screen nav_home_bedroom_wmom

    elif map == Map_Data["home"]["name"] + " - " + Map_Data["home"]["map"]["bathroom"]["name"]:
        scene bg_home bathroom
        show screen nav_home_bathroom

    elif map == Map_Data["office"]["name"] + " - " + Map_Data["office"]["map"]["facade"]["name"]:
        scene bg_office facade
        show screen nav_office_facade

    elif map == Map_Data["office"]["name"] + " - " + Map_Data["office"]["map"]["office_wcou"]["name"]:
        scene bg_office_room
        show screen nav_office_room

    elif map == Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["facade"]["name"]:
        scene bg_school facade
        show screen nav_school_facade

    elif map == Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["courtyard"]["name"]:
        scene bg_school courtyard
        show screen nav_school_courtyard

    elif map == Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["frontyard"]["name"]:
        scene bg_school frontyard
        show screen nav_school_frontyard

    elif map == Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["locker_m"]["name"]:
        scene bg_school locker_m
        show screen nav_school_locker_m

    elif map == Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["hallway_1"]["name"]:
        scene bg_school hallway1
        show screen nav_school_hallway1

    elif map == Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["hallway_2"]["name"]:
        scene bg_school hallway2
        show screen nav_school_hallway2

    elif map == Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["class_1a"]["name"]:
        scene bg_school classroom_1a
        show screen nav_school_classroom_1a

    elif map == Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["class_1b"]["name"]:
        scene bg_school classroom_1b
        show screen nav_school_classroom_1b

    elif map == Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["class_3a"]["name"]:
        scene bg_school classroom_3a
        show screen nav_school_classroom_3a

    elif map == Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["library"]["name"]:
        scene bg_school library
        show screen nav_school_library

    elif map == Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["swimming_pool"]["name"]:
        scene bg_school pool
        show screen nav_school_pool

    elif map == Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["sports_court"]["name"]:
        scene bg_school sportcourt
        show screen nav_school_sportcourt

    elif map == Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["club_coun"]["name"]:
        scene bg_school club_council
        show screen nav_school_club_council

    return

init -90000 python:
    def wolfitdm_check_map_ok(i):

        if not WChar.get_is_old_version():
           return

        if not i in Char_Data:
           Char_Data[i] = {}

        if not "map" in Char_Data[i]:
           Char_Data[i]["map"] = None

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

default wolfitdm_original_player_map = None
default Char_Data = {}
default override_check_playermap_wolfitdm_inject = False

label wolfitdm_check_playermap:
    $ wolfitdm_check_map_ok("hero")

    $ the_hero_map = WChar.gvar("hero", "map")

    if the_hero_map == None:
       $ wolfitdm_original_player_map = None
       $ store.wolfitdm_original_player_map = None
    elif the_hero_map in wolfitdm_get_maps():
       $ wolfitdm_original_player_map = the_hero_map
       $ store.wolfitdm_original_player_map = the_hero_map
    else:
       call check_playermap_new_wolfitdm(wolfitdm_original_player_map)

    jump check_playermap_override