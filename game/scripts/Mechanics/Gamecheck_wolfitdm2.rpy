# ----------------------------------------------------------------------------------------------------
# Check Player Current Map
# ----------------------------------------------------------------------------------------------------

label check_playermap_new:
    if Char_Data["hero"]["map"] == None:
        $ Get_MapName("hero")

    if Char_Data["hero"]["map"] == Map_Data["city"]["name"]:
        call goto_map
        scene bg_map at Zoom_X(0.5)
        show screen nav_map

    if Char_Data["hero"]["map"] == Map_Data["home"]["name"] + " - " + Map_Data["home"]["map"]["facade"]["name"]:
        call goto_home_facade
        scene bg_home facade
        show screen nav_home_facade

    elif Char_Data["hero"]["map"] == Map_Data["home"]["name"] + " - " + Map_Data["home"]["map"]["living_room"]["name"]:
        call goto_home_livingroom
        scene bg_home livingroom
        show screen nav_home_livingroom

    elif Char_Data["hero"]["map"] == Map_Data["home"]["name"] + " - " + Map_Data["home"]["map"]["hallway"]["name"]:
        call goto_home_hallway
        scene bg_home hallway
        show screen nav_home_hallway

    elif Char_Data["hero"]["map"] == Map_Data["home"]["name"] + " - " + Map_Data["home"]["map"]["bedroom_hero"]["name"]:
        call goto_home_bedroom_hero
        scene bg_home bedroom hero
        show screen nav_home_bedroom_hero

    elif Char_Data["hero"]["map"] == Map_Data["home"]["name"] + " - " + Map_Data["home"]["map"]["bedroom_wsis"]["name"]:
        call goto_home_bedroom_wsis
        scene bg_home bedroom wsis
        show screen nav_home_bedroom_wsis
        #with fade

    elif Char_Data["hero"]["map"] == Map_Data["home"]["name"] + " - " + Map_Data["home"]["map"]["bedroom_wmom"]["name"]:
        call goto_home_bedroom_wmom
        scene bg_home bedroom wmom
        show screen nav_home_bedroom_wmom

    elif Char_Data["hero"]["map"] == Map_Data["home"]["name"] + " - " + Map_Data["home"]["map"]["bathroom"]["name"]:
        call goto_home_bathroom
        scene bg_home bathroom
        show screen nav_home_bathroom

    elif Char_Data["hero"]["map"] == Map_Data["office"]["name"] + " - " + Map_Data["office"]["map"]["facade"]["name"]:
        call goto_office_facade
        scene bg_office facade
        show screen nav_office_facade

    elif Char_Data["hero"]["map"] == Map_Data["office"]["name"] + " - " + Map_Data["office"]["map"]["office_wcou"]["name"]:
        call goto_office_room
        scene bg_office_room
        show screen nav_office_room

    elif Char_Data["hero"]["map"] == Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["facade"]["name"]:
        call goto_school_facade
        scene bg_school facade
        show screen nav_school_facade

    elif Char_Data["hero"]["map"] == Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["courtyard"]["name"]:
        call goto_school_courtyard
        scene bg_school courtyard
        show screen nav_school_courtyard

    elif Char_Data["hero"]["map"] == Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["frontyard"]["name"]:
        call goto_school_frontyard
        scene bg_school frontyard
        show screen nav_school_frontyard

    elif Char_Data["hero"]["map"] == Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["locker_m"]["name"]:
        call goto_school_locker_m
        scene bg_school locker_m
        show screen nav_school_locker_m

    elif Char_Data["hero"]["map"] == Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["hallway_1"]["name"]:
        call goto_school_hallway1
        scene bg_school hallway1
        show screen nav_school_hallway1

    elif Char_Data["hero"]["map"] == Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["hallway_2"]["name"]:
        call goto_school_hallway2
        scene bg_school hallway2
        show screen nav_school_hallway2

    elif Char_Data["hero"]["map"] == Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["class_1a"]["name"]:
        call goto_school_classroom_1a
        scene bg_school classroom_1a
        show screen nav_school_classroom_1a

    elif Char_Data["hero"]["map"] == Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["class_1b"]["name"]:
        call goto_school_classroom_1b
        scene bg_school classroom_1b
        show screen nav_school_classroom_1b

    elif Char_Data["hero"]["map"] == Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["class_3a"]["name"]:
        call goto_school_classroom_3a
        scene bg_school classroom_3a
        show screen nav_school_classroom_3a

    elif Char_Data["hero"]["map"] == Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["library"]["name"]:
        call goto_school_library
        scene bg_school library
        show screen nav_school_library

    elif Char_Data["hero"]["map"] == Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["swimming_pool"]["name"]:
        call goto_school_pool
        scene bg_school pool
        show screen nav_school_pool

    elif Char_Data["hero"]["map"] == Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["sports_court"]["name"]:
        call goto_school_sportcourt
        scene bg_school sportcourt
        show screen nav_school_sportcourt

    elif Char_Data["hero"]["map"] == Map_Data["school"]["name"] + " - " + Map_Data["school"]["map"]["club_coun"]["name"]:
        call goto_school_club_council
        scene bg_school club_council
        show screen nav_school_club_council

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