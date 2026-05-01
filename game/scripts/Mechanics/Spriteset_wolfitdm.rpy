# ----------------------------------------------------------------------------------------------------
# KAWAII
# ----------------------------------------------------------------------------------------------------
image KAWAII EYES:
    "kawaii/eyes/kawaii_eyes0.png",
    choice:
        0.15
    choice:
        4
    choice:
        5
    choice:
        5
    choice:
        6
    choice:
        7
    "kawaii/eyes/kawaii_eyes2.png",
    0.15
    "kawaii/eyes/kawaii_eyes1.png",
    0.1
    repeat

image KAWAII MOUTH:
    ConditionSwitch(
        "Char_Data['hero']['mood'] == 'A1'", "kawaii/mouth/general_mouth_2_A1.png",
        "Char_Data['hero']['mood'] == 'A2'", "kawaii/mouth/general_mouth_2_A2.png",
        "Char_Data['hero']['mood'] == 'A3'", "kawaii/mouth/general_mouth_2_A3.png",
        "Char_Data['hero']['mood'] == 'A4'", "kawaii/mouth/general_mouth_2_A4.png",
        "Char_Data['hero']['mood'] == 'O1'", "kawaii/mouth/general_mouth_2_O1.png",
        "Char_Data['hero']['mood'] == 'O2'", "kawaii/mouth/general_mouth_2_O2.png",
        "Char_Data['hero']['mood'] == 'O3'", "kawaii/mouth/general_mouth_2_O3.png",
        "Char_Data['hero']['mood'] == 'O4'", "kawaii/mouth/general_mouth_2_O4.png",
        "True", "kawaii/mouth/general_mouth_2_A1.png"
    ),
    .15
    ConditionSwitch(
        "Char_Data['hero']['mood'] == 'A1'", "kawaii/mouth/kawaii_mouth_1_A1.png",
        "Char_Data['hero']['mood'] == 'A2'", "kawaii/mouth/kawaii_mouth_1_A2.png",
        "Char_Data['hero']['mood'] == 'A3'", "kawaii/mouth/kawaii_mouth_1_A3.png",
        "Char_Data['hero']['mood'] == 'A4'", "kawaii/mouth/kawaii_mouth_1_A4.png",
        "Char_Data['hero']['mood'] == 'O1'", "kawaii/mouth/kawaii_mouth_1_O1.png",
        "Char_Data['hero']['mood'] == 'O2'", "kawaii/mouth/kawaii_mouth_1_O2.png",
        "Char_Data['hero']['mood'] == 'O3'", "kawaii/mouth/kawaii_mouth_1_O3.png",
        "Char_Data['hero']['mood'] == 'O4'", "kawaii/mouth/kawaii_mouth_1_O4.png",
        "True", "kawaii/mouth/kawaii_mouth_1_A1.png"
    )
    .15
    repeat

image KAWAII WEAR:
    ConditionSwitch(
        "Char_Data['hero']['wear'] == 'kawaii_home'", "kawaii/body_wear_phone/kawaii_body_wear_home.png",
        "Char_Data['hero']['wear'] == 'kawaii_under'", "kawaii/body_wear_phone/kawaii_body_wear_under.png",
        "Char_Data['hero']['wear'] == 'kawaii_sleep'", "kawaii/body_wear_phone/kawaii_body_wear_sleep.png",
        "Char_Data['hero']['wear'] == 'kawaii_casual'", "kawaii/body_wear_phone/kawaii_body_wear_casual.png",
        "Char_Data['hero']['wear'] == 'kawaii_dressy'", "kawaii/body_wear_phone/kawaii_body_wear_dressy.png",
        "Char_Data['hero']['wear'] == 'kawaii_formal'", "kawaii/body_wear_phone/kawaii_body_wear_formal.png",
        "Char_Data['hero']['wear'] == 'kawaii_sport'", "kawaii/body_wear_phone/kawaii_body_wear_sport.png",
        "Char_Data['hero']['wear'] == 'kawaii_swim'", "kawaii/body_wear_phone/kawaii_body_wear_swim.png",
        "Char_Data['hero']['wear'] == 'kawaii_school'", "kawaii/body_wear_phone/kawaii_body_wear_school.png",
        "Char_Data['hero']['wear'] == 'kawaii_school_swim'", "kawaii/body_wear_phone/kawaii_body_wear_school_swim.png",
        "Char_Data['hero']['wear'] == 'kawaii_school_sport'", "kawaii/body_wear_phone/kawaii_body_wear_school_sport.png",
        "Char_Data['hero']['wear'] == 'kawaii_work'", "kawaii/body_wear_phone/kawaii_body_wear_work.png",
        "Char_Data['hero']['wear'] == 'kawaii_soap'", "kawaii/body_wear_phone/kawaii_body_wear_soap.png",
        "True", Null()
    ),

image KAWAII HEADFG PARTS = Composite(
    (720,1080),
    (0,0), "kawaii/eyes/kawaii_eyes3.png",
    (0,0), ConditionSwitch(
         "Char_Data['hero']['wear'] == 'kawaii_school_swim'", "kawaii/head/school_swim/kawaii_head_mg_school_swim.png",
         "Char_Data['hero']['wear'] == 'kawaii_school_sport'", "kawaii/head/school_sport/kawaii_head_mg_school_sport.png",
         "Char_Data['hero']['wear'] == 'kawaii_casual'", "kawaii/head/casual/kawaii_head_mg_casual.png",
         "Char_Data['hero']['wear'] == 'kawaii_dressy'", "kawaii/head/dressy/kawaii_head_mg_dressy.png",
         "Char_Data['hero']['wear'] == 'kawaii_formal'", "kawaii/head/formal/kawaii_head_mg_formal.png",
         "Char_Data['hero']['wear'] == 'kawaii_home'", "kawaii/head/home/kawaii_head_mg_home.png",
         "Char_Data['hero']['wear'] == 'kawaii_school'", "kawaii/head/school/kawaii_head_mg_school.png",
         "Char_Data['hero']['wear'] == 'kawaii_sleep'", "kawaii/head/sleep/kawaii_head_mg_sleep.png",
         "Char_Data['hero']['wear'] == 'kawaii_soap'", "kawaii/head/soap/kawaii_head_mg_soap.png",
         "Char_Data['hero']['wear'] == 'kawaii_under'", "kawaii/head/under/kawaii_head_mg_under.png",
         "Char_Data['hero']['wear'] == 'kawaii_work'", "kawaii/head/work/kawaii_head_mg_work.png",
         "True", "kawaii/head/kawaii_head_mg.png"
    ),
    (0,0), ConditionSwitch(
        "Char_Data['hero']['fx'] == 0", "kawaii/fx/kawaii_fx_0.png",
        "Char_Data['hero']['fx'] == 1", "kawaii/fx/kawaii_fx_1.png",
        "Char_Data['hero']['fx'] == 2", "kawaii/fx/kawaii_fx_2.png",
        "Char_Data['hero']['fx'] == 3", "kawaii/fx/kawaii_fx_3.png",
        "True", "kawaii/fx/kawaii_fx_0.png"
    ),
    (0,0), WhileSpeaking("hero", "KAWAII MOUTH", ConditionSwitch(
        "Char_Data['hero']['mood'] == 'A1'", "kawaii/mouth/general_mouth_2_A1.png",
        "Char_Data['hero']['mood'] == 'A2'", "kawaii/mouth/general_mouth_2_A2.png",
        "Char_Data['hero']['mood'] == 'A3'", "kawaii/mouth/general_mouth_2_A3.png",
        "Char_Data['hero']['mood'] == 'A4'", "kawaii/mouth/general_mouth_2_A4.png",
        "Char_Data['hero']['mood'] == 'O1'", "kawaii/mouth/general_mouth_2_O1.png",
        "Char_Data['hero']['mood'] == 'O2'", "kawaii/mouth/general_mouth_2_O2.png",
        "Char_Data['hero']['mood'] == 'O3'", "kawaii/mouth/general_mouth_2_O3.png",
        "Char_Data['hero']['mood'] == 'O4'", "kawaii/mouth/general_mouth_2_O4.png",
        "True", "kawaii/mouth/general_mouth_2_A1.png"
    )),
    (0,0), ConditionSwitch(
         "Char_Data['hero']['wear'] == 'kawaii_school_swim'", "kawaii/head/school_swim/kawaii_head_wear_school_swim.png",
         "Char_Data['hero']['wear'] == 'kawaii_school_sport'", "kawaii/head/school_sport/kawaii_head_wear_school_sport.png",
         "Char_Data['hero']['wear'] == 'kawaii_casual'", "kawaii/head/casual/kawaii_head_wear_casual.png",
         "Char_Data['hero']['wear'] == 'kawaii_dressy'", "kawaii/head/dressy/kawaii_head_wear_dressy.png",
         "Char_Data['hero']['wear'] == 'kawaii_formal'", "kawaii/head/formal/kawaii_head_wear_formal.png",
         "Char_Data['hero']['wear'] == 'kawaii_home'", "kawaii/head/home/kawaii_head_wear_home.png",
         "Char_Data['hero']['wear'] == 'kawaii_school'", "kawaii/head/school/kawaii_head_wear_school.png",
         "Char_Data['hero']['wear'] == 'kawaii_sleep'", "kawaii/head/sleep/kawaii_head_wear_sleep.png",
         "Char_Data['hero']['wear'] == 'kawaii_soap'", "kawaii/head/soap/kawaii_head_wear_soap.png",
         "Char_Data['hero']['wear'] == 'kawaii_under'", "kawaii/head/under/kawaii_head_wear_under.png",
         "Char_Data['hero']['wear'] == 'kawaii_work'", "kawaii/head/work/kawaii_head_wear_work.png",
         "True", "kawaii/head/kawaii_head_wear.png"
    ),
    (0,0), "KAWAII EYES",
    (0,0), ConditionSwitch(
         "Char_Data['hero']['wear'] == 'kawaii_school_swim'", "kawaii/head/school_swim/kawaii_head_fg1_school_swim.png",
         "Char_Data['hero']['wear'] == 'kawaii_school_sport'", "kawaii/head/school_sport/kawaii_head_fg1_school_sport.png",
         "Char_Data['hero']['wear'] == 'kawaii_casual'", "kawaii/head/casual/kawaii_head_fg1_casual.png",
         "Char_Data['hero']['wear'] == 'kawaii_dressy'", "kawaii/head/dressy/kawaii_head_fg1_dressy.png",
         "Char_Data['hero']['wear'] == 'kawaii_formal'", "kawaii/head/formal/kawaii_head_fg1_formal.png",
         "Char_Data['hero']['wear'] == 'kawaii_home'", "kawaii/head/home/kawaii_head_fg1_home.png",
         "Char_Data['hero']['wear'] == 'kawaii_school'", "kawaii/head/school/kawaii_head_fg1_school.png",
         "Char_Data['hero']['wear'] == 'kawaii_sleep'", "kawaii/head/sleep/kawaii_head_fg1_sleep.png",
         "Char_Data['hero']['wear'] == 'kawaii_soap'", "kawaii/head/soap/kawaii_head_fg1_soap.png",
         "Char_Data['hero']['wear'] == 'kawaii_under'", "kawaii/head/under/kawaii_head_fg1_under.png",
         "Char_Data['hero']['wear'] == 'kawaii_work'", "kawaii/head/work/kawaii_head_fg1_work.png",
         "True", "kawaii/head/kawaii_head_fg1.png"
    ),
    (0,0), ConditionSwitch(
         "Char_Data['hero']['wear'] == 'kawaii_school_swim'", "kawaii/head/school_swim/kawaii_head_fg2_school_swim.png",
         "Char_Data['hero']['wear'] == 'kawaii_school_sport'", "kawaii/head/school_sport/kawaii_head_fg2_school_sport.png",
         "Char_Data['hero']['wear'] == 'kawaii_casual'", "kawaii/head/casual/kawaii_head_fg2_casual.png",
         "Char_Data['hero']['wear'] == 'kawaii_dressy'", "kawaii/head/dressy/kawaii_head_fg2_dressy.png",
         "Char_Data['hero']['wear'] == 'kawaii_formal'", "kawaii/head/formal/kawaii_head_fg2_formal.png",
         "Char_Data['hero']['wear'] == 'kawaii_home'", "kawaii/head/home/kawaii_head_fg2_home.png",
         "Char_Data['hero']['wear'] == 'kawaii_school'", "kawaii/head/school/kawaii_head_fg2_school.png",
         "Char_Data['hero']['wear'] == 'kawaii_sleep'", "kawaii/head/sleep/kawaii_head_fg2_sleep.png",
         "Char_Data['hero']['wear'] == 'kawaii_soap'", "kawaii/head/soap/kawaii_head_fg2_soap.png",
         "Char_Data['hero']['wear'] == 'kawaii_under'", "kawaii/head/under/kawaii_head_fg2_under.png",
         "Char_Data['hero']['wear'] == 'kawaii_work'", "kawaii/head/work/kawaii_head_fg2_work.png",
         "True", "kawaii/head/kawaii_head_fg2.png"
    ),
    (0,0), ConditionSwitch(
        "Char_Data['hero']['mood'] == 'A1'", "kawaii/eyes/kawaii_eyebrow_A1.png",
        "Char_Data['hero']['mood'] == 'A2'", "kawaii/eyes/kawaii_eyebrow A2.png",
        "Char_Data['hero']['mood'] == 'A3'", "kawaii/eyes/kawaii_eyebrow_A3.png",
        "Char_Data['hero']['mood'] == 'A4'", "kawaii/eyes/kawaii_eyebrow_A4.png",
        "Char_Data['hero']['mood'] == 'O1'", "kawaii/eyes/kawaii_eyebrow_O1.png",
        "Char_Data['hero']['mood'] == 'O2'", "kawaii/eyes/kawaii_eyebrow_O2.png",
        "Char_Data['hero']['mood'] == 'O3'", "kawaii/eyes/kawaii_eyebrow_O3.png",
        "Char_Data['hero']['mood'] == 'O4'", "kawaii/eyes/kawaii_eyebrow_O4.png",
        "True", "kawaii/eyes/kawaii_eyebrow_A1.png"
    ),
    )

image KAWAII HEADBG:
    ConditionSwitch(
        "Char_Data['hero']['wear'] == 'kawaii_school_swim'", "kawaii/head/school_swim/kawaii_head_bg_school_swim.png", 
        "Char_Data['hero']['wear'] == 'kawaii_school_sport'", "kawaii/head/school_sport/kawaii_head_bg_school_sport.png",
        "Char_Data['hero']['wear'] == 'kawaii_casual'", "kawaii/head/casual/kawaii_head_bg_casual.png", 
        "Char_Data['hero']['wear'] == 'kawaii_dressy'", "kawaii/head/dressy/kawaii_head_bg_dressy.png",
        "Char_Data['hero']['wear'] == 'kawaii_formal'", "kawaii/head/formal/kawaii_head_bg_formal.png",
        "Char_Data['hero']['wear'] == 'kawaii_home'", "kawaii/head/home/kawaii_head_bg_home.png",
        "Char_Data['hero']['wear'] == 'kawaii_school'", "kawaii/head/school/kawaii_head_bg_school.png",
        "Char_Data['hero']['wear'] == 'kawaii_sleep'", "kawaii/head/sleep/kawaii_head_bg_sleep.png",
        "Char_Data['hero']['wear'] == 'kawaii_soap'", "kawaii/head/soap/kawaii_head_bg_soap.png",
        "Char_Data['hero']['wear'] == 'kawaii_under'", "kawaii/head/under/kawaii_head_bg_under.png",
        "Char_Data['hero']['wear'] == 'kawaii_work'", "kawaii/head/work/kawaii_head_bg_work.png",
        "True", "kawaii/head/kawaii_head_bg_common.png"
    )
    zoom 1.5/Char_Data['hero']['size']
    xoffset int((Char_Data['hero']['size'] - 1.50) * 206)
    yoffset int((Char_Data['hero']['size'] - 1.50) * 275)

image KAWAII HEADFG:
    "KAWAII HEADFG PARTS"
    zoom 1.5/Char_Data['hero']['size']
    xoffset int((Char_Data['hero']['size'] - 1.50) * 206)
    yoffset int((Char_Data['hero']['size'] - 1.50) * 275)

image KAWAII PARTS = Composite(
    (720,1080),
    (0,0), "KAWAII HEADBG",
    (0,0), ConditionSwitch(
        "len(Char_Data['hero']['achiev']['wear']) > 0 and isinstance(Char_Data['hero']['achiev']['wear'][get_wear_var('hero')], str) and Char_Data['hero']['achiev']['wear'][get_wear_var('hero')].startswith('kawaii')", "kawaii/body_wear_phone/kawaii_body_1.png",
        "True", "kawaii/body_wear_phone/kawaii_body_0.png"
    ),
    (0,0), "KAWAII WEAR",
    (0,0), "KAWAII HEADFG",
    )

image KAWAII STYLE = Composite(
    (720,1080),
    (0,0), "KAWAII HEADBG",
    (0,0), ConditionSwitch(
        "len(Char_Data['hero']['achiev']['wear']) > 0 and isinstance(Char_Data['hero']['achiev']['wear'][get_wear_var('hero')], str) and Char_Data['hero']['achiev']['wear'][get_wear_var('hero')].startswith('kawaii')", "kawaii/body_wear_phone/kawaii_body_1.png",
        "True", "kawaii/body_wear_phone/kawaii_body_0.png"
    ),
    (0,0), ConditionSwitch(
        "len(Char_Data['hero']['achiev']['wear']) > 0 and Char_Data['hero']['achiev']['wear'][get_wear_var('hero')] == 'kawaii_home'", "kawaii/body_wear_phone/kawaii_body_wear_home.png",
        "len(Char_Data['hero']['achiev']['wear']) > 0 and Char_Data['hero']['achiev']['wear'][get_wear_var('hero')] == 'kawaii_under'", "kawaii/body_wear_phone/kawaii_body_wear_under.png",
        "len(Char_Data['hero']['achiev']['wear']) > 0 and Char_Data['hero']['achiev']['wear'][get_wear_var('hero')] == 'kawaii_sleep'", "kawaii/body_wear_phone/kawaii_body_wear_sleep.png",
        "len(Char_Data['hero']['achiev']['wear']) > 0 and Char_Data['hero']['achiev']['wear'][get_wear_var('hero')] == 'kawaii_casual'", "kawaii/body_wear_phone/kawaii_body_wear_casual.png",
        "len(Char_Data['hero']['achiev']['wear']) > 0 and Char_Data['hero']['achiev']['wear'][get_wear_var('hero')] == 'kawaii_school'", "kawaii/body_wear_phone/kawaii_body_wear_school.png",
        "len(Char_Data['hero']['achiev']['wear']) > 0 and Char_Data['hero']['achiev']['wear'][get_wear_var('hero')] == 'kawaii_school_swim'", "kawaii/body_wear_phone/kawaii_body_wear_school_swim.png",
        "len(Char_Data['hero']['achiev']['wear']) > 0 and Char_Data['hero']['achiev']['wear'][get_wear_var('hero')] == 'kawaii_school_sport'", "kawaii/body_wear_phone/kawaii_body_wear_school_sport.png",
        "len(Char_Data['hero']['achiev']['wear']) > 0 and Char_Data['hero']['achiev']['wear'][get_wear_var('hero')] == 'kawaii_soap'", "kawaii/body_wear_phone/kawaii_body_wear_soap.png",
        "len(Char_Data['hero']['achiev']['wear']) > 0 and Char_Data['hero']['achiev']['wear'][get_wear_var('hero')] == 'kawaii_work'", "kawaii/body_wear_phone/kawaii_body_wear_work.png",
        "len(Char_Data['hero']['achiev']['wear']) > 0 and Char_Data['hero']['achiev']['wear'][get_wear_var('hero')] == 'kawaii_dressy'", "kawaii/body_wear_phone/kawaii_body_wear_dressy.png",
        "len(Char_Data['hero']['achiev']['wear']) > 0 and Char_Data['hero']['achiev']['wear'][get_wear_var('hero')] == 'kawaii_formal'", "kawaii/body_wear_phone/kawaii_body_wear_formal.png",
        "True", Null()
    ),
    (0,0), "KAWAII HEADFG",
    )

image HERO STYLE DEFAULT = Composite(
    (720,1080),
    (0,0), ConditionSwitch(
        "Char_Data['hero']['body'] == 0", "images/Sprite/hero/hero body 0.webp",
        "Char_Data['hero']['body'] == 1", "images/Sprite/hero/hero body 1.webp",
        "True", "images/Sprite/hero/hero body 0.webp"
    ),
    (0,0), ConditionSwitch(
        "len(Char_Data['hero']['achiev']['wear']) > 0 and Char_Data['hero']['achiev']['wear'][get_wear_var('hero')] == 'home'", "images/Sprite/hero/hero body_wear home.webp",
        "len(Char_Data['hero']['achiev']['wear']) > 0 and Char_Data['hero']['achiev']['wear'][get_wear_var('hero')] == 'under'", "images/Sprite/hero/hero body_wear under.webp",
        "len(Char_Data['hero']['achiev']['wear']) > 0 and Char_Data['hero']['achiev']['wear'][get_wear_var('hero')] == 'sleep'", "images/Sprite/hero/hero body_wear sleep.webp",
        "len(Char_Data['hero']['achiev']['wear']) > 0 and Char_Data['hero']['achiev']['wear'][get_wear_var('hero')] == 'casual'", "images/Sprite/hero/hero body_wear casual.webp",
        "len(Char_Data['hero']['achiev']['wear']) > 0 and Char_Data['hero']['achiev']['wear'][get_wear_var('hero')] == 'school'", "images/Sprite/hero/hero body_wear school.webp",
        "len(Char_Data['hero']['achiev']['wear']) > 0 and Char_Data['hero']['achiev']['wear'][get_wear_var('hero')] == 'school_swim'", "images/Sprite/hero/hero body_wear school_swim.webp",
        "len(Char_Data['hero']['achiev']['wear']) > 0 and Char_Data['hero']['achiev']['wear'][get_wear_var('hero')] == 'school_sport'", "images/Sprite/hero/hero body_wear school_sport.webp",
        "len(Char_Data['hero']['achiev']['wear']) > 0 and Char_Data['hero']['achiev']['wear'][get_wear_var('hero')] == 'soap'", "images/Sprite/hero/hero body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "HERO HEADFG",
    (25,64), ConditionSwitch(
        "Char_Data['hero']['item']['hold_left'] == 0", "images/Sprite/_General/item_l 0.webp",
        "Char_Data['hero']['item']['hold_left'] == 1", "images/Sprite/_General/item_l 1.webp",
        "True", "images/Sprite/_General/item_l 0.webp"
    ),
    (-35,65), ConditionSwitch(
        "Char_Data['hero']['item']['hold_right'] == 0", "images/Sprite/_General/item_r 0.webp",
        "Char_Data['hero']['item']['hold_right'] == 1", "images/Sprite/_General/item_r 1.webp",
        "True", "images/Sprite/_General/item_r 0.webp"
    ),
    )

image HERO STYLE:
    ConditionSwitch(
       "len(Char_Data['hero']['achiev']['wear']) > 0 and isinstance(Char_Data['hero']['achiev']['wear'][get_wear_var('hero')], str) and Char_Data['hero']['achiev']['wear'][get_wear_var('hero')].startswith('kawaii')", "KAWAII STYLE",
       "(len(Char_Data['hero']['achiev']['wear']) > 0 and isinstance(Char_Data['hero']['achiev']['wear'][get_wear_var('hero')], str) and Char_Data['hero']['achiev']['wear'][get_wear_var('hero')].startswith('kawaii')) == False", "HERO STYLE DEFAULT"
    )

image HERO DEFAULT:
    "HERO PARTS"

image HERO KAWAII:    
    "KAWAII PARTS"

image HERO:
    ConditionSwitch(
       "len(Char_Data['hero']['achiev']['wear']) > 0 and isinstance(Char_Data['hero']['achiev']['wear'][get_wear_var('hero')], str) and Char_Data['hero']['achiev']['wear'][get_wear_var('hero')].startswith('kawaii')", "HERO KAWAII",
       "(len(Char_Data['hero']['achiev']['wear']) > 0 and isinstance(Char_Data['hero']['achiev']['wear'][get_wear_var('hero')], str) and Char_Data['hero']['achiev']['wear'][get_wear_var('hero')].startswith('kawaii')) == False", "HERO DEFAULT"
    )
    yalign 1.0
    ypos 1400
    zoom 0+(0.25+(1*Char_Data['hero']['size']))*(0.25+(1*Char_Data['hero']['size']))/2.5


# HRIV

image HRIV STYLE = Composite(
    (720,1080),
    (0,0), "HRIV HEADBG",
    (0,0), ConditionSwitch(
        "Char_Data['hriv']['body'] == 0", "images/Sprite/hriv/hriv body 0.webp",
        "Char_Data['hriv']['body'] == 1", "images/Sprite/hriv/hriv body 1.webp",
        "True", "images/Sprite/hriv/hriv body 0.webp"
    ),
    (0,0), ConditionSwitch(
        "len(Char_Data['hriv']['achiev']['wear']) > 0 and Char_Data['hriv']['achiev']['wear'][get_wear_var('hriv')] == 'home'", "images/Sprite/hriv/hriv body_wear home.webp",
        "len(Char_Data['hriv']['achiev']['wear']) > 0 and Char_Data['hriv']['achiev']['wear'][get_wear_var('hriv')] == 'under'", "images/Sprite/hriv/hriv body_wear under.webp",
        "len(Char_Data['hriv']['achiev']['wear']) > 0 and Char_Data['hriv']['achiev']['wear'][get_wear_var('hriv')] == 'sleep'", "images/Sprite/hriv/hriv body_wear sleep.webp",
        "len(Char_Data['hriv']['achiev']['wear']) > 0 and Char_Data['hriv']['achiev']['wear'][get_wear_var('hriv')] == 'casual'", "images/Sprite/hriv/hriv body_wear casual.webp",
        "len(Char_Data['hriv']['achiev']['wear']) > 0 and Char_Data['hriv']['achiev']['wear'][get_wear_var('hriv')] == 'school'", "images/Sprite/hriv/hriv body_wear school.webp",
        "len(Char_Data['hriv']['achiev']['wear']) > 0 and Char_Data['hriv']['achiev']['wear'][get_wear_var('hriv')] == 'school_swim'", "images/Sprite/hriv/hriv body_wear school_swim.webp",
        "len(Char_Data['hriv']['achiev']['wear']) > 0 and Char_Data['hriv']['achiev']['wear'][get_wear_var('hriv')] == 'school_sport'", "images/Sprite/hriv/hriv body_wear school_sport.webp",
        "len(Char_Data['hriv']['achiev']['wear']) > 0 and Char_Data['hriv']['achiev']['wear'][get_wear_var('hriv')] == 'soap'", "images/Sprite/hriv/hriv body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "HRIV HEADFG",
    (25,64), ConditionSwitch(
        "Char_Data['hriv']['item']['hold_left'] == 0", "images/Sprite/_General/item_l 0.webp",
        "Char_Data['hriv']['item']['hold_left'] == 1", "images/Sprite/_General/item_l 1.webp",
        "True", "images/Sprite/_General/item_l 0.webp"
    ),
    (-35,65), ConditionSwitch(
        "Char_Data['hriv']['item']['hold_right'] == 0", "images/Sprite/_General/item_r 0.webp",
        "Char_Data['hriv']['item']['hold_right'] == 1", "images/Sprite/_General/item_r 1.webp",
        "True", "images/Sprite/_General/item_r 0.webp"
    ),
    )

# HPRV

image HPRV STYLE = Composite(
    (720,1080),
    (0,0), "HPRV HEADBG",
    (0,0), "images/Sprite/hprv/hprv body 1.webp",
    (0,0), ConditionSwitch(
        "len(Char_Data['hprv']['achiev']['wear']) > 0 and Char_Data['hprv']['achiev']['wear'][get_wear_var('hprv')] == 'home'", "images/Sprite/hprv/hprv body_wear home.webp",
        "len(Char_Data['hprv']['achiev']['wear']) > 0 and Char_Data['hprv']['achiev']['wear'][get_wear_var('hprv')] == 'under'", "images/Sprite/hprv/hprv body_wear under.webp",
        "len(Char_Data['hprv']['achiev']['wear']) > 0 and Char_Data['hprv']['achiev']['wear'][get_wear_var('hprv')] == 'sleep'", "images/Sprite/hprv/hprv body_wear sleep.webp",
        "len(Char_Data['hprv']['achiev']['wear']) > 0 and Char_Data['hprv']['achiev']['wear'][get_wear_var('hprv')] == 'casual'", "images/Sprite/hprv/hprv body_wear casual.webp",
        "len(Char_Data['hprv']['achiev']['wear']) > 0 and Char_Data['hprv']['achiev']['wear'][get_wear_var('hprv')] == 'school'", "images/Sprite/hprv/hprv body_wear school.webp",
        "len(Char_Data['hprv']['achiev']['wear']) > 0 and Char_Data['hprv']['achiev']['wear'][get_wear_var('hprv')] == 'school_swim'", "images/Sprite/hprv/hprv body_wear school_swim.webp",
        "len(Char_Data['hprv']['achiev']['wear']) > 0 and Char_Data['hprv']['achiev']['wear'][get_wear_var('hprv')] == 'school_sport'", "images/Sprite/hprv/hprv body_wear school_sport.webp",
        "len(Char_Data['hprv']['achiev']['wear']) > 0 and Char_Data['hprv']['achiev']['wear'][get_wear_var('hprv')] == 'soap'", "images/Sprite/hprv/hprv body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "HPRV HEADFG",
    (-600,0), ConditionSwitch(
        "Char_Data['hprv']['item']['hold_left'] == 0", "images/Sprite/_General/item_l 0.webp",
        "Char_Data['hprv']['item']['hold_left'] == 1", "images/Sprite/_General/item_l 1.webp",
        "True", "images/Sprite/_General/item_l 0.webp"
    ),
    (-600,0), ConditionSwitch(
        "Char_Data['hprv']['item']['hold_right'] == 0", "images/Sprite/_General/item_r 0.webp",
        "Char_Data['hprv']['item']['hold_right'] == 1", "images/Sprite/_General/item_r 1.webp",
        "True", "images/Sprite/_General/item_r 0.webp"
    ),
    )

# HINE

image HINE STYLE = Composite(
    (720,1080),
    (0,0), "HINE HEADBG",
    (0,0), "images/Sprite/hine/hine body 0.webp",
    (0,0), ConditionSwitch(
        "len(Char_Data['hine']['achiev']['wear']) > 0 and Char_Data['hine']['achiev']['wear'][get_wear_var('hine')] == 'home'", "images/Sprite/hine/hine body_wear home.webp",
        "len(Char_Data['hine']['achiev']['wear']) > 0 and Char_Data['hine']['achiev']['wear'][get_wear_var('hine')] == 'under'", "images/Sprite/hine/hine body_wear under.webp",
        "len(Char_Data['hine']['achiev']['wear']) > 0 and Char_Data['hine']['achiev']['wear'][get_wear_var('hine')] == 'sleep'", "images/Sprite/hine/hine body_wear sleep.webp",
        "len(Char_Data['hine']['achiev']['wear']) > 0 and Char_Data['hine']['achiev']['wear'][get_wear_var('hine')] == 'casual'", "images/Sprite/hine/hine body_wear casual.webp",
        "len(Char_Data['hine']['achiev']['wear']) > 0 and Char_Data['hine']['achiev']['wear'][get_wear_var('hine')] == 'school'", "images/Sprite/hine/hine body_wear school.webp",
        "len(Char_Data['hine']['achiev']['wear']) > 0 and Char_Data['hine']['achiev']['wear'][get_wear_var('hine')] == 'school_swim'", "images/Sprite/hine/hine body_wear school_swim.webp",
        "len(Char_Data['hine']['achiev']['wear']) > 0 and Char_Data['hine']['achiev']['wear'][get_wear_var('hine')] == 'school_sport'", "images/Sprite/hine/hine body_wear school_sport.webp",
        "len(Char_Data['hine']['achiev']['wear']) > 0 and Char_Data['hine']['achiev']['wear'][get_wear_var('hine')] == 'soap'", "images/Sprite/hine/hine body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "HINE HEADFG",
    (-600,0), ConditionSwitch(
        "Char_Data['hine']['item']['hold_left'] == 0", "images/Sprite/_General/item_l 0.webp",
        "Char_Data['hine']['item']['hold_left'] == 1", "images/Sprite/_General/item_l 1.webp",
        "True", "images/Sprite/_General/item_l 0.webp"
    ),
    (-600,0), ConditionSwitch(
        "Char_Data['hine']['item']['hold_right'] == 0", "images/Sprite/_General/item_r 0.webp",
        "Char_Data['hine']['item']['hold_right'] == 1", "images/Sprite/_General/item_r 1.webp",
        "True", "images/Sprite/_General/item_r 0.webp"
    ),
    )

# WSIS

image WSIS STYLE = Composite(
    (720,1080),
    (0,0), "WSIS HEADBG",
    (0,0), ConditionSwitch(
        "len(Char_Data['wsis']['achiev']['wear']) > 0 and isinstance(Char_Data['wsis']['achiev']['wear'][a_menu_8], str)", "images/Sprite/wsis/wsis body 1.webp",
        "True", "images/Sprite/wsis/wsis body 0.webp"
    ),
    (0,0), ConditionSwitch(
        "len(Char_Data['wsis']['achiev']['wear']) > 0 and Char_Data['wsis']['achiev']['wear'][get_wear_var('wsis')] == 'home'", "images/Sprite/wsis/wsis body_wear home.webp",
        "len(Char_Data['wsis']['achiev']['wear']) > 0 and Char_Data['wsis']['achiev']['wear'][get_wear_var('wsis')] == 'under'", "images/Sprite/wsis/wsis body_wear under.webp",
        "len(Char_Data['wsis']['achiev']['wear']) > 0 and Char_Data['wsis']['achiev']['wear'][get_wear_var('wsis')] == 'sleep'", "images/Sprite/wsis/wsis body_wear sleep.webp",
        "len(Char_Data['wsis']['achiev']['wear']) > 0 and Char_Data['wsis']['achiev']['wear'][get_wear_var('wsis')] == 'casual'", "images/Sprite/wsis/wsis body_wear casual.webp",
        "len(Char_Data['wsis']['achiev']['wear']) > 0 and Char_Data['wsis']['achiev']['wear'][get_wear_var('wsis')] == 'school'", "images/Sprite/wsis/wsis body_wear school.webp",
        "len(Char_Data['wsis']['achiev']['wear']) > 0 and Char_Data['wsis']['achiev']['wear'][get_wear_var('wsis')] == 'school_swim'", "images/Sprite/wsis/wsis body_wear school_swim.webp",
        "len(Char_Data['wsis']['achiev']['wear']) > 0 and Char_Data['wsis']['achiev']['wear'][get_wear_var('wsis')] == 'school_sport'", "images/Sprite/wsis/wsis body_wear school_sport.webp",
        "len(Char_Data['wsis']['achiev']['wear']) > 0 and Char_Data['wsis']['achiev']['wear'][get_wear_var('wsis')] == 'soap'", "images/Sprite/wsis/wsis body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "WSIS HEADFG",
    )

# WNEI

image WNEI STYLE = Composite(
    (720,1080),
    (0,0), "WNEI HEADBG",
    (0,0), ConditionSwitch(
        "isinstance(Char_Data['wnei']['wear'], str)", "images/Sprite/wnei/wnei body 1.webp",
        "True", "images/Sprite/wnei/wnei body 0.webp"
    ),
    (0,0), ConditionSwitch(
        "len(Char_Data['wnei']['achiev']['wear']) > 0 and Char_Data['wnei']['achiev']['wear'][get_wear_var('wnei')] == 'home'", "images/Sprite/wnei/wnei body_wear home.webp",
        "len(Char_Data['wnei']['achiev']['wear']) > 0 and Char_Data['wnei']['achiev']['wear'][get_wear_var('wnei')] == 'under'", "images/Sprite/wnei/wnei body_wear under.webp",
        "len(Char_Data['wnei']['achiev']['wear']) > 0 and Char_Data['wnei']['achiev']['wear'][get_wear_var('wnei')] == 'sleep'", "images/Sprite/wnei/wnei body_wear sleep.webp",
        "len(Char_Data['wnei']['achiev']['wear']) > 0 and Char_Data['wnei']['achiev']['wear'][get_wear_var('wnei')] == 'casual'", "images/Sprite/wnei/wnei body_wear casual.webp",
        "len(Char_Data['wnei']['achiev']['wear']) > 0 and Char_Data['wnei']['achiev']['wear'][get_wear_var('wnei')] == 'school'", "images/Sprite/wnei/wnei body_wear school.webp",
        "len(Char_Data['wnei']['achiev']['wear']) > 0 and Char_Data['wnei']['achiev']['wear'][get_wear_var('wnei')] == 'school_swim'", "images/Sprite/wnei/wnei body_wear school_swim.webp",
        "len(Char_Data['wnei']['achiev']['wear']) > 0 and Char_Data['wnei']['achiev']['wear'][get_wear_var('wnei')] == 'school_sport'", "images/Sprite/wnei/wnei body_wear school_sport.webp",
        "len(Char_Data['wnei']['achiev']['wear']) > 0 and Char_Data['wnei']['achiev']['wear'][get_wear_var('wnei')] == 'soap'", "images/Sprite/wnei/wnei body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "WNEI HEADFG",
    )

# WMOM

image WMOM STYLE = Composite(
    (720,1080),
    (0,0), "WMOM HEADBG",
    (0,0), ConditionSwitch(
        "isinstance(Char_Data['wmom']['wear'], str)", "images/Sprite/wmom/wmom body 1.webp",
        "True", "images/Sprite/wmom/wmom body 0.webp"
    ),
    (0,0), ConditionSwitch(
        "len(Char_Data['wmom']['achiev']['wear']) > 0 and Char_Data['wmom']['achiev']['wear'][get_wear_var('wmom')] == 'home'", "images/Sprite/wmom/wmom body_wear home.webp",
        "len(Char_Data['wmom']['achiev']['wear']) > 0 and Char_Data['wmom']['achiev']['wear'][get_wear_var('wmom')] == 'under'", "images/Sprite/wmom/wmom body_wear under.webp",
        "len(Char_Data['wmom']['achiev']['wear']) > 0 and Char_Data['wmom']['achiev']['wear'][get_wear_var('wmom')] == 'sleep'", "images/Sprite/wmom/wmom body_wear sleep.webp",
        "len(Char_Data['wmom']['achiev']['wear']) > 0 and Char_Data['wmom']['achiev']['wear'][get_wear_var('wmom')] == 'casual'", "images/Sprite/wmom/wmom body_wear casual.webp",
        "len(Char_Data['wmom']['achiev']['wear']) > 0 and Char_Data['wmom']['achiev']['wear'][get_wear_var('wmom')] == 'school'", "images/Sprite/wmom/wmom body_wear school.webp",
        "len(Char_Data['wmom']['achiev']['wear']) > 0 and Char_Data['wmom']['achiev']['wear'][get_wear_var('wmom')] == 'school_swim'", "images/Sprite/wmom/wmom body_wear school_swim.webp",
        "len(Char_Data['wmom']['achiev']['wear']) > 0 and Char_Data['wmom']['achiev']['wear'][get_wear_var('wmom')] == 'school_sport'", "images/Sprite/wmom/wmom body_wear school_sport.webp",
        "len(Char_Data['wmom']['achiev']['wear']) > 0 and Char_Data['wmom']['achiev']['wear'][get_wear_var('wmom')] == 'soap'", "images/Sprite/wmom/wmom body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "WMOM HEADFG",
    (-600,0), ConditionSwitch(
        "Char_Data['wmom']['item']['hold_left'] == 0", "images/Sprite/_General/item_l 0.webp",
        "Char_Data['wmom']['item']['hold_left'] == 1", "images/Sprite/_General/item_l 1.webp",
        "True", "images/Sprite/_General/item_l 0.webp"
    ),
    (-600,0), ConditionSwitch(
        "Char_Data['wmom']['item']['hold_right'] == 0", "images/Sprite/_General/item_r 0.webp",
        "Char_Data['wmom']['item']['hold_right'] == 1", "images/Sprite/_General/item_r 1.webp",
        "True", "images/Sprite/_General/item_r 0.webp"
    ),
    )

# WGMA

image WGMA STYLE = Composite(
    (720,1080),
    (0,0), "WGMA HEADBG",
    (0,0), "images/Sprite/wgma/wgma body 1.webp",
    (0,0), ConditionSwitch(
        "len(Char_Data['wgma']['achiev']['wear']) > 0 and Char_Data['wgma']['achiev']['wear'][get_wear_var('wgma')] == 'home'", "images/Sprite/wgma/wgma body_wear home.webp",
        "len(Char_Data['wgma']['achiev']['wear']) > 0 and Char_Data['wgma']['achiev']['wear'][get_wear_var('wgma')] == 'under'", "images/Sprite/wgma/wgma body_wear under.webp",
        "len(Char_Data['wgma']['achiev']['wear']) > 0 and Char_Data['wgma']['achiev']['wear'][get_wear_var('wgma')] == 'sleep'", "images/Sprite/wgma/wgma body_wear sleep.webp",
        "len(Char_Data['wgma']['achiev']['wear']) > 0 and Char_Data['wgma']['achiev']['wear'][get_wear_var('wgma')] == 'casual'", "images/Sprite/wgma/wgma body_wear casual.webp",
        "len(Char_Data['wgma']['achiev']['wear']) > 0 and Char_Data['wgma']['achiev']['wear'][get_wear_var('wgma')] == 'school'", "images/Sprite/wgma/wgma body_wear school.webp",
        "len(Char_Data['wgma']['achiev']['wear']) > 0 and Char_Data['wgma']['achiev']['wear'][get_wear_var('wgma')] == 'school_swim'", "images/Sprite/wgma/wgma body_wear school_swim.webp",
        "len(Char_Data['wgma']['achiev']['wear']) > 0 and Char_Data['wgma']['achiev']['wear'][get_wear_var('wgma')] == 'school_sport'", "images/Sprite/wgma/wgma body_wear school_sport.webp",
        "len(Char_Data['wgma']['achiev']['wear']) > 0 and Char_Data['wgma']['achiev']['wear'][get_wear_var('wgma')] == 'soap'", "images/Sprite/wgma/wgma body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "WGMA HEADFG",
    (-600,0), ConditionSwitch(
        "Char_Data['wgma']['item']['hold_left'] == 0", "images/Sprite/_General/item_l 0.webp",
        "Char_Data['wgma']['item']['hold_left'] == 1", "images/Sprite/_General/item_l 1.webp",
        "True", "images/Sprite/_General/item_l 0.webp"
    ),
    (-600,0), ConditionSwitch(
        "Char_Data['wgma']['item']['hold_right'] == 0", "images/Sprite/_General/item_r 0.webp",
        "Char_Data['wgma']['item']['hold_right'] == 1", "images/Sprite/_General/item_r 1.webp",
        "True", "images/Sprite/_General/item_r 0.webp"
    ),
    )

# WCOU

image WCOU STYLE = Composite(
    (720,1080),
    (0,0), "WCOU HEADBG",
    (0,0), ConditionSwitch(
        "isinstance(Char_Data['wcou']['wear'], str)", "images/Sprite/wcou/wcou body 1.webp",
        "True", "images/Sprite/wcou/wcou body 1.webp"
    ),
    (0,0), ConditionSwitch(
        "len(Char_Data['wcou']['achiev']['wear']) > 0 and Char_Data['wcou']['achiev']['wear'][get_wear_var('wcou')] == 'home'", "images/Sprite/wcou/wcou body_wear home.webp",
        "len(Char_Data['wcou']['achiev']['wear']) > 0 and Char_Data['wcou']['achiev']['wear'][get_wear_var('wcou')] == 'under'", "images/Sprite/wcou/wcou body_wear under.webp",
        "len(Char_Data['wcou']['achiev']['wear']) > 0 and Char_Data['wcou']['achiev']['wear'][get_wear_var('wcou')] == 'sleep'", "images/Sprite/wcou/wcou body_wear sleep.webp",
        "len(Char_Data['wcou']['achiev']['wear']) > 0 and Char_Data['wcou']['achiev']['wear'][get_wear_var('wcou')] == 'casual'", "images/Sprite/wcou/wcou body_wear casual.webp",
        "len(Char_Data['wcou']['achiev']['wear']) > 0 and Char_Data['wcou']['achiev']['wear'][get_wear_var('wcou')] == 'work'", "images/Sprite/wcou/wcou body_wear work_1.webp",
        "len(Char_Data['wcou']['achiev']['wear']) > 0 and Char_Data['wcou']['achiev']['wear'][get_wear_var('wcou')] == 'work2'", "images/Sprite/wcou/wcou body_wear work_2.webp",
        "True", Null()
    ),
    (0,0), "WCOU HEADFG",
    (-600,0), ConditionSwitch(
        "Char_Data['wcou']['item']['hold_left'] == 0", "images/Sprite/_General/item_l 0.webp",
        "Char_Data['wcou']['item']['hold_left'] == 1", "images/Sprite/_General/item_l 1.webp",
        "True", "images/Sprite/_General/item_l 0.webp"
    ),
    (-600,0), ConditionSwitch(
        "Char_Data['wcou']['item']['hold_right'] == 0", "images/Sprite/_General/item_r 0.webp",
        "Char_Data['wcou']['item']['hold_right'] == 1", "images/Sprite/_General/item_r 1.webp",
        "True", "images/Sprite/_General/item_r 0.webp"
    ),
    )

# WPRE

image WPRE STYLE = Composite(
    (720,1080),
    (0,0), "WPRE HEADBG",
    (0,0), ConditionSwitch(
        "isinstance(Char_Data['wpre']['wear'], str)", "images/Sprite/wpre/wpre body 1.webp",
        "True", "images/Sprite/wpre/wpre body 0.webp"
    ),
    (0,0), ConditionSwitch(
        "len(Char_Data['wpre']['achiev']['wear']) > 0 and Char_Data['wpre']['achiev']['wear'][get_wear_var('wpre')] == 'home'", "images/Sprite/wpre/wpre body_wear home.webp",
        "len(Char_Data['wpre']['achiev']['wear']) > 0 and Char_Data['wpre']['achiev']['wear'][get_wear_var('wpre')] == 'under'", "images/Sprite/wpre/wpre body_wear under.webp",
        "len(Char_Data['wpre']['achiev']['wear']) > 0 and Char_Data['wpre']['achiev']['wear'][get_wear_var('wpre')] == 'sleep'", "images/Sprite/wpre/wpre body_wear sleep.webp",
        "len(Char_Data['wpre']['achiev']['wear']) > 0 and Char_Data['wpre']['achiev']['wear'][get_wear_var('wpre')] == 'casual'", "images/Sprite/wpre/wpre body_wear casual.webp",
        "len(Char_Data['wpre']['achiev']['wear']) > 0 and Char_Data['wpre']['achiev']['wear'][get_wear_var('wpre')] == 'school'", "images/Sprite/wpre/wpre body_wear school.webp",
        "len(Char_Data['wpre']['achiev']['wear']) > 0 and Char_Data['wpre']['achiev']['wear'][get_wear_var('wpre')] == 'school_swim'", "images/Sprite/wpre/wpre body_wear school_swim.webp",
        "len(Char_Data['wpre']['achiev']['wear']) > 0 and Char_Data['wpre']['achiev']['wear'][get_wear_var('wpre')] == 'school_sport'", "images/Sprite/wpre/wpre body_wear school_sport.webp",
        "len(Char_Data['wpre']['achiev']['wear']) > 0 and Char_Data['wpre']['achiev']['wear'][get_wear_var('wpre')] == 'soap'", "images/Sprite/wpre/wpre body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "WPRE HEADFG",
    )

# WGAL

image WGAL STYLE = Composite(
    (720,1080),
    (0,0), "WGAL HEADBG",
    (0,0), ConditionSwitch(
        "isinstance(Char_Data['wgal']['wear'], str)", "images/Sprite/wgal/wgal body 1.webp",
        "True", "images/Sprite/wgal/wgal body 0.webp"
    ),
    (0,0), ConditionSwitch(
        "len(Char_Data['wgal']['achiev']['wear']) > 0 and Char_Data['wgal']['achiev']['wear'][get_wear_var('wgal')] == 'home'", "images/Sprite/wgal/wgal body_wear home.webp",
        "len(Char_Data['wgal']['achiev']['wear']) > 0 and Char_Data['wgal']['achiev']['wear'][get_wear_var('wgal')] == 'under'", "images/Sprite/wgal/wgal body_wear under.webp",
        "len(Char_Data['wgal']['achiev']['wear']) > 0 and Char_Data['wgal']['achiev']['wear'][get_wear_var('wgal')] == 'sleep'", "images/Sprite/wgal/wgal body_wear sleep.webp",
        "len(Char_Data['wgal']['achiev']['wear']) > 0 and Char_Data['wgal']['achiev']['wear'][get_wear_var('wgal')] == 'casual'", "images/Sprite/wgal/wgal body_wear casual.webp",
        "len(Char_Data['wgal']['achiev']['wear']) > 0 and Char_Data['wgal']['achiev']['wear'][get_wear_var('wgal')] == 'school'", "images/Sprite/wgal/wgal body_wear school.webp",
        "len(Char_Data['wgal']['achiev']['wear']) > 0 and Char_Data['wgal']['achiev']['wear'][get_wear_var('wgal')] == 'school_swim'", "images/Sprite/wgal/wgal body_wear school_swim.webp",
        "len(Char_Data['wgal']['achiev']['wear']) > 0 and Char_Data['wgal']['achiev']['wear'][get_wear_var('wgal')] == 'school_sport'", "images/Sprite/wgal/wgal body_wear school_sport.webp",
        "len(Char_Data['wgal']['achiev']['wear']) > 0 and Char_Data['wgal']['achiev']['wear'][get_wear_var('wgal')] == 'soap'", "images/Sprite/wgal/wgal body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "WGAL HEADFG",
    (-600,0), ConditionSwitch(
        "Char_Data['wgal']['item']['hold_left'] == 0", "images/Sprite/_General/item_l 0.webp",
        "Char_Data['wgal']['item']['hold_left'] == 1", "images/Sprite/_General/item_l 1.webp",
        "True", "images/Sprite/_General/item_l 0.webp"
    ),
    (-600,0), ConditionSwitch(
        "Char_Data['wgal']['item']['hold_right'] == 0", "images/Sprite/_General/item_r 0.webp",
        "Char_Data['wgal']['item']['hold_right'] == 1", "images/Sprite/_General/item_r 1.webp",
        "True", "images/Sprite/_General/item_r 0.webp"
    ),
    )

# WOTA

image WOTA STYLE = Composite(
    (720,1080),
    (0,0), "WOTA HEADBG",
    (0,0), ConditionSwitch(
        "isinstance(Char_Data['wota']['wear'], str)", "images/Sprite/wota/wota body 1.webp",
        "True", "images/Sprite/wota/wota body 0.webp"
    ),
    (0,0), ConditionSwitch(
        "len(Char_Data['wota']['achiev']['wear']) > 0 and Char_Data['wota']['achiev']['wear'][get_wear_var('wota')] == 'home'", "images/Sprite/wota/wota body_wear home.webp",
        "len(Char_Data['wota']['achiev']['wear']) > 0 and Char_Data['wota']['achiev']['wear'][get_wear_var('wota')] == 'under'", "images/Sprite/wota/wota body_wear under.webp",
        "len(Char_Data['wota']['achiev']['wear']) > 0 and Char_Data['wota']['achiev']['wear'][get_wear_var('wota')] == 'sleep'", "images/Sprite/wota/wota body_wear sleep.webp",
        "len(Char_Data['wota']['achiev']['wear']) > 0 and Char_Data['wota']['achiev']['wear'][get_wear_var('wota')] == 'casual'", "images/Sprite/wota/wota body_wear casual.webp",
        "len(Char_Data['wota']['achiev']['wear']) > 0 and Char_Data['wota']['achiev']['wear'][get_wear_var('wota')] == 'school'", "images/Sprite/wota/wota body_wear school.webp",
        "len(Char_Data['wota']['achiev']['wear']) > 0 and Char_Data['wota']['achiev']['wear'][get_wear_var('wota')] == 'school_swim'", "images/Sprite/wota/wota body_wear school_swim.webp",
        "len(Char_Data['wota']['achiev']['wear']) > 0 and Char_Data['wota']['achiev']['wear'][get_wear_var('wota')] == 'school_sport'", "images/Sprite/wota/wota body_wear school_sport.webp",
        "len(Char_Data['wota']['achiev']['wear']) > 0 and Char_Data['wota']['achiev']['wear'][get_wear_var('wota')] == 'soap'", "images/Sprite/wota/wota body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "WOTA HEADFG",
    (-600,0), ConditionSwitch(
        "Char_Data['wota']['item']['hold_left'] == 0", "images/Sprite/_General/item_l 0.webp",
        "Char_Data['wota']['item']['hold_left'] == 1", "images/Sprite/_General/item_l 1.webp",
        "True", "images/Sprite/_General/item_l 0.webp"
    ),
    (-600,0), ConditionSwitch(
        "Char_Data['wota']['item']['hold_right'] == 0", "images/Sprite/_General/item_r 0.webp",
        "Char_Data['wota']['item']['hold_right'] == 1", "images/Sprite/_General/item_r 1.webp",
        "True", "images/Sprite/_General/item_r 0.webp"
    ),
    )

# WDIS

image WDIS STYLE = Composite(
    (720,1080),
    (0,0), "WDIS HEADBG",
    (0,0), ConditionSwitch(
        "isinstance(Char_Data['wdis']['wear'], str)", "images/Sprite/wdis/wdis body 1.webp",
        "True", "images/Sprite/wdis/wdis body 0.webp"
    ),
    (0,0), ConditionSwitch(
        "len(Char_Data['wdis']['achiev']['wear']) > 0 and Char_Data['wdis']['achiev']['wear'][get_wear_var('wdis')] == 'home'", "images/Sprite/wdis/wdis body_wear home.webp",
        "len(Char_Data['wdis']['achiev']['wear']) > 0 and Char_Data['wdis']['achiev']['wear'][get_wear_var('wdis')] == 'under'", "images/Sprite/wdis/wdis body_wear under.webp",
        "len(Char_Data['wdis']['achiev']['wear']) > 0 and Char_Data['wdis']['achiev']['wear'][get_wear_var('wdis')] == 'sleep'", "images/Sprite/wdis/wdis body_wear sleep.webp",
        "len(Char_Data['wdis']['achiev']['wear']) > 0 and Char_Data['wdis']['achiev']['wear'][get_wear_var('wdis')] == 'casual'", "images/Sprite/wdis/wdis body_wear casual.webp",
        "len(Char_Data['wdis']['achiev']['wear']) > 0 and Char_Data['wdis']['achiev']['wear'][get_wear_var('wdis')] == 'school'", "images/Sprite/wdis/wdis body_wear school.webp",
        "len(Char_Data['wdis']['achiev']['wear']) > 0 and Char_Data['wdis']['achiev']['wear'][get_wear_var('wdis')] == 'school_swim'", "images/Sprite/wdis/wdis body_wear school_swim.webp",
        "len(Char_Data['wdis']['achiev']['wear']) > 0 and Char_Data['wdis']['achiev']['wear'][get_wear_var('wdis')] == 'school_sport'", "images/Sprite/wdis/wdis body_wear school_sport.webp",
        "len(Char_Data['wdis']['achiev']['wear']) > 0 and Char_Data['wdis']['achiev']['wear'][get_wear_var('wdis')] == 'soap'", "images/Sprite/wdis/wdis body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "WDIS HEADFG",
    (-600,0), ConditionSwitch(
        "Char_Data['wdis']['item']['hold_left'] == 0", "images/Sprite/_General/item_l 0.webp",
        "Char_Data['wdis']['item']['hold_left'] == 1", "images/Sprite/_General/item_l 1.webp",
        "True", "images/Sprite/_General/item_l 0.webp"
    ),
    (-600,0), ConditionSwitch(
        "Char_Data['wdis']['item']['hold_right'] == 0", "images/Sprite/_General/item_r 0.webp",
        "Char_Data['wdis']['item']['hold_right'] == 1", "images/Sprite/_General/item_r 1.webp",
        "True", "images/Sprite/_General/item_r 0.webp"
    ),
    )

# WRIC

image WRIC STYLE = Composite(
    (720,1080),
    (0,0), "WRIC HEADBG",
    (0,0), "images/Sprite/wric/wric body.webp",
    (0,0), ConditionSwitch(
        "len(Char_Data['wric']['achiev']['wear']) > 0 and Char_Data['wric']['achiev']['wear'][get_wear_var('wric')] == 'home'", "images/Sprite/wric/wric body_wear home.webp",
        "len(Char_Data['wric']['achiev']['wear']) > 0 and Char_Data['wric']['achiev']['wear'][get_wear_var('wric')] == 'under'", "images/Sprite/wric/wric body_wear under.webp",
        "len(Char_Data['wric']['achiev']['wear']) > 0 and Char_Data['wric']['achiev']['wear'][get_wear_var('wric')] == 'sleep'", "images/Sprite/wric/wric body_wear sleep.webp",
        "len(Char_Data['wric']['achiev']['wear']) > 0 and Char_Data['wric']['achiev']['wear'][get_wear_var('wric')] == 'casual'", "images/Sprite/wric/wric body_wear casual.webp",
        "len(Char_Data['wric']['achiev']['wear']) > 0 and Char_Data['wric']['achiev']['wear'][get_wear_var('wric')] == 'school'", "images/Sprite/wric/wric body_wear school.webp",
        "len(Char_Data['wric']['achiev']['wear']) > 0 and Char_Data['wric']['achiev']['wear'][get_wear_var('wric')] == 'school_swim'", "images/Sprite/wric/wric body_wear school_swim.webp",
        "len(Char_Data['wric']['achiev']['wear']) > 0 and Char_Data['wric']['achiev']['wear'][get_wear_var('wric')] == 'school_sport'", "images/Sprite/wric/wric body_wear school_sport.webp",
        "len(Char_Data['wric']['achiev']['wear']) > 0 and Char_Data['wric']['achiev']['wear'][get_wear_var('wric')] == 'soap'", "images/Sprite/wric/wric body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "WRIC HEADFG",
    )

# WUZA

image WUZA STYLE = Composite(
    (720,1080),
    (0,0), "WUZA HEADBG",
    (0,0), ConditionSwitch(
        "isinstance(Char_Data['wuza']['wear'], str)", "images/Sprite/wuza/wuza body 1.webp",
        "True", "images/Sprite/wuza/wuza body 0.webp"
    ),
    (0,0), ConditionSwitch(
        "len(Char_Data['wuza']['achiev']['wear']) > 0 and Char_Data['wuza']['achiev']['wear'][get_wear_var('wuza')] == 'home'", "images/Sprite/wuza/wuza body_wear home.webp",
        "len(Char_Data['wuza']['achiev']['wear']) > 0 and Char_Data['wuza']['achiev']['wear'][get_wear_var('wuza')] == 'under'", "images/Sprite/wuza/wuza body_wear under.webp",
        "len(Char_Data['wuza']['achiev']['wear']) > 0 and Char_Data['wuza']['achiev']['wear'][get_wear_var('wuza')] == 'sleep'", "images/Sprite/wuza/wuza body_wear sleep.webp",
        "len(Char_Data['wuza']['achiev']['wear']) > 0 and Char_Data['wuza']['achiev']['wear'][get_wear_var('wuza')] == 'casual'", "images/Sprite/wuza/wuza body_wear casual.webp",
        "len(Char_Data['wuza']['achiev']['wear']) > 0 and Char_Data['wuza']['achiev']['wear'][get_wear_var('wuza')] == 'school'", "images/Sprite/wuza/wuza body_wear school.webp",
        "len(Char_Data['wuza']['achiev']['wear']) > 0 and Char_Data['wuza']['achiev']['wear'][get_wear_var('wuza')] == 'school_swim'", "images/Sprite/wuza/wuza body_wear school_swim.webp",
        "len(Char_Data['wuza']['achiev']['wear']) > 0 and Char_Data['wuza']['achiev']['wear'][get_wear_var('wuza')] == 'school_sport'", "images/Sprite/wuza/wuza body_wear school_sport.webp",
        "len(Char_Data['wuza']['achiev']['wear']) > 0 and Char_Data['wuza']['achiev']['wear'][get_wear_var('wuza')] == 'soap'", "images/Sprite/wuza/wuza body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "WUZA HEADFG",
    (-600,0), ConditionSwitch(
        "Char_Data['wuza']['item']['hold_left'] == 0", "images/Sprite/_General/item_l 0.webp",
        "Char_Data['wuza']['item']['hold_left'] == 1", "images/Sprite/_General/item_l 1.webp",
        "True", "images/Sprite/_General/item_l 0.webp"
    ),
    (-600,0), ConditionSwitch(
        "Char_Data['wuza']['item']['hold_right'] == 0", "images/Sprite/_General/item_r 0.webp",
        "Char_Data['wuza']['item']['hold_right'] == 1", "images/Sprite/_General/item_r 1.webp",
        "True", "images/Sprite/_General/item_r 0.webp"
    ),
    )

# WLAZ

image WLAZ STYLE = Composite(
    (720,1080),
    (0,0), "WLAZ HEADBG",
    (0,0), ConditionSwitch(
        "isinstance(Char_Data['wlaz']['wear'], str)", "images/Sprite/wlaz/wlaz body 1.webp",
        "True", "images/Sprite/wlaz/wlaz body 0.webp"
    ),
    (0,0), ConditionSwitch(
        "len(Char_Data['wlaz']['achiev']['wear']) > 0 and Char_Data['wlaz']['achiev']['wear'][get_wear_var('wlaz')] == 'home'", "images/Sprite/wlaz/wlaz body_wear home.webp",
        "len(Char_Data['wlaz']['achiev']['wear']) > 0 and Char_Data['wlaz']['achiev']['wear'][get_wear_var('wlaz')] == 'under'", "images/Sprite/wlaz/wlaz body_wear under.webp",
        "len(Char_Data['wlaz']['achiev']['wear']) > 0 and Char_Data['wlaz']['achiev']['wear'][get_wear_var('wlaz')] == 'sleep'", "images/Sprite/wlaz/wlaz body_wear sleep.webp",
        "len(Char_Data['wlaz']['achiev']['wear']) > 0 and Char_Data['wlaz']['achiev']['wear'][get_wear_var('wlaz')] == 'casual'", "images/Sprite/wlaz/wlaz body_wear casual.webp",
        "len(Char_Data['wlaz']['achiev']['wear']) > 0 and Char_Data['wlaz']['achiev']['wear'][get_wear_var('wlaz')] == 'school'", "images/Sprite/wlaz/wlaz body_wear school.webp",
        "len(Char_Data['wlaz']['achiev']['wear']) > 0 and Char_Data['wlaz']['achiev']['wear'][get_wear_var('wlaz')] == 'school_swim'", "images/Sprite/wlaz/wlaz body_wear school_swim.webp",
        "len(Char_Data['wlaz']['achiev']['wear']) > 0 and Char_Data['wlaz']['achiev']['wear'][get_wear_var('wlaz')] == 'school_sport'", "images/Sprite/wlaz/wlaz body_wear school_sport.webp",
        "len(Char_Data['wlaz']['achiev']['wear']) > 0 and Char_Data['wlaz']['achiev']['wear'][get_wear_var('wlaz')] == 'soap'", "images/Sprite/wlaz/wlaz body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "WLAZ HEADFG",
    (-600,0), ConditionSwitch(
        "Char_Data['wlaz']['item']['hold_left'] == 0", "images/Sprite/_General/item_l 0.webp",
        "Char_Data['wlaz']['item']['hold_left'] == 1", "images/Sprite/_General/item_l 1.webp",
        "True", "images/Sprite/_General/item_l 0.webp"
    ),
    (-600,0), ConditionSwitch(
        "Char_Data['wlaz']['item']['hold_right'] == 0", "images/Sprite/_General/item_r 0.webp",
        "Char_Data['wlaz']['item']['hold_right'] == 1", "images/Sprite/_General/item_r 1.webp",
        "True", "images/Sprite/_General/item_r 0.webp"
    ),
    )

# WDEL

image WDEL STYLE = Composite(
    (720,1080),
    (0,0), "WDEL HEADBG",
    (0,0), ConditionSwitch(
        "isinstance(Char_Data['wdel']['wear'], str)", "images/Sprite/wdel/wdel body 1.webp",
        "True", "images/Sprite/wdel/wdel body 0.webp"
    ),
    (0,0), ConditionSwitch(
        "len(Char_Data['wdel']['achiev']['wear']) > 0 and Char_Data['wdel']['achiev']['wear'][get_wear_var('wdel')] == 'home'", "images/Sprite/wdel/wdel body_wear home.webp",
        "len(Char_Data['wdel']['achiev']['wear']) > 0 and Char_Data['wdel']['achiev']['wear'][get_wear_var('wdel')] == 'under'", "images/Sprite/wdel/wdel body_wear under.webp",
        "len(Char_Data['wdel']['achiev']['wear']) > 0 and Char_Data['wdel']['achiev']['wear'][get_wear_var('wdel')] == 'sleep'", "images/Sprite/wdel/wdel body_wear sleep.webp",
        "len(Char_Data['wdel']['achiev']['wear']) > 0 and Char_Data['wdel']['achiev']['wear'][get_wear_var('wdel')] == 'casual'", "images/Sprite/wdel/wdel body_wear casual.webp",
        "len(Char_Data['wdel']['achiev']['wear']) > 0 and Char_Data['wdel']['achiev']['wear'][get_wear_var('wdel')] == 'school'", "images/Sprite/wdel/wdel body_wear school.webp",
        "len(Char_Data['wdel']['achiev']['wear']) > 0 and Char_Data['wdel']['achiev']['wear'][get_wear_var('wdel')] == 'school_swim'", "images/Sprite/wdel/wdel body_wear school_swim.webp",
        "len(Char_Data['wdel']['achiev']['wear']) > 0 and Char_Data['wdel']['achiev']['wear'][get_wear_var('wdel')] == 'school_sport'", "images/Sprite/wdel/wdel body_wear school_sport.webp",
        "len(Char_Data['wdel']['achiev']['wear']) > 0 and Char_Data['wdel']['achiev']['wear'][get_wear_var('wdel')] == 'soap'", "images/Sprite/wdel/wdel body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "WDEL HEADFG",
    (-600,0), ConditionSwitch(
        "Char_Data['wdel']['item']['hold_left'] == 0", "images/Sprite/_General/item_l 0.webp",
        "Char_Data['wdel']['item']['hold_left'] == 1", "images/Sprite/_General/item_l 1.webp",
        "True", "images/Sprite/_General/item_l 0.webp"
    ),
    (-600,0), ConditionSwitch(
        "Char_Data['wdel']['item']['hold_right'] == 0", "images/Sprite/_General/item_r 0.webp",
        "Char_Data['wdel']['item']['hold_right'] == 1", "images/Sprite/_General/item_r 1.webp",
        "True", "images/Sprite/_General/item_r 0.webp"
    ),
    )

# WGOT

image WGOT STYLE = Composite(
    (720,1080),
    (0,0), "WGOT HEADBG",
    (0,0), ConditionSwitch(
        "isinstance(Char_Data['wgot']['wear'], str)", "images/Sprite/wgot/wgot body 1.webp",
        "True", "images/Sprite/wgot/wgot body 0.webp"
    ),
    (0,0), ConditionSwitch(
        "len(Char_Data['wgot']['achiev']['wear']) > 0 and Char_Data['wgot']['achiev']['wear'][get_wear_var('wgot')] == 'home'", "images/Sprite/wgot/wgot body_wear home.webp",
        "len(Char_Data['wgot']['achiev']['wear']) > 0 and Char_Data['wgot']['achiev']['wear'][get_wear_var('wgot')] == 'under'", "images/Sprite/wgot/wgot body_wear under.webp",
        "len(Char_Data['wgot']['achiev']['wear']) > 0 and Char_Data['wgot']['achiev']['wear'][get_wear_var('wgot')] == 'sleep'", "images/Sprite/wgot/wgot body_wear sleep.webp",
        "len(Char_Data['wgot']['achiev']['wear']) > 0 and Char_Data['wgot']['achiev']['wear'][get_wear_var('wgot')] == 'casual'", "images/Sprite/wgot/wgot body_wear casual.webp",
        "len(Char_Data['wgot']['achiev']['wear']) > 0 and Char_Data['wgot']['achiev']['wear'][get_wear_var('wgot')] == 'school'", "images/Sprite/wgot/wgot body_wear school.webp",
        "len(Char_Data['wgot']['achiev']['wear']) > 0 and Char_Data['wgot']['achiev']['wear'][get_wear_var('wgot')] == 'school_swim'", "images/Sprite/wgot/wgot body_wear school_swim.webp",
        "len(Char_Data['wgot']['achiev']['wear']) > 0 and Char_Data['wgot']['achiev']['wear'][get_wear_var('wgot')] == 'school_sport'", "images/Sprite/wgot/wgot body_wear school_sport.webp",
        "len(Char_Data['wgot']['achiev']['wear']) > 0 and Char_Data['wgot']['achiev']['wear'][get_wear_var('wgot')] == 'soap'", "images/Sprite/wgot/wgot body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "WGOT HEADFG",
    (-600,0), ConditionSwitch(
        "Char_Data['wgot']['item']['hold_left'] == 0", "images/Sprite/_General/item_l 0.webp",
        "Char_Data['wgot']['item']['hold_left'] == 1", "images/Sprite/_General/item_l 1.webp",
        "True", "images/Sprite/_General/item_l 0.webp"
    ),
    (-600,0), ConditionSwitch(
        "Char_Data['wgot']['item']['hold_right'] == 0", "images/Sprite/_General/item_r 0.webp",
        "Char_Data['wgot']['item']['hold_right'] == 1", "images/Sprite/_General/item_r 1.webp",
        "True", "images/Sprite/_General/item_r 0.webp"
    ),
    )

# WDAN

image WDAN STYLE = Composite(
    (720,1080),
    (0,0), "WDAN HEADBG",
    (0,0), ConditionSwitch(
        "isinstance(Char_Data['wdan']['wear'], str)", "images/Sprite/wdan/wdan body 1.webp",
        "True", "images/Sprite/wdan/wdan body 0.webp"
    ),
    (0,0), ConditionSwitch(
        "len(Char_Data['wdan']['achiev']['wear']) > 0 and Char_Data['wdan']['achiev']['wear'][get_wear_var('wdan')] == 'home'", "images/Sprite/wdan/wdan body_wear home.webp",
        "len(Char_Data['wdan']['achiev']['wear']) > 0 and Char_Data['wdan']['achiev']['wear'][get_wear_var('wdan')] == 'under'", "images/Sprite/wdan/wdan body_wear under.webp",
        "len(Char_Data['wdan']['achiev']['wear']) > 0 and Char_Data['wdan']['achiev']['wear'][get_wear_var('wdan')] == 'sleep'", "images/Sprite/wdan/wdan body_wear sleep.webp",
        "len(Char_Data['wdan']['achiev']['wear']) > 0 and Char_Data['wdan']['achiev']['wear'][get_wear_var('wdan')] == 'casual'", "images/Sprite/wdan/wdan body_wear casual.webp",
        "len(Char_Data['wdan']['achiev']['wear']) > 0 and Char_Data['wdan']['achiev']['wear'][get_wear_var('wdan')] == 'school'", "images/Sprite/wdan/wdan body_wear school.webp",
        "len(Char_Data['wdan']['achiev']['wear']) > 0 and Char_Data['wdan']['achiev']['wear'][get_wear_var('wdan')] == 'school_swim'", "images/Sprite/wdan/wdan body_wear school_swim.webp",
        "len(Char_Data['wdan']['achiev']['wear']) > 0 and Char_Data['wdan']['achiev']['wear'][get_wear_var('wdan')] == 'school_sport'", "images/Sprite/wdan/wdan body_wear school_sport.webp",
        "len(Char_Data['wdan']['achiev']['wear']) > 0 and Char_Data['wdan']['achiev']['wear'][get_wear_var('wdan')] == 'soap'", "images/Sprite/wdan/wdan body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "WDAN HEADFG",
    (-600,0), ConditionSwitch(
        "Char_Data['wdan']['item']['hold_left'] == 0", "images/Sprite/_General/item_l 0.webp",
        "Char_Data['wdan']['item']['hold_left'] == 1", "images/Sprite/_General/item_l 1.webp",
        "True", "images/Sprite/_General/item_l 0.webp"
    ),
    (-600,0), ConditionSwitch(
        "Char_Data['wdan']['item']['hold_right'] == 0", "images/Sprite/_General/item_r 0.webp",
        "Char_Data['wdan']['item']['hold_right'] == 1", "images/Sprite/_General/item_r 1.webp",
        "True", "images/Sprite/_General/item_r 0.webp"
    ),
    )

# WKUU

image WKUU STYLE = Composite(
    (720,1080),
    (0,0), "WKUU HEADBG",
    (0,0), ConditionSwitch(
        "isinstance(Char_Data['wkuu']['wear'], str)", "images/Sprite/wkuu/wkuu body 1.webp",
        "True", "images/Sprite/wkuu/wkuu body 0.webp"
    ),
    (0,0), ConditionSwitch(
        "len(Char_Data['wkuu']['achiev']['wear']) > 0 and Char_Data['wkuu']['achiev']['wear'][get_wear_var('wkuu')] == 'home'", "images/Sprite/wkuu/wkuu body_wear home.webp",
        "len(Char_Data['wkuu']['achiev']['wear']) > 0 and Char_Data['wkuu']['achiev']['wear'][get_wear_var('wkuu')] == 'under'", "images/Sprite/wkuu/wkuu body_wear under.webp",
        "len(Char_Data['wkuu']['achiev']['wear']) > 0 and Char_Data['wkuu']['achiev']['wear'][get_wear_var('wkuu')] == 'sleep'", "images/Sprite/wkuu/wkuu body_wear sleep.webp",
        "len(Char_Data['wkuu']['achiev']['wear']) > 0 and Char_Data['wkuu']['achiev']['wear'][get_wear_var('wkuu')] == 'casual'", "images/Sprite/wkuu/wkuu body_wear casual.webp",
        "len(Char_Data['wkuu']['achiev']['wear']) > 0 and Char_Data['wkuu']['achiev']['wear'][get_wear_var('wkuu')] == 'school'", "images/Sprite/wkuu/wkuu body_wear school.webp",
        "len(Char_Data['wkuu']['achiev']['wear']) > 0 and Char_Data['wkuu']['achiev']['wear'][get_wear_var('wkuu')] == 'school_swim'", "images/Sprite/wkuu/wkuu body_wear school_swim.webp",
        "len(Char_Data['wkuu']['achiev']['wear']) > 0 and Char_Data['wkuu']['achiev']['wear'][get_wear_var('wkuu')] == 'school_sport'", "images/Sprite/wkuu/wkuu body_wear school_sport.webp",
        "len(Char_Data['wkuu']['achiev']['wear']) > 0 and Char_Data['wkuu']['achiev']['wear'][get_wear_var('wkuu')] == 'soap'", "images/Sprite/wkuu/wkuu body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "WKUU HEADFG",
    (-600,0), ConditionSwitch(
        "Char_Data['wkuu']['item']['hold_left'] == 0", "images/Sprite/_General/item_l 0.webp",
        "Char_Data['wkuu']['item']['hold_left'] == 1", "images/Sprite/_General/item_l 1.webp",
        "True", "images/Sprite/_General/item_l 0.webp"
    ),
    (-600,0), ConditionSwitch(
        "Char_Data['wkuu']['item']['hold_right'] == 0", "images/Sprite/_General/item_r 0.webp",
        "Char_Data['wkuu']['item']['hold_right'] == 1", "images/Sprite/_General/item_r 1.webp",
        "True", "images/Sprite/_General/item_r 0.webp"
    ),
    )

# WRIN

image WRIN STYLE = Composite(
    (720,1080),
    (0,0), "WRIN HEADBG",
    (0,0), ConditionSwitch(
        "isinstance(Char_Data['wrin']['wear'], str)", "images/Sprite/wrin/wrin body 1.webp",
        "True", "images/Sprite/wrin/wrin body 0.webp"
    ),
    (0,0), ConditionSwitch(
        "len(Char_Data['wrin']['achiev']['wear']) > 0 and Char_Data['wrin']['achiev']['wear'][get_wear_var('wrin')] == 'home'", "images/Sprite/wrin/wrin body_wear home.webp",
        "len(Char_Data['wrin']['achiev']['wear']) > 0 and Char_Data['wrin']['achiev']['wear'][get_wear_var('wrin')] == 'under'", "images/Sprite/wrin/wrin body_wear under.webp",
        "len(Char_Data['wrin']['achiev']['wear']) > 0 and Char_Data['wrin']['achiev']['wear'][get_wear_var('wrin')] == 'sleep'", "images/Sprite/wrin/wrin body_wear sleep.webp",
        "len(Char_Data['wrin']['achiev']['wear']) > 0 and Char_Data['wrin']['achiev']['wear'][get_wear_var('wrin')] == 'casual'", "images/Sprite/wrin/wrin body_wear casual.webp",
        "len(Char_Data['wrin']['achiev']['wear']) > 0 and Char_Data['wrin']['achiev']['wear'][get_wear_var('wrin')] == 'school'", "images/Sprite/wrin/wrin body_wear school.webp",
        "len(Char_Data['wrin']['achiev']['wear']) > 0 and Char_Data['wrin']['achiev']['wear'][get_wear_var('wrin')] == 'school_swim'", "images/Sprite/wrin/wrin body_wear school_swim.webp",
        "len(Char_Data['wrin']['achiev']['wear']) > 0 and Char_Data['wrin']['achiev']['wear'][get_wear_var('wrin')] == 'school_sport'", "images/Sprite/wrin/wrin body_wear school_sport.webp",
        "len(Char_Data['wrin']['achiev']['wear']) > 0 and Char_Data['wrin']['achiev']['wear'][get_wear_var('wrin')] == 'soap'", "images/Sprite/wrin/wrin body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "WRIN HEADFG",
    (-600,0), ConditionSwitch(
        "Char_Data['wrin']['item']['hold_left'] == 0", "images/Sprite/_General/item_l 0.webp",
        "Char_Data['wrin']['item']['hold_left'] == 1", "images/Sprite/_General/item_l 1.webp",
        "True", "images/Sprite/_General/item_l 0.webp"
    ),
    (-600,0), ConditionSwitch(
        "Char_Data['wrin']['item']['hold_right'] == 0", "images/Sprite/_General/item_r 0.webp",
        "Char_Data['wrin']['item']['hold_right'] == 1", "images/Sprite/_General/item_r 1.webp",
        "True", "images/Sprite/_General/item_r 0.webp"
    ),
    )

# WSUK

image WSUK STYLE = Composite(
    (720,1080),
    (0,0), "WSUK HEADBG",
    (0,0), ConditionSwitch(
        "isinstance(Char_Data['wsuk']['wear'], str)", "images/Sprite/wsuk/wsuk body 1.webp",
        "True", "images/Sprite/wsuk/wsuk body 0.webp"
    ),
    (0,0), ConditionSwitch(
        "len(Char_Data['wsuk']['achiev']['wear']) > 0 and Char_Data['wsuk']['achiev']['wear'][get_wear_var('wsuk')] == 'home'", "images/Sprite/wsuk/wsuk body_wear home.webp",
        "len(Char_Data['wsuk']['achiev']['wear']) > 0 and Char_Data['wsuk']['achiev']['wear'][get_wear_var('wsuk')] == 'under'", "images/Sprite/wsuk/wsuk body_wear under.webp",
        "len(Char_Data['wsuk']['achiev']['wear']) > 0 and Char_Data['wsuk']['achiev']['wear'][get_wear_var('wsuk')] == 'sleep'", "images/Sprite/wsuk/wsuk body_wear sleep.webp",
        "len(Char_Data['wsuk']['achiev']['wear']) > 0 and Char_Data['wsuk']['achiev']['wear'][get_wear_var('wsuk')] == 'casual'", "images/Sprite/wsuk/wsuk body_wear casual.webp",
        "len(Char_Data['wsuk']['achiev']['wear']) > 0 and Char_Data['wsuk']['achiev']['wear'][get_wear_var('wsuk')] == 'school'", "images/Sprite/wsuk/wsuk body_wear school.webp",
        "len(Char_Data['wsuk']['achiev']['wear']) > 0 and Char_Data['wsuk']['achiev']['wear'][get_wear_var('wsuk')] == 'school_swim'", "images/Sprite/wsuk/wsuk body_wear school_swim.webp",
        "len(Char_Data['wsuk']['achiev']['wear']) > 0 and Char_Data['wsuk']['achiev']['wear'][get_wear_var('wsuk')] == 'school_sport'", "images/Sprite/wsuk/wsuk body_wear school_sport.webp",
        "len(Char_Data['wsuk']['achiev']['wear']) > 0 and Char_Data['wsuk']['achiev']['wear'][get_wear_var('wsuk')] == 'soap'", "images/Sprite/wsuk/wsuk body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "WSUK HEADFG",
    (-600,0), ConditionSwitch(
        "Char_Data['wsuk']['item']['hold_left'] == 0", "images/Sprite/_General/item_l 0.webp",
        "Char_Data['wsuk']['item']['hold_left'] == 1", "images/Sprite/_General/item_l 1.webp",
        "True", "images/Sprite/_General/item_l 0.webp"
    ),
    (-600,0), ConditionSwitch(
        "Char_Data['wsuk']['item']['hold_right'] == 0", "images/Sprite/_General/item_r 0.webp",
        "Char_Data['wsuk']['item']['hold_right'] == 1", "images/Sprite/_General/item_r 1.webp",
        "True", "images/Sprite/_General/item_r 0.webp"
    ),
    )