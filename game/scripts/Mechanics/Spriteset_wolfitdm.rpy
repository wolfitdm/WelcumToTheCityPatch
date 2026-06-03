# ----------------------------------------------------------------------------------------------------
# KAWAII
# ----------------------------------------------------------------------------------------------------

default kawaii_path = "kawaiis/kawaii"

init python:
     import os

     def wolfitdm_add_modloader_path():
         mod_loader_path = os.path.join(config.basedir, "game", "wolfitdm")

         os.makedirs(mod_loader_path, exist_ok=True)

         if not mod_loader_path in config.searchpath:
            config.searchpath.append(mod_loader_path)

     def init_kawaii_path():
         wolfitdm_add_modloader_path()
         kawaii_dir = os.path.join(config.basedir, "game", "wolfitdm", "kawaiis", "kawaii")
         os.makedirs(kawaii_dir, exist_ok=True)
         setattr(store, "kawaii_path", "kawaiis/kawaii")

     init_kawaii_path()

     def get_kawaii_path():
         if hasattr(store, "my_kawaii_path"):
            return getattr(store, "my_kawaii_path")

         if hasattr(store, "kawaii_path"):
            return getattr(store, "kawaii_path")

         return ""

     def get_current_kawaii_folders():
         root_path =  os.path.join(config.basedir, "game", "wolfitdm", "kawaiis")

         os.makedirs(root_path, exist_ok=True)

         if not isinstance(root_path, str):
            return

         if not os.path.exists(root_path):
            return

         if not os.path.isdir(root_path):
            return

         kawaii_dirs = []

         for current_path, dirs, files in os.walk(root_path):
             for d in dirs:
                 kawaii_dirs.append(d)
             break

         if not "kawaii" in kawaii_dirs:
            kawaii_dirs.append("kawaii")

         return kawaii_dirs

     def switch_kawaii_folder(folder):
         kawaii_folders = get_current_kawaii_folders()

         if folder in kawaii_folders:
            if folder == "kawaii":
               if hasattr(store, "my_kawaii_path"):
                  delattr(store, "my_kawaii_path")

               return folder
            else:
               setattr(store, "my_kawaii_path", "kawaiis/" + folder)
               return folder
        
         return None


image KAWAII EYES:
    "%s/eyes/kawaii_eyes0.png" % get_kawaii_path(),
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
    "%s/eyes/kawaii_eyes2.png" % get_kawaii_path(),
    0.15
    "%s/eyes/kawaii_eyes1.png" % get_kawaii_path(),
    0.1
    repeat

image KAWAII MOUTH:
    ConditionSwitch(
        "WChar.gvar('hero', 'mood') == 'A1'", "%s/mouth/general_mouth_2_A1.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'mood') == 'A2'", "%s/mouth/general_mouth_2_A2.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'mood') == 'A3'", "%s/mouth/general_mouth_2_A3.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'mood') == 'A4'", "%s/mouth/general_mouth_2_A4.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'mood') == 'O1'", "%s/mouth/general_mouth_2_O1.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'mood') == 'O2'", "%s/mouth/general_mouth_2_O2.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'mood') == 'O3'", "%s/mouth/general_mouth_2_O3.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'mood') == 'O4'", "%s/mouth/general_mouth_2_O4.png" % get_kawaii_path(),
        "True", "%s/mouth/general_mouth_2_A1.png" % get_kawaii_path()
    ),
    .15
    ConditionSwitch(
        "WChar.gvar('hero', 'mood') == 'A1'", "%s/mouth/kawaii_mouth_1_A1.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'mood') == 'A2'", "%s/mouth/kawaii_mouth_1_A2.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'mood') == 'A3'", "%s/mouth/kawaii_mouth_1_A3.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'mood') == 'A4'", "%s/mouth/kawaii_mouth_1_A4.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'mood') == 'O1'", "%s/mouth/kawaii_mouth_1_O1.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'mood') == 'O2'", "%s/mouth/kawaii_mouth_1_O2.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'mood') == 'O3'", "%s/mouth/kawaii_mouth_1_O3.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'mood') == 'O4'", "%s/mouth/kawaii_mouth_1_O4.png" % get_kawaii_path(),
        "True", "%s/mouth/kawaii_mouth_1_A1.png" % get_kawaii_path()
    )
    .15
    repeat

image KAWAII WEAR:
    ConditionSwitch(
        "WChar.gvar('hero', 'wear') == 'kawaii_home'", "%s/body_wear_phone/kawaii_body_wear_home.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'wear') == 'kawaii_under'", "%s/body_wear_phone/kawaii_body_wear_under.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'wear') == 'kawaii_sleep'", "%s/body_wear_phone/kawaii_body_wear_sleep.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'wear') == 'kawaii_casual'", "%s/body_wear_phone/kawaii_body_wear_casual.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'wear') == 'kawaii_dressy'", "%s/body_wear_phone/kawaii_body_wear_dressy.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'wear') == 'kawaii_formal'", "%s/body_wear_phone/kawaii_body_wear_formal.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'wear') == 'kawaii_sport'", "%s/body_wear_phone/kawaii_body_wear_sport.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'wear') == 'kawaii_swim'", "%s/body_wear_phone/kawaii_body_wear_swim.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'wear') == 'kawaii_school'", "%s/body_wear_phone/kawaii_body_wear_school.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'wear') == 'kawaii_school_swim'", "%s/body_wear_phone/kawaii_body_wear_school_swim.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'wear') == 'kawaii_school_sport'", "%s/body_wear_phone/kawaii_body_wear_school_sport.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'wear') == 'kawaii_work'", "%s/body_wear_phone/kawaii_body_wear_work.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'wear') == 'kawaii_soap'", "%s/body_wear_phone/kawaii_body_wear_soap.png" % get_kawaii_path(),
        "True", Null()
    ),

image KAWAII HEADFG PARTS = Composite(
    (720,1080),
    (0,0), "%s/eyes/kawaii_eyes3.png" % get_kawaii_path(),
    (0,0), ConditionSwitch(
         "WChar.gvar('hero', 'wear') == 'kawaii_school_swim'", "%s/head/school_swim/kawaii_head_mg_school_swim.png" % get_kawaii_path(),
         "WChar.gvar('hero', 'wear') == 'kawaii_school_sport'", "%s/head/school_sport/kawaii_head_mg_school_sport.png" % get_kawaii_path(),
         "WChar.gvar('hero', 'wear') == 'kawaii_casual'", "%s/head/casual/kawaii_head_mg_casual.png" % get_kawaii_path(),
         "WChar.gvar('hero', 'wear') == 'kawaii_dressy'", "%s/head/dressy/kawaii_head_mg_dressy.png" % get_kawaii_path(),
         "WChar.gvar('hero', 'wear') == 'kawaii_formal'", "%s/head/formal/kawaii_head_mg_formal.png" % get_kawaii_path(),
         "WChar.gvar('hero', 'wear') == 'kawaii_home'", "%s/head/home/kawaii_head_mg_home.png" % get_kawaii_path(),
         "WChar.gvar('hero', 'wear') == 'kawaii_school'", "%s/head/school/kawaii_head_mg_school.png" % get_kawaii_path(),
         "WChar.gvar('hero', 'wear') == 'kawaii_sleep'", "%s/head/sleep/kawaii_head_mg_sleep.png" % get_kawaii_path(),
         "WChar.gvar('hero', 'wear') == 'kawaii_soap'", "%s/head/soap/kawaii_head_mg_soap.png" % get_kawaii_path(),
         "WChar.gvar('hero', 'wear') == 'kawaii_under'", "%s/head/under/kawaii_head_mg_under.png" % get_kawaii_path(),
         "WChar.gvar('hero', 'wear') == 'kawaii_work'", "%s/head/work/kawaii_head_mg_work.png" % get_kawaii_path(),
         "True", "%s/head/kawaii_head_mg.png" % get_kawaii_path()
    ),
    (0,0), ConditionSwitch(
        "WChar.gvar('hero', 'fx') == 0", "%s/fx/kawaii_fx_0.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'fx') == 1", "%s/fx/kawaii_fx_1.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'fx') == 2", "%s/fx/kawaii_fx_2.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'fx') == 3", "%s/fx/kawaii_fx_3.png" % get_kawaii_path(),
        "True", "%s/fx/kawaii_fx_0.png" % get_kawaii_path()
    ),
    (0,0), WhileSpeaking("hero", "KAWAII MOUTH", ConditionSwitch(
        "WChar.gvar('hero', 'mood') == 'A1'", "%s/mouth/general_mouth_2_A1.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'mood') == 'A2'", "%s/mouth/general_mouth_2_A2.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'mood') == 'A3'", "%s/mouth/general_mouth_2_A3.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'mood') == 'A4'", "%s/mouth/general_mouth_2_A4.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'mood') == 'O1'", "%s/mouth/general_mouth_2_O1.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'mood') == 'O2'", "%s/mouth/general_mouth_2_O2.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'mood') == 'O3'", "%s/mouth/general_mouth_2_O3.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'mood') == 'O4'", "%s/mouth/general_mouth_2_O4.png" % get_kawaii_path(),
        "True", "%s/mouth/general_mouth_2_A1.png" % get_kawaii_path()
    )),
    (0,0), ConditionSwitch(
         "WChar.gvar('hero', 'wear') == 'kawaii_school_swim'", "%s/head/school_swim/kawaii_head_wear_school_swim.png" % get_kawaii_path(),
         "WChar.gvar('hero', 'wear') == 'kawaii_school_sport'", "%s/head/school_sport/kawaii_head_wear_school_sport.png" % get_kawaii_path(),
         "WChar.gvar('hero', 'wear') == 'kawaii_casual'", "%s/head/casual/kawaii_head_wear_casual.png" % get_kawaii_path(),
         "WChar.gvar('hero', 'wear') == 'kawaii_dressy'", "%s/head/dressy/kawaii_head_wear_dressy.png" % get_kawaii_path(),
         "WChar.gvar('hero', 'wear') == 'kawaii_formal'", "%s/head/formal/kawaii_head_wear_formal.png" % get_kawaii_path(),
         "WChar.gvar('hero', 'wear') == 'kawaii_home'", "%s/head/home/kawaii_head_wear_home.png" % get_kawaii_path(),
         "WChar.gvar('hero', 'wear') == 'kawaii_school'", "%s/head/school/kawaii_head_wear_school.png" % get_kawaii_path(),
         "WChar.gvar('hero', 'wear') == 'kawaii_sleep'", "%s/head/sleep/kawaii_head_wear_sleep.png" % get_kawaii_path(),
         "WChar.gvar('hero', 'wear') == 'kawaii_soap'", "%s/head/soap/kawaii_head_wear_soap.png" % get_kawaii_path(),
         "WChar.gvar('hero', 'wear') == 'kawaii_under'", "%s/head/under/kawaii_head_wear_under.png" % get_kawaii_path(),
         "WChar.gvar('hero', 'wear') == 'kawaii_work'", "%s/head/work/kawaii_head_wear_work.png" % get_kawaii_path(),
         "True", "%s/head/kawaii_head_wear.png" % get_kawaii_path()
    ),
    (0,0), "KAWAII EYES",
    (0,0), ConditionSwitch(
         "WChar.gvar('hero', 'wear') == 'kawaii_school_swim'", "%s/head/school_swim/kawaii_head_fg1_school_swim.png" % get_kawaii_path(),
         "WChar.gvar('hero', 'wear') == 'kawaii_school_sport'", "%s/head/school_sport/kawaii_head_fg1_school_sport.png" % get_kawaii_path(),
         "WChar.gvar('hero', 'wear') == 'kawaii_casual'", "%s/head/casual/kawaii_head_fg1_casual.png" % get_kawaii_path(),
         "WChar.gvar('hero', 'wear') == 'kawaii_dressy'", "%s/head/dressy/kawaii_head_fg1_dressy.png" % get_kawaii_path(),
         "WChar.gvar('hero', 'wear') == 'kawaii_formal'", "%s/head/formal/kawaii_head_fg1_formal.png" % get_kawaii_path(),
         "WChar.gvar('hero', 'wear') == 'kawaii_home'", "%s/head/home/kawaii_head_fg1_home.png" % get_kawaii_path(),
         "WChar.gvar('hero', 'wear') == 'kawaii_school'", "%s/head/school/kawaii_head_fg1_school.png" % get_kawaii_path(),
         "WChar.gvar('hero', 'wear') == 'kawaii_sleep'", "%s/head/sleep/kawaii_head_fg1_sleep.png" % get_kawaii_path(),
         "WChar.gvar('hero', 'wear') == 'kawaii_soap'", "%s/head/soap/kawaii_head_fg1_soap.png" % get_kawaii_path(),
         "WChar.gvar('hero', 'wear') == 'kawaii_under'", "%s/head/under/kawaii_head_fg1_under.png" % get_kawaii_path(),
         "WChar.gvar('hero', 'wear') == 'kawaii_work'", "%s/head/work/kawaii_head_fg1_work.png" % get_kawaii_path(),
         "True", "%s/head/kawaii_head_fg1.png" % get_kawaii_path()
    ),
    (0,0), ConditionSwitch(
         "WChar.gvar('hero', 'wear') == 'kawaii_school_swim'", "%s/head/school_swim/kawaii_head_fg2_school_swim.png" % get_kawaii_path(),
         "WChar.gvar('hero', 'wear') == 'kawaii_school_sport'", "%s/head/school_sport/kawaii_head_fg2_school_sport.png" % get_kawaii_path(),
         "WChar.gvar('hero', 'wear') == 'kawaii_casual'", "%s/head/casual/kawaii_head_fg2_casual.png" % get_kawaii_path(),
         "WChar.gvar('hero', 'wear') == 'kawaii_dressy'", "%s/head/dressy/kawaii_head_fg2_dressy.png" % get_kawaii_path(),
         "WChar.gvar('hero', 'wear') == 'kawaii_formal'", "%s/head/formal/kawaii_head_fg2_formal.png" % get_kawaii_path(),
         "WChar.gvar('hero', 'wear') == 'kawaii_home'", "%s/head/home/kawaii_head_fg2_home.png" % get_kawaii_path(),
         "WChar.gvar('hero', 'wear') == 'kawaii_school'", "%s/head/school/kawaii_head_fg2_school.png" % get_kawaii_path(),
         "WChar.gvar('hero', 'wear') == 'kawaii_sleep'", "%s/head/sleep/kawaii_head_fg2_sleep.png" % get_kawaii_path(),
         "WChar.gvar('hero', 'wear') == 'kawaii_soap'", "%s/head/soap/kawaii_head_fg2_soap.png" % get_kawaii_path(),
         "WChar.gvar('hero', 'wear') == 'kawaii_under'", "%s/head/under/kawaii_head_fg2_under.png" % get_kawaii_path(),
         "WChar.gvar('hero', 'wear') == 'kawaii_work'", "%s/head/work/kawaii_head_fg2_work.png" % get_kawaii_path(),
         "True", "%s/head/kawaii_head_fg2.png" % get_kawaii_path()
    ),
    (0,0), ConditionSwitch(
        "WChar.gvar('hero', 'mood') == 'A1'", "%s/eyes/kawaii_eyebrow_A1.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'mood') == 'A2'", "%s/eyes/kawaii_eyebrow A2.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'mood') == 'A3'", "%s/eyes/kawaii_eyebrow_A3.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'mood') == 'A4'", "%s/eyes/kawaii_eyebrow_A4.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'mood') == 'O1'", "%s/eyes/kawaii_eyebrow_O1.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'mood') == 'O2'", "%s/eyes/kawaii_eyebrow_O2.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'mood') == 'O3'", "%s/eyes/kawaii_eyebrow_O3.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'mood') == 'O4'", "%s/eyes/kawaii_eyebrow_O4.png" % get_kawaii_path(),
        "True", "%s/eyes/kawaii_eyebrow_A1.png" % get_kawaii_path()
    ),
    )

image KAWAII HEADBG:
    ConditionSwitch(
        "WChar.gvar('hero', 'wear') == 'kawaii_school_swim'", "%s/head/school_swim/kawaii_head_bg_school_swim.png" % get_kawaii_path(), 
        "WChar.gvar('hero', 'wear') == 'kawaii_school_sport'", "%s/head/school_sport/kawaii_head_bg_school_sport.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'wear') == 'kawaii_casual'", "%s/head/casual/kawaii_head_bg_casual.png" % get_kawaii_path(), 
        "WChar.gvar('hero', 'wear') == 'kawaii_dressy'", "%s/head/dressy/kawaii_head_bg_dressy.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'wear') == 'kawaii_formal'", "%s/head/formal/kawaii_head_bg_formal.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'wear') == 'kawaii_home'", "%s/head/home/kawaii_head_bg_home.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'wear') == 'kawaii_school'", "%s/head/school/kawaii_head_bg_school.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'wear') == 'kawaii_sleep'", "%s/head/sleep/kawaii_head_bg_sleep.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'wear') == 'kawaii_soap'", "%s/head/soap/kawaii_head_bg_soap.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'wear') == 'kawaii_under'", "%s/head/under/kawaii_head_bg_under.png" % get_kawaii_path(),
        "WChar.gvar('hero', 'wear') == 'kawaii_work'", "%s/head/work/kawaii_head_bg_work.png" % get_kawaii_path(),
        "True", "%s/head/kawaii_head_bg_common.png" % get_kawaii_path()
    )
    zoom 1.5/WChar.gvar('hero', 'size')
    xoffset int((WChar.gvar('hero', 'size') - 1.50) * 206)
    yoffset int((WChar.gvar('hero', 'size') - 1.50) * 275)

image KAWAII HEADFG:
    "KAWAII HEADFG PARTS"
    zoom 1.5/WChar.gvar('hero', 'size')
    xoffset int((WChar.gvar('hero', 'size') - 1.50) * 206)
    yoffset int((WChar.gvar('hero', 'size') - 1.50) * 275)

image KAWAII PARTS = Composite(
    (720,1080),
    (0,0), "KAWAII HEADBG",
    (0,0), ConditionSwitch(
        "len(WChar.gvar('hero', 'achiev_wear')) > 0 and isinstance(WChar.avar('hero', 'achiev_wear', get_wear_var('hero')), str) and WChar.avar('hero', 'achiev_wear', get_wear_var('hero')).startswith('kawaii')", "%s/body_wear_phone/kawaii_body_1.png" % get_kawaii_path(),
        "True", "%s/body_wear_phone/kawaii_body_0.png" % get_kawaii_path()
    ),
    (0,0), "KAWAII WEAR",
    (0,0), "KAWAII HEADFG",
    )

image KAWAII STYLE = Composite(
    (720,1080),
    (0,0), "KAWAII HEADBG",
    (0,0), ConditionSwitch(
        "len(WChar.gvar('hero', 'achiev_wear')) > 0 and isinstance(WChar.avar('hero', 'achiev_wear', get_wear_var('hero')), str) and WChar.avar('hero', 'achiev_wear', get_wear_var('hero')).startswith('kawaii')", "%s/body_wear_phone/kawaii_body_1.png" % get_kawaii_path(),
        "True", "%s/body_wear_phone/kawaii_body_0.png" % get_kawaii_path()
    ),
    (0,0), ConditionSwitch(
        "len(WChar.gvar('hero', 'achiev_wear')) > 0 and WChar.avar('hero', 'achiev_wear', get_wear_var('hero')) == 'kawaii_home'", "%s/body_wear_phone/kawaii_body_wear_home.png" % get_kawaii_path(),
        "len(WChar.gvar('hero', 'achiev_wear')) > 0 and WChar.avar('hero', 'achiev_wear', get_wear_var('hero')) == 'kawaii_under'", "%s/body_wear_phone/kawaii_body_wear_under.png" % get_kawaii_path(),
        "len(WChar.gvar('hero', 'achiev_wear')) > 0 and WChar.avar('hero', 'achiev_wear', get_wear_var('hero')) == 'kawaii_sleep'", "%s/body_wear_phone/kawaii_body_wear_sleep.png" % get_kawaii_path(),
        "len(WChar.gvar('hero', 'achiev_wear')) > 0 and WChar.avar('hero', 'achiev_wear', get_wear_var('hero')) == 'kawaii_casual'", "%s/body_wear_phone/kawaii_body_wear_casual.png" % get_kawaii_path(),
        "len(WChar.gvar('hero', 'achiev_wear')) > 0 and WChar.avar('hero', 'achiev_wear', get_wear_var('hero')) == 'kawaii_school'", "%s/body_wear_phone/kawaii_body_wear_school.png" % get_kawaii_path(),
        "len(WChar.gvar('hero', 'achiev_wear')) > 0 and WChar.avar('hero', 'achiev_wear', get_wear_var('hero')) == 'kawaii_school_swim'", "%s/body_wear_phone/kawaii_body_wear_school_swim.png" % get_kawaii_path(),
        "len(WChar.gvar('hero', 'achiev_wear')) > 0 and WChar.avar('hero', 'achiev_wear', get_wear_var('hero')) == 'kawaii_school_sport'", "%s/body_wear_phone/kawaii_body_wear_school_sport.png" % get_kawaii_path(),
        "len(WChar.gvar('hero', 'achiev_wear')) > 0 and WChar.avar('hero', 'achiev_wear', get_wear_var('hero')) == 'kawaii_soap'", "%s/body_wear_phone/kawaii_body_wear_soap.png" % get_kawaii_path(),
        "len(WChar.gvar('hero', 'achiev_wear')) > 0 and WChar.avar('hero', 'achiev_wear', get_wear_var('hero')) == 'kawaii_work'", "%s/body_wear_phone/kawaii_body_wear_work.png" % get_kawaii_path(),
        "len(WChar.gvar('hero', 'achiev_wear')) > 0 and WChar.avar('hero', 'achiev_wear', get_wear_var('hero')) == 'kawaii_dressy'", "%s/body_wear_phone/kawaii_body_wear_dressy.png" % get_kawaii_path(),
        "len(WChar.gvar('hero', 'achiev_wear')) > 0 and WChar.avar('hero', 'achiev_wear', get_wear_var('hero')) == 'kawaii_formal'", "%s/body_wear_phone/kawaii_body_wear_formal.png" % get_kawaii_path(),
        "True", Null()
    ),
    (0,0), "KAWAII HEADFG",
    )

image HERO STYLE DEFAULT = Composite(
    (720,1080),
    (0,0), ConditionSwitch(
        "WChar.gvar('hero', 'body') == 0", "images/Sprite/hero/hero body 0.webp",
        "WChar.gvar('hero', 'body') == 1", "images/Sprite/hero/hero body 1.webp",
        "True", "images/Sprite/hero/hero body 0.webp"
    ),
    (0,0), ConditionSwitch(
        "len(WChar.gvar('hero', 'achiev_wear')) > 0 and WChar.avar('hero', 'achiev_wear', get_wear_var('hero')) == 'home'", "images/Sprite/hero/hero body_wear home.webp",
        "len(WChar.gvar('hero', 'achiev_wear')) > 0 and WChar.avar('hero', 'achiev_wear', get_wear_var('hero')) == 'under'", "images/Sprite/hero/hero body_wear under.webp",
        "len(WChar.gvar('hero', 'achiev_wear')) > 0 and WChar.avar('hero', 'achiev_wear', get_wear_var('hero')) == 'sleep'", "images/Sprite/hero/hero body_wear sleep.webp",
        "len(WChar.gvar('hero', 'achiev_wear')) > 0 and WChar.avar('hero', 'achiev_wear', get_wear_var('hero')) == 'casual'", "images/Sprite/hero/hero body_wear casual.webp",
        "len(WChar.gvar('hero', 'achiev_wear')) > 0 and WChar.avar('hero', 'achiev_wear', get_wear_var('hero')) == 'school'", "images/Sprite/hero/hero body_wear school.webp",
        "len(WChar.gvar('hero', 'achiev_wear')) > 0 and WChar.avar('hero', 'achiev_wear', get_wear_var('hero')) == 'school_swim'", "images/Sprite/hero/hero body_wear school_swim.webp",
        "len(WChar.gvar('hero', 'achiev_wear')) > 0 and WChar.avar('hero', 'achiev_wear', get_wear_var('hero')) == 'school_sport'", "images/Sprite/hero/hero body_wear school_sport.webp",
        "len(WChar.gvar('hero', 'achiev_wear')) > 0 and WChar.avar('hero', 'achiev_wear', get_wear_var('hero')) == 'soap'", "images/Sprite/hero/hero body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "HERO HEADFG",
    (25,64), ConditionSwitch(
        "WChar.gvar('hero', 'itemL') == 0", "images/Sprite/_General/item_l 0.webp",
        "WChar.gvar('hero', 'itemL') == 1", "images/Sprite/_General/item_l 1.webp",
        "True", "images/Sprite/_General/item_l 0.webp"
    ),
    (-35,65), ConditionSwitch(
        "WChar.gvar('hero', 'itemR') == 0", "images/Sprite/_General/item_r 0.webp",
        "WChar.gvar('hero', 'itemR') == 1", "images/Sprite/_General/item_r 1.webp",
        "True", "images/Sprite/_General/item_r 0.webp"
    ),
    )

default wolfitdm_image_style = "HERO STYLE DEFAULT"

image HERO STYLE:
    ConditionSwitch(
       "len(WChar.gvar('hero', 'achiev_wear')) > 0 and isinstance(WChar.avar('hero', 'achiev_wear', get_wear_var('hero')), str) and WChar.avar('hero', 'achiev_wear', get_wear_var('hero')).startswith('kawaii')", "KAWAII STYLE",
       "(len(WChar.gvar('hero', 'achiev_wear')) > 0 and isinstance(WChar.avar('hero', 'achiev_wear', get_wear_var('hero')), str) and WChar.avar('hero', 'achiev_wear', get_wear_var('hero')).startswith('kawaii')) == False", "[wolfitdm_image_style]"
    )

image HERO DEFAULT:
    "HERO PARTS"
    yalign 1.0
    ypos 1400
    zoom 0+(0.25+(1*WChar.gvar('hero', 'size')))*(0.25+(1*WChar.gvar('hero', 'size')))/2.5

image HERO KAWAII:    
    "KAWAII PARTS"
    yalign 1.0
    ypos 1400
    zoom 0+(0.25+(1*WChar.gvar('hero', 'size')))*(0.25+(1*WChar.gvar('hero', 'size')))/2.5

default wolfitdm_image = "HERO DEFAULT"

image HERO:
    ConditionSwitch(
       "len(WChar.gvar('hero', 'achiev_wear')) > 0 and isinstance(WChar.avar('hero', 'achiev_wear', get_wear_var('hero')), str) and WChar.avar('hero', 'achiev_wear', get_wear_var('hero')).startswith('kawaii')", "HERO KAWAII",
       "(len(WChar.gvar('hero', 'achiev_wear')) > 0 and isinstance(WChar.avar('hero', 'achiev_wear', get_wear_var('hero')), str) and WChar.avar('hero', 'achiev_wear', get_wear_var('hero')).startswith('kawaii')) == False", "[wolfitdm_image]"
    )

# HRIV

image HRIV STYLE = Composite(
    (720,1080),
    (0,0), "HRIV HEADBG",
    (0,0), ConditionSwitch(
        "WChar.gvar('hriv', 'body') == 0", "images/Sprite/hriv/hriv body 0.webp",
        "WChar.gvar('hriv', 'body') == 1", "images/Sprite/hriv/hriv body 1.webp",
        "True", "images/Sprite/hriv/hriv body 0.webp"
    ),
    (0,0), ConditionSwitch(
        "len(WChar.gvar('hriv', 'achiev_wear')) > 0 and WChar.avar('hriv', 'achiev_wear', get_wear_var('hriv')) == 'home'", "images/Sprite/hriv/hriv body_wear home.webp",
        "len(WChar.gvar('hriv', 'achiev_wear')) > 0 and WChar.avar('hriv', 'achiev_wear', get_wear_var('hriv')) == 'under'", "images/Sprite/hriv/hriv body_wear under.webp",
        "len(WChar.gvar('hriv', 'achiev_wear')) > 0 and WChar.avar('hriv', 'achiev_wear', get_wear_var('hriv')) == 'sleep'", "images/Sprite/hriv/hriv body_wear sleep.webp",
        "len(WChar.gvar('hriv', 'achiev_wear')) > 0 and WChar.avar('hriv', 'achiev_wear', get_wear_var('hriv')) == 'casual'", "images/Sprite/hriv/hriv body_wear casual.webp",
        "len(WChar.gvar('hriv', 'achiev_wear')) > 0 and WChar.avar('hriv', 'achiev_wear', get_wear_var('hriv')) == 'school'", "images/Sprite/hriv/hriv body_wear school.webp",
        "len(WChar.gvar('hriv', 'achiev_wear')) > 0 and WChar.avar('hriv', 'achiev_wear', get_wear_var('hriv')) == 'school_swim'", "images/Sprite/hriv/hriv body_wear school_swim.webp",
        "len(WChar.gvar('hriv', 'achiev_wear')) > 0 and WChar.avar('hriv', 'achiev_wear', get_wear_var('hriv')) == 'school_sport'", "images/Sprite/hriv/hriv body_wear school_sport.webp",
        "len(WChar.gvar('hriv', 'achiev_wear')) > 0 and WChar.avar('hriv', 'achiev_wear', get_wear_var('hriv')) == 'soap'", "images/Sprite/hriv/hriv body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "HRIV HEADFG",
    (25,64), ConditionSwitch(
        "WChar.gvar('hriv', 'itemL') == 0", "images/Sprite/_General/item_l 0.webp",
        "WChar.gvar('hriv', 'itemL') == 1", "images/Sprite/_General/item_l 1.webp",
        "True", "images/Sprite/_General/item_l 0.webp"
    ),
    (-35,65), ConditionSwitch(
        "WChar.gvar('hriv', 'itemR') == 0", "images/Sprite/_General/item_r 0.webp",
        "WChar.gvar('hriv', 'itemR') == 1", "images/Sprite/_General/item_r 1.webp",
        "True", "images/Sprite/_General/item_r 0.webp"
    ),
    )

# HPRV

image HPRV STYLE = Composite(
    (720,1080),
    (0,0), "HPRV HEADBG",
    (0,0), "images/Sprite/hprv/hprv body 1.webp",
    (0,0), ConditionSwitch(
        "len(WChar.gvar('hprv', 'achiev_wear')) > 0 and WChar.avar('hprv', 'achiev_wear', get_wear_var('hprv')) == 'home'", "images/Sprite/hprv/hprv body_wear home.webp",
        "len(WChar.gvar('hprv', 'achiev_wear')) > 0 and WChar.avar('hprv', 'achiev_wear', get_wear_var('hprv')) == 'under'", "images/Sprite/hprv/hprv body_wear under.webp",
        "len(WChar.gvar('hprv', 'achiev_wear')) > 0 and WChar.avar('hprv', 'achiev_wear', get_wear_var('hprv')) == 'sleep'", "images/Sprite/hprv/hprv body_wear sleep.webp",
        "len(WChar.gvar('hprv', 'achiev_wear')) > 0 and WChar.avar('hprv', 'achiev_wear', get_wear_var('hprv')) == 'casual'", "images/Sprite/hprv/hprv body_wear casual.webp",
        "len(WChar.gvar('hprv', 'achiev_wear')) > 0 and WChar.avar('hprv', 'achiev_wear', get_wear_var('hprv')) == 'school'", "images/Sprite/hprv/hprv body_wear school.webp",
        "len(WChar.gvar('hprv', 'achiev_wear')) > 0 and WChar.avar('hprv', 'achiev_wear', get_wear_var('hprv')) == 'school_swim'", "images/Sprite/hprv/hprv body_wear school_swim.webp",
        "len(WChar.gvar('hprv', 'achiev_wear')) > 0 and WChar.avar('hprv', 'achiev_wear', get_wear_var('hprv')) == 'school_sport'", "images/Sprite/hprv/hprv body_wear school_sport.webp",
        "len(WChar.gvar('hprv', 'achiev_wear')) > 0 and WChar.avar('hprv', 'achiev_wear', get_wear_var('hprv')) == 'soap'", "images/Sprite/hprv/hprv body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "HPRV HEADFG",
    (-600,0), ConditionSwitch(
        "WChar.gvar('hprv', 'itemL') == 0", "images/Sprite/_General/item_l 0.webp",
        "WChar.gvar('hprv', 'itemL') == 1", "images/Sprite/_General/item_l 1.webp",
        "True", "images/Sprite/_General/item_l 0.webp"
    ),
    (-600,0), ConditionSwitch(
        "WChar.gvar('hprv', 'itemR') == 0", "images/Sprite/_General/item_r 0.webp",
        "WChar.gvar('hprv', 'itemR') == 1", "images/Sprite/_General/item_r 1.webp",
        "True", "images/Sprite/_General/item_r 0.webp"
    ),
    )

# HINE

image HINE STYLE = Composite(
    (720,1080),
    (0,0), "HINE HEADBG",
    (0,0), "images/Sprite/hine/hine body 0.webp",
    (0,0), ConditionSwitch(
        "len(WChar.gvar('hine', 'achiev_wear')) > 0 and WChar.avar('hine', 'achiev_wear', get_wear_var('hine')) == 'home'", "images/Sprite/hine/hine body_wear home.webp",
        "len(WChar.gvar('hine', 'achiev_wear')) > 0 and WChar.avar('hine', 'achiev_wear', get_wear_var('hine')) == 'under'", "images/Sprite/hine/hine body_wear under.webp",
        "len(WChar.gvar('hine', 'achiev_wear')) > 0 and WChar.avar('hine', 'achiev_wear', get_wear_var('hine')) == 'sleep'", "images/Sprite/hine/hine body_wear sleep.webp",
        "len(WChar.gvar('hine', 'achiev_wear')) > 0 and WChar.avar('hine', 'achiev_wear', get_wear_var('hine')) == 'casual'", "images/Sprite/hine/hine body_wear casual.webp",
        "len(WChar.gvar('hine', 'achiev_wear')) > 0 and WChar.avar('hine', 'achiev_wear', get_wear_var('hine')) == 'school'", "images/Sprite/hine/hine body_wear school.webp",
        "len(WChar.gvar('hine', 'achiev_wear')) > 0 and WChar.avar('hine', 'achiev_wear', get_wear_var('hine')) == 'school_swim'", "images/Sprite/hine/hine body_wear school_swim.webp",
        "len(WChar.gvar('hine', 'achiev_wear')) > 0 and WChar.avar('hine', 'achiev_wear', get_wear_var('hine')) == 'school_sport'", "images/Sprite/hine/hine body_wear school_sport.webp",
        "len(WChar.gvar('hine', 'achiev_wear')) > 0 and WChar.avar('hine', 'achiev_wear', get_wear_var('hine')) == 'soap'", "images/Sprite/hine/hine body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "HINE HEADFG",
    (-600,0), ConditionSwitch(
        "WChar.gvar('hine', 'itemL') == 0", "images/Sprite/_General/item_l 0.webp",
        "WChar.gvar('hine', 'itemL') == 1", "images/Sprite/_General/item_l 1.webp",
        "True", "images/Sprite/_General/item_l 0.webp"
    ),
    (-600,0), ConditionSwitch(
        "WChar.gvar('hine', 'itemR') == 0", "images/Sprite/_General/item_r 0.webp",
        "WChar.gvar('hine', 'itemR') == 1", "images/Sprite/_General/item_r 1.webp",
        "True", "images/Sprite/_General/item_r 0.webp"
    ),
    )

# WSIS

image WSIS STYLE = Composite(
    (720,1080),
    (0,0), "WSIS HEADBG",
    (0,0), ConditionSwitch(
        "len(WChar.gvar('wsis', 'achiev_wear')) > 0 and isinstance(WChar.gvar('wsis', 'achiev_wear')[a_menu_8], str)", "images/Sprite/wsis/wsis body 1.webp",
        "True", "images/Sprite/wsis/wsis body 0.webp"
    ),
    (0,0), ConditionSwitch(
        "len(WChar.gvar('wsis', 'achiev_wear')) > 0 and WChar.avar('wsis', 'achiev_wear', get_wear_var('wsis')) == 'home'", "images/Sprite/wsis/wsis body_wear home.webp",
        "len(WChar.gvar('wsis', 'achiev_wear')) > 0 and WChar.avar('wsis', 'achiev_wear', get_wear_var('wsis')) == 'under'", "images/Sprite/wsis/wsis body_wear under.webp",
        "len(WChar.gvar('wsis', 'achiev_wear')) > 0 and WChar.avar('wsis', 'achiev_wear', get_wear_var('wsis')) == 'sleep'", "images/Sprite/wsis/wsis body_wear sleep.webp",
        "len(WChar.gvar('wsis', 'achiev_wear')) > 0 and WChar.avar('wsis', 'achiev_wear', get_wear_var('wsis')) == 'casual'", "images/Sprite/wsis/wsis body_wear casual.webp",
        "len(WChar.gvar('wsis', 'achiev_wear')) > 0 and WChar.avar('wsis', 'achiev_wear', get_wear_var('wsis')) == 'school'", "images/Sprite/wsis/wsis body_wear school.webp",
        "len(WChar.gvar('wsis', 'achiev_wear')) > 0 and WChar.avar('wsis', 'achiev_wear', get_wear_var('wsis')) == 'school_swim'", "images/Sprite/wsis/wsis body_wear school_swim.webp",
        "len(WChar.gvar('wsis', 'achiev_wear')) > 0 and WChar.avar('wsis', 'achiev_wear', get_wear_var('wsis')) == 'school_sport'", "images/Sprite/wsis/wsis body_wear school_sport.webp",
        "len(WChar.gvar('wsis', 'achiev_wear')) > 0 and WChar.avar('wsis', 'achiev_wear', get_wear_var('wsis')) == 'soap'", "images/Sprite/wsis/wsis body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "WSIS HEADFG",
    )

# WNEI

image WNEI STYLE = Composite(
    (720,1080),
    (0,0), "WNEI HEADBG",
    (0,0), ConditionSwitch(
        "isinstance(WChar.gvar('wnei', 'wear'), str)", "images/Sprite/wnei/wnei body 1.webp",
        "True", "images/Sprite/wnei/wnei body 0.webp"
    ),
    (0,0), ConditionSwitch(
        "len(WChar.gvar('wnei', 'achiev_wear')) > 0 and WChar.avar('wnei', 'achiev_wear', get_wear_var('wnei')) == 'home'", "images/Sprite/wnei/wnei body_wear home.webp",
        "len(WChar.gvar('wnei', 'achiev_wear')) > 0 and WChar.avar('wnei', 'achiev_wear', get_wear_var('wnei')) == 'under'", "images/Sprite/wnei/wnei body_wear under.webp",
        "len(WChar.gvar('wnei', 'achiev_wear')) > 0 and WChar.avar('wnei', 'achiev_wear', get_wear_var('wnei')) == 'sleep'", "images/Sprite/wnei/wnei body_wear sleep.webp",
        "len(WChar.gvar('wnei', 'achiev_wear')) > 0 and WChar.avar('wnei', 'achiev_wear', get_wear_var('wnei')) == 'casual'", "images/Sprite/wnei/wnei body_wear casual.webp",
        "len(WChar.gvar('wnei', 'achiev_wear')) > 0 and WChar.avar('wnei', 'achiev_wear', get_wear_var('wnei')) == 'school'", "images/Sprite/wnei/wnei body_wear school.webp",
        "len(WChar.gvar('wnei', 'achiev_wear')) > 0 and WChar.avar('wnei', 'achiev_wear', get_wear_var('wnei')) == 'school_swim'", "images/Sprite/wnei/wnei body_wear school_swim.webp",
        "len(WChar.gvar('wnei', 'achiev_wear')) > 0 and WChar.avar('wnei', 'achiev_wear', get_wear_var('wnei')) == 'school_sport'", "images/Sprite/wnei/wnei body_wear school_sport.webp",
        "len(WChar.gvar('wnei', 'achiev_wear')) > 0 and WChar.avar('wnei', 'achiev_wear', get_wear_var('wnei')) == 'soap'", "images/Sprite/wnei/wnei body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "WNEI HEADFG",
    )

# WMOM

image WMOM STYLE = Composite(
    (720,1080),
    (0,0), "WMOM HEADBG",
    (0,0), ConditionSwitch(
        "isinstance(WChar.gvar('wmom', 'wear'), str)", "images/Sprite/wmom/wmom body 1.webp",
        "True", "images/Sprite/wmom/wmom body 0.webp"
    ),
    (0,0), ConditionSwitch(
        "len(WChar.gvar('wmom', 'achiev_wear')) > 0 and WChar.avar('wmom', 'achiev_wear', get_wear_var('wmom')) == 'home'", "images/Sprite/wmom/wmom body_wear home.webp",
        "len(WChar.gvar('wmom', 'achiev_wear')) > 0 and WChar.avar('wmom', 'achiev_wear', get_wear_var('wmom')) == 'under'", "images/Sprite/wmom/wmom body_wear under.webp",
        "len(WChar.gvar('wmom', 'achiev_wear')) > 0 and WChar.avar('wmom', 'achiev_wear', get_wear_var('wmom')) == 'sleep'", "images/Sprite/wmom/wmom body_wear sleep.webp",
        "len(WChar.gvar('wmom', 'achiev_wear')) > 0 and WChar.avar('wmom', 'achiev_wear', get_wear_var('wmom')) == 'casual'", "images/Sprite/wmom/wmom body_wear casual.webp",
        "len(WChar.gvar('wmom', 'achiev_wear')) > 0 and WChar.avar('wmom', 'achiev_wear', get_wear_var('wmom')) == 'school'", "images/Sprite/wmom/wmom body_wear school.webp",
        "len(WChar.gvar('wmom', 'achiev_wear')) > 0 and WChar.avar('wmom', 'achiev_wear', get_wear_var('wmom')) == 'school_swim'", "images/Sprite/wmom/wmom body_wear school_swim.webp",
        "len(WChar.gvar('wmom', 'achiev_wear')) > 0 and WChar.avar('wmom', 'achiev_wear', get_wear_var('wmom')) == 'school_sport'", "images/Sprite/wmom/wmom body_wear school_sport.webp",
        "len(WChar.gvar('wmom', 'achiev_wear')) > 0 and WChar.avar('wmom', 'achiev_wear', get_wear_var('wmom')) == 'soap'", "images/Sprite/wmom/wmom body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "WMOM HEADFG",
    (-600,0), ConditionSwitch(
        "WChar.gvar('wmom', 'itemL') == 0", "images/Sprite/_General/item_l 0.webp",
        "WChar.gvar('wmom', 'itemL') == 1", "images/Sprite/_General/item_l 1.webp",
        "True", "images/Sprite/_General/item_l 0.webp"
    ),
    (-600,0), ConditionSwitch(
        "WChar.gvar('wmom', 'itemR') == 0", "images/Sprite/_General/item_r 0.webp",
        "WChar.gvar('wmom', 'itemR') == 1", "images/Sprite/_General/item_r 1.webp",
        "True", "images/Sprite/_General/item_r 0.webp"
    ),
    )

# WGMA

image WGMA STYLE = Composite(
    (720,1080),
    (0,0), "WGMA HEADBG",
    (0,0), "images/Sprite/wgma/wgma body 1.webp",
    (0,0), ConditionSwitch(
        "len(WChar.gvar('wgma', 'achiev_wear')) > 0 and WChar.avar('wgma', 'achiev_wear', get_wear_var('wgma')) == 'home'", "images/Sprite/wgma/wgma body_wear home.webp",
        "len(WChar.gvar('wgma', 'achiev_wear')) > 0 and WChar.avar('wgma', 'achiev_wear', get_wear_var('wgma')) == 'under'", "images/Sprite/wgma/wgma body_wear under.webp",
        "len(WChar.gvar('wgma', 'achiev_wear')) > 0 and WChar.avar('wgma', 'achiev_wear', get_wear_var('wgma')) == 'sleep'", "images/Sprite/wgma/wgma body_wear sleep.webp",
        "len(WChar.gvar('wgma', 'achiev_wear')) > 0 and WChar.avar('wgma', 'achiev_wear', get_wear_var('wgma')) == 'casual'", "images/Sprite/wgma/wgma body_wear casual.webp",
        "len(WChar.gvar('wgma', 'achiev_wear')) > 0 and WChar.avar('wgma', 'achiev_wear', get_wear_var('wgma')) == 'school'", "images/Sprite/wgma/wgma body_wear school.webp",
        "len(WChar.gvar('wgma', 'achiev_wear')) > 0 and WChar.avar('wgma', 'achiev_wear', get_wear_var('wgma')) == 'school_swim'", "images/Sprite/wgma/wgma body_wear school_swim.webp",
        "len(WChar.gvar('wgma', 'achiev_wear')) > 0 and WChar.avar('wgma', 'achiev_wear', get_wear_var('wgma')) == 'school_sport'", "images/Sprite/wgma/wgma body_wear school_sport.webp",
        "len(WChar.gvar('wgma', 'achiev_wear')) > 0 and WChar.avar('wgma', 'achiev_wear', get_wear_var('wgma')) == 'soap'", "images/Sprite/wgma/wgma body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "WGMA HEADFG",
    (-600,0), ConditionSwitch(
        "WChar.gvar('wgma', 'itemL') == 0", "images/Sprite/_General/item_l 0.webp",
        "WChar.gvar('wgma', 'itemL') == 1", "images/Sprite/_General/item_l 1.webp",
        "True", "images/Sprite/_General/item_l 0.webp"
    ),
    (-600,0), ConditionSwitch(
        "WChar.gvar('wgma', 'itemR') == 0", "images/Sprite/_General/item_r 0.webp",
        "WChar.gvar('wgma', 'itemR') == 1", "images/Sprite/_General/item_r 1.webp",
        "True", "images/Sprite/_General/item_r 0.webp"
    ),
    )

# WCOU

image WCOU STYLE = Composite(
    (720,1080),
    (0,0), "WCOU HEADBG",
    (0,0), ConditionSwitch(
        "isinstance(WChar.gvar('wcou', 'wear'), str)", "images/Sprite/wcou/wcou body 1.webp",
        "True", "images/Sprite/wcou/wcou body 1.webp"
    ),
    (0,0), ConditionSwitch(
        "len(WChar.gvar('wcou', 'achiev_wear')) > 0 and WChar.avar('wcou', 'achiev_wear', get_wear_var('wcou')) == 'home'", "images/Sprite/wcou/wcou body_wear home.webp",
        "len(WChar.gvar('wcou', 'achiev_wear')) > 0 and WChar.avar('wcou', 'achiev_wear', get_wear_var('wcou')) == 'under'", "images/Sprite/wcou/wcou body_wear under.webp",
        "len(WChar.gvar('wcou', 'achiev_wear')) > 0 and WChar.avar('wcou', 'achiev_wear', get_wear_var('wcou')) == 'sleep'", "images/Sprite/wcou/wcou body_wear sleep.webp",
        "len(WChar.gvar('wcou', 'achiev_wear')) > 0 and WChar.avar('wcou', 'achiev_wear', get_wear_var('wcou')) == 'casual'", "images/Sprite/wcou/wcou body_wear casual.webp",
        "len(WChar.gvar('wcou', 'achiev_wear')) > 0 and WChar.avar('wcou', 'achiev_wear', get_wear_var('wcou')) == 'work'", "images/Sprite/wcou/wcou body_wear work_1.webp",
        "len(WChar.gvar('wcou', 'achiev_wear')) > 0 and WChar.avar('wcou', 'achiev_wear', get_wear_var('wcou')) == 'work2'", "images/Sprite/wcou/wcou body_wear work_2.webp",
        "True", Null()
    ),
    (0,0), "WCOU HEADFG",
    (-600,0), ConditionSwitch(
        "WChar.gvar('wcou', 'itemL') == 0", "images/Sprite/_General/item_l 0.webp",
        "WChar.gvar('wcou', 'itemL') == 1", "images/Sprite/_General/item_l 1.webp",
        "True", "images/Sprite/_General/item_l 0.webp"
    ),
    (-600,0), ConditionSwitch(
        "WChar.gvar('wcou', 'itemR') == 0", "images/Sprite/_General/item_r 0.webp",
        "WChar.gvar('wcou', 'itemR') == 1", "images/Sprite/_General/item_r 1.webp",
        "True", "images/Sprite/_General/item_r 0.webp"
    ),
    )

# WPRE

image WPRE STYLE = Composite(
    (720,1080),
    (0,0), "WPRE HEADBG",
    (0,0), ConditionSwitch(
        "isinstance(WChar.gvar('wpre', 'wear'), str)", "images/Sprite/wpre/wpre body 1.webp",
        "True", "images/Sprite/wpre/wpre body 0.webp"
    ),
    (0,0), ConditionSwitch(
        "len(WChar.gvar('wpre', 'achiev_wear')) > 0 and WChar.avar('wpre', 'achiev_wear', get_wear_var('wpre')) == 'home'", "images/Sprite/wpre/wpre body_wear home.webp",
        "len(WChar.gvar('wpre', 'achiev_wear')) > 0 and WChar.avar('wpre', 'achiev_wear', get_wear_var('wpre')) == 'under'", "images/Sprite/wpre/wpre body_wear under.webp",
        "len(WChar.gvar('wpre', 'achiev_wear')) > 0 and WChar.avar('wpre', 'achiev_wear', get_wear_var('wpre')) == 'sleep'", "images/Sprite/wpre/wpre body_wear sleep.webp",
        "len(WChar.gvar('wpre', 'achiev_wear')) > 0 and WChar.avar('wpre', 'achiev_wear', get_wear_var('wpre')) == 'casual'", "images/Sprite/wpre/wpre body_wear casual.webp",
        "len(WChar.gvar('wpre', 'achiev_wear')) > 0 and WChar.avar('wpre', 'achiev_wear', get_wear_var('wpre')) == 'school'", "images/Sprite/wpre/wpre body_wear school.webp",
        "len(WChar.gvar('wpre', 'achiev_wear')) > 0 and WChar.avar('wpre', 'achiev_wear', get_wear_var('wpre')) == 'school_swim'", "images/Sprite/wpre/wpre body_wear school_swim.webp",
        "len(WChar.gvar('wpre', 'achiev_wear')) > 0 and WChar.avar('wpre', 'achiev_wear', get_wear_var('wpre')) == 'school_sport'", "images/Sprite/wpre/wpre body_wear school_sport.webp",
        "len(WChar.gvar('wpre', 'achiev_wear')) > 0 and WChar.avar('wpre', 'achiev_wear', get_wear_var('wpre')) == 'soap'", "images/Sprite/wpre/wpre body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "WPRE HEADFG",
    )

# WGAL

image WGAL STYLE = Composite(
    (720,1080),
    (0,0), "WGAL HEADBG",
    (0,0), ConditionSwitch(
        "isinstance(WChar.gvar('wgal', 'wear'), str)", "images/Sprite/wgal/wgal body 1.webp",
        "True", "images/Sprite/wgal/wgal body 0.webp"
    ),
    (0,0), ConditionSwitch(
        "len(WChar.gvar('wgal', 'achiev_wear')) > 0 and WChar.avar('wgal', 'achiev_wear', get_wear_var('wgal')) == 'home'", "images/Sprite/wgal/wgal body_wear home.webp",
        "len(WChar.gvar('wgal', 'achiev_wear')) > 0 and WChar.avar('wgal', 'achiev_wear', get_wear_var('wgal')) == 'under'", "images/Sprite/wgal/wgal body_wear under.webp",
        "len(WChar.gvar('wgal', 'achiev_wear')) > 0 and WChar.avar('wgal', 'achiev_wear', get_wear_var('wgal')) == 'sleep'", "images/Sprite/wgal/wgal body_wear sleep.webp",
        "len(WChar.gvar('wgal', 'achiev_wear')) > 0 and WChar.avar('wgal', 'achiev_wear', get_wear_var('wgal')) == 'casual'", "images/Sprite/wgal/wgal body_wear casual.webp",
        "len(WChar.gvar('wgal', 'achiev_wear')) > 0 and WChar.avar('wgal', 'achiev_wear', get_wear_var('wgal')) == 'school'", "images/Sprite/wgal/wgal body_wear school.webp",
        "len(WChar.gvar('wgal', 'achiev_wear')) > 0 and WChar.avar('wgal', 'achiev_wear', get_wear_var('wgal')) == 'school_swim'", "images/Sprite/wgal/wgal body_wear school_swim.webp",
        "len(WChar.gvar('wgal', 'achiev_wear')) > 0 and WChar.avar('wgal', 'achiev_wear', get_wear_var('wgal')) == 'school_sport'", "images/Sprite/wgal/wgal body_wear school_sport.webp",
        "len(WChar.gvar('wgal', 'achiev_wear')) > 0 and WChar.avar('wgal', 'achiev_wear', get_wear_var('wgal')) == 'soap'", "images/Sprite/wgal/wgal body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "WGAL HEADFG",
    (-600,0), ConditionSwitch(
        "WChar.gvar('wgal', 'itemL') == 0", "images/Sprite/_General/item_l 0.webp",
        "WChar.gvar('wgal', 'itemL') == 1", "images/Sprite/_General/item_l 1.webp",
        "True", "images/Sprite/_General/item_l 0.webp"
    ),
    (-600,0), ConditionSwitch(
        "WChar.gvar('wgal', 'itemR') == 0", "images/Sprite/_General/item_r 0.webp",
        "WChar.gvar('wgal', 'itemR') == 1", "images/Sprite/_General/item_r 1.webp",
        "True", "images/Sprite/_General/item_r 0.webp"
    ),
    )

# WOTA

image WOTA STYLE = Composite(
    (720,1080),
    (0,0), "WOTA HEADBG",
    (0,0), ConditionSwitch(
        "isinstance(WChar.gvar('wota', 'wear'), str)", "images/Sprite/wota/wota body 1.webp",
        "True", "images/Sprite/wota/wota body 0.webp"
    ),
    (0,0), ConditionSwitch(
        "len(WChar.gvar('wota', 'achiev_wear')) > 0 and WChar.avar('wota', 'achiev_wear', get_wear_var('wota')) == 'home'", "images/Sprite/wota/wota body_wear home.webp",
        "len(WChar.gvar('wota', 'achiev_wear')) > 0 and WChar.avar('wota', 'achiev_wear', get_wear_var('wota')) == 'under'", "images/Sprite/wota/wota body_wear under.webp",
        "len(WChar.gvar('wota', 'achiev_wear')) > 0 and WChar.avar('wota', 'achiev_wear', get_wear_var('wota')) == 'sleep'", "images/Sprite/wota/wota body_wear sleep.webp",
        "len(WChar.gvar('wota', 'achiev_wear')) > 0 and WChar.avar('wota', 'achiev_wear', get_wear_var('wota')) == 'casual'", "images/Sprite/wota/wota body_wear casual.webp",
        "len(WChar.gvar('wota', 'achiev_wear')) > 0 and WChar.avar('wota', 'achiev_wear', get_wear_var('wota')) == 'school'", "images/Sprite/wota/wota body_wear school.webp",
        "len(WChar.gvar('wota', 'achiev_wear')) > 0 and WChar.avar('wota', 'achiev_wear', get_wear_var('wota')) == 'school_swim'", "images/Sprite/wota/wota body_wear school_swim.webp",
        "len(WChar.gvar('wota', 'achiev_wear')) > 0 and WChar.avar('wota', 'achiev_wear', get_wear_var('wota')) == 'school_sport'", "images/Sprite/wota/wota body_wear school_sport.webp",
        "len(WChar.gvar('wota', 'achiev_wear')) > 0 and WChar.avar('wota', 'achiev_wear', get_wear_var('wota')) == 'soap'", "images/Sprite/wota/wota body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "WOTA HEADFG",
    (-600,0), ConditionSwitch(
        "WChar.gvar('wota', 'itemL') == 0", "images/Sprite/_General/item_l 0.webp",
        "WChar.gvar('wota', 'itemL') == 1", "images/Sprite/_General/item_l 1.webp",
        "True", "images/Sprite/_General/item_l 0.webp"
    ),
    (-600,0), ConditionSwitch(
        "WChar.gvar('wota', 'itemR') == 0", "images/Sprite/_General/item_r 0.webp",
        "WChar.gvar('wota', 'itemR') == 1", "images/Sprite/_General/item_r 1.webp",
        "True", "images/Sprite/_General/item_r 0.webp"
    ),
    )

# WDIS

image WDIS STYLE = Composite(
    (720,1080),
    (0,0), "WDIS HEADBG",
    (0,0), ConditionSwitch(
        "isinstance(WChar.gvar('wdis', 'wear'), str)", "images/Sprite/wdis/wdis body 1.webp",
        "True", "images/Sprite/wdis/wdis body 0.webp"
    ),
    (0,0), ConditionSwitch(
        "len(WChar.gvar('wdis', 'achiev_wear')) > 0 and WChar.avar('wdis', 'achiev_wear', get_wear_var('wdis')) == 'home'", "images/Sprite/wdis/wdis body_wear home.webp",
        "len(WChar.gvar('wdis', 'achiev_wear')) > 0 and WChar.avar('wdis', 'achiev_wear', get_wear_var('wdis')) == 'under'", "images/Sprite/wdis/wdis body_wear under.webp",
        "len(WChar.gvar('wdis', 'achiev_wear')) > 0 and WChar.avar('wdis', 'achiev_wear', get_wear_var('wdis')) == 'sleep'", "images/Sprite/wdis/wdis body_wear sleep.webp",
        "len(WChar.gvar('wdis', 'achiev_wear')) > 0 and WChar.avar('wdis', 'achiev_wear', get_wear_var('wdis')) == 'casual'", "images/Sprite/wdis/wdis body_wear casual.webp",
        "len(WChar.gvar('wdis', 'achiev_wear')) > 0 and WChar.avar('wdis', 'achiev_wear', get_wear_var('wdis')) == 'school'", "images/Sprite/wdis/wdis body_wear school.webp",
        "len(WChar.gvar('wdis', 'achiev_wear')) > 0 and WChar.avar('wdis', 'achiev_wear', get_wear_var('wdis')) == 'school_swim'", "images/Sprite/wdis/wdis body_wear school_swim.webp",
        "len(WChar.gvar('wdis', 'achiev_wear')) > 0 and WChar.avar('wdis', 'achiev_wear', get_wear_var('wdis')) == 'school_sport'", "images/Sprite/wdis/wdis body_wear school_sport.webp",
        "len(WChar.gvar('wdis', 'achiev_wear')) > 0 and WChar.avar('wdis', 'achiev_wear', get_wear_var('wdis')) == 'soap'", "images/Sprite/wdis/wdis body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "WDIS HEADFG",
    (-600,0), ConditionSwitch(
        "WChar.gvar('wdis', 'itemL') == 0", "images/Sprite/_General/item_l 0.webp",
        "WChar.gvar('wdis', 'itemL') == 1", "images/Sprite/_General/item_l 1.webp",
        "True", "images/Sprite/_General/item_l 0.webp"
    ),
    (-600,0), ConditionSwitch(
        "WChar.gvar('wdis', 'itemR') == 0", "images/Sprite/_General/item_r 0.webp",
        "WChar.gvar('wdis', 'itemR') == 1", "images/Sprite/_General/item_r 1.webp",
        "True", "images/Sprite/_General/item_r 0.webp"
    ),
    )

# WRIC

image WRIC STYLE = Composite(
    (720,1080),
    (0,0), "WRIC HEADBG",
    (0,0), "images/Sprite/wric/wric body.webp",
    (0,0), ConditionSwitch(
        "len(WChar.gvar('wric', 'achiev_wear')) > 0 and WChar.avar('wric', 'achiev_wear', get_wear_var('wric')) == 'home'", "images/Sprite/wric/wric body_wear home.webp",
        "len(WChar.gvar('wric', 'achiev_wear')) > 0 and WChar.avar('wric', 'achiev_wear', get_wear_var('wric')) == 'under'", "images/Sprite/wric/wric body_wear under.webp",
        "len(WChar.gvar('wric', 'achiev_wear')) > 0 and WChar.avar('wric', 'achiev_wear', get_wear_var('wric')) == 'sleep'", "images/Sprite/wric/wric body_wear sleep.webp",
        "len(WChar.gvar('wric', 'achiev_wear')) > 0 and WChar.avar('wric', 'achiev_wear', get_wear_var('wric')) == 'casual'", "images/Sprite/wric/wric body_wear casual.webp",
        "len(WChar.gvar('wric', 'achiev_wear')) > 0 and WChar.avar('wric', 'achiev_wear', get_wear_var('wric')) == 'school'", "images/Sprite/wric/wric body_wear school.webp",
        "len(WChar.gvar('wric', 'achiev_wear')) > 0 and WChar.avar('wric', 'achiev_wear', get_wear_var('wric')) == 'school_swim'", "images/Sprite/wric/wric body_wear school_swim.webp",
        "len(WChar.gvar('wric', 'achiev_wear')) > 0 and WChar.avar('wric', 'achiev_wear', get_wear_var('wric')) == 'school_sport'", "images/Sprite/wric/wric body_wear school_sport.webp",
        "len(WChar.gvar('wric', 'achiev_wear')) > 0 and WChar.avar('wric', 'achiev_wear', get_wear_var('wric')) == 'soap'", "images/Sprite/wric/wric body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "WRIC HEADFG",
    )

# WUZA

image WUZA STYLE = Composite(
    (720,1080),
    (0,0), "WUZA HEADBG",
    (0,0), ConditionSwitch(
        "isinstance(WChar.gvar('wuza', 'wear'), str)", "images/Sprite/wuza/wuza body 1.webp",
        "True", "images/Sprite/wuza/wuza body 0.webp"
    ),
    (0,0), ConditionSwitch(
        "len(WChar.gvar('wuza', 'achiev_wear')) > 0 and WChar.avar('wuza', 'achiev_wear', get_wear_var('wuza')) == 'home'", "images/Sprite/wuza/wuza body_wear home.webp",
        "len(WChar.gvar('wuza', 'achiev_wear')) > 0 and WChar.avar('wuza', 'achiev_wear', get_wear_var('wuza')) == 'under'", "images/Sprite/wuza/wuza body_wear under.webp",
        "len(WChar.gvar('wuza', 'achiev_wear')) > 0 and WChar.avar('wuza', 'achiev_wear', get_wear_var('wuza')) == 'sleep'", "images/Sprite/wuza/wuza body_wear sleep.webp",
        "len(WChar.gvar('wuza', 'achiev_wear')) > 0 and WChar.avar('wuza', 'achiev_wear', get_wear_var('wuza')) == 'casual'", "images/Sprite/wuza/wuza body_wear casual.webp",
        "len(WChar.gvar('wuza', 'achiev_wear')) > 0 and WChar.avar('wuza', 'achiev_wear', get_wear_var('wuza')) == 'school'", "images/Sprite/wuza/wuza body_wear school.webp",
        "len(WChar.gvar('wuza', 'achiev_wear')) > 0 and WChar.avar('wuza', 'achiev_wear', get_wear_var('wuza')) == 'school_swim'", "images/Sprite/wuza/wuza body_wear school_swim.webp",
        "len(WChar.gvar('wuza', 'achiev_wear')) > 0 and WChar.avar('wuza', 'achiev_wear', get_wear_var('wuza')) == 'school_sport'", "images/Sprite/wuza/wuza body_wear school_sport.webp",
        "len(WChar.gvar('wuza', 'achiev_wear')) > 0 and WChar.avar('wuza', 'achiev_wear', get_wear_var('wuza')) == 'soap'", "images/Sprite/wuza/wuza body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "WUZA HEADFG",
    (-600,0), ConditionSwitch(
        "WChar.gvar('wuza', 'itemL') == 0", "images/Sprite/_General/item_l 0.webp",
        "WChar.gvar('wuza', 'itemL') == 1", "images/Sprite/_General/item_l 1.webp",
        "True", "images/Sprite/_General/item_l 0.webp"
    ),
    (-600,0), ConditionSwitch(
        "WChar.gvar('wuza', 'itemR') == 0", "images/Sprite/_General/item_r 0.webp",
        "WChar.gvar('wuza', 'itemR') == 1", "images/Sprite/_General/item_r 1.webp",
        "True", "images/Sprite/_General/item_r 0.webp"
    ),
    )

# WLAZ

image WLAZ STYLE = Composite(
    (720,1080),
    (0,0), "WLAZ HEADBG",
    (0,0), ConditionSwitch(
        "isinstance(WChar.gvar('wlaz', 'wear'), str)", "images/Sprite/wlaz/wlaz body 1.webp",
        "True", "images/Sprite/wlaz/wlaz body 0.webp"
    ),
    (0,0), ConditionSwitch(
        "len(WChar.gvar('wlaz', 'achiev_wear')) > 0 and WChar.avar('wlaz', 'achiev_wear', get_wear_var('wlaz')) == 'home'", "images/Sprite/wlaz/wlaz body_wear home.webp",
        "len(WChar.gvar('wlaz', 'achiev_wear')) > 0 and WChar.avar('wlaz', 'achiev_wear', get_wear_var('wlaz')) == 'under'", "images/Sprite/wlaz/wlaz body_wear under.webp",
        "len(WChar.gvar('wlaz', 'achiev_wear')) > 0 and WChar.avar('wlaz', 'achiev_wear', get_wear_var('wlaz')) == 'sleep'", "images/Sprite/wlaz/wlaz body_wear sleep.webp",
        "len(WChar.gvar('wlaz', 'achiev_wear')) > 0 and WChar.avar('wlaz', 'achiev_wear', get_wear_var('wlaz')) == 'casual'", "images/Sprite/wlaz/wlaz body_wear casual.webp",
        "len(WChar.gvar('wlaz', 'achiev_wear')) > 0 and WChar.avar('wlaz', 'achiev_wear', get_wear_var('wlaz')) == 'school'", "images/Sprite/wlaz/wlaz body_wear school.webp",
        "len(WChar.gvar('wlaz', 'achiev_wear')) > 0 and WChar.avar('wlaz', 'achiev_wear', get_wear_var('wlaz')) == 'school_swim'", "images/Sprite/wlaz/wlaz body_wear school_swim.webp",
        "len(WChar.gvar('wlaz', 'achiev_wear')) > 0 and WChar.avar('wlaz', 'achiev_wear', get_wear_var('wlaz')) == 'school_sport'", "images/Sprite/wlaz/wlaz body_wear school_sport.webp",
        "len(WChar.gvar('wlaz', 'achiev_wear')) > 0 and WChar.avar('wlaz', 'achiev_wear', get_wear_var('wlaz')) == 'soap'", "images/Sprite/wlaz/wlaz body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "WLAZ HEADFG",
    (-600,0), ConditionSwitch(
        "WChar.gvar('wlaz', 'itemL') == 0", "images/Sprite/_General/item_l 0.webp",
        "WChar.gvar('wlaz', 'itemL') == 1", "images/Sprite/_General/item_l 1.webp",
        "True", "images/Sprite/_General/item_l 0.webp"
    ),
    (-600,0), ConditionSwitch(
        "WChar.gvar('wlaz', 'itemR') == 0", "images/Sprite/_General/item_r 0.webp",
        "WChar.gvar('wlaz', 'itemR') == 1", "images/Sprite/_General/item_r 1.webp",
        "True", "images/Sprite/_General/item_r 0.webp"
    ),
    )

# WDEL

image WDEL STYLE = Composite(
    (720,1080),
    (0,0), "WDEL HEADBG",
    (0,0), ConditionSwitch(
        "isinstance(WChar.gvar('wdel', 'wear'), str)", "images/Sprite/wdel/wdel body 1.webp",
        "True", "images/Sprite/wdel/wdel body 0.webp"
    ),
    (0,0), ConditionSwitch(
        "len(WChar.gvar('wdel', 'achiev_wear')) > 0 and WChar.avar('wdel', 'achiev_wear', get_wear_var('wdel')) == 'home'", "images/Sprite/wdel/wdel body_wear home.webp",
        "len(WChar.gvar('wdel', 'achiev_wear')) > 0 and WChar.avar('wdel', 'achiev_wear', get_wear_var('wdel')) == 'under'", "images/Sprite/wdel/wdel body_wear under.webp",
        "len(WChar.gvar('wdel', 'achiev_wear')) > 0 and WChar.avar('wdel', 'achiev_wear', get_wear_var('wdel')) == 'sleep'", "images/Sprite/wdel/wdel body_wear sleep.webp",
        "len(WChar.gvar('wdel', 'achiev_wear')) > 0 and WChar.avar('wdel', 'achiev_wear', get_wear_var('wdel')) == 'casual'", "images/Sprite/wdel/wdel body_wear casual.webp",
        "len(WChar.gvar('wdel', 'achiev_wear')) > 0 and WChar.avar('wdel', 'achiev_wear', get_wear_var('wdel')) == 'school'", "images/Sprite/wdel/wdel body_wear school.webp",
        "len(WChar.gvar('wdel', 'achiev_wear')) > 0 and WChar.avar('wdel', 'achiev_wear', get_wear_var('wdel')) == 'school_swim'", "images/Sprite/wdel/wdel body_wear school_swim.webp",
        "len(WChar.gvar('wdel', 'achiev_wear')) > 0 and WChar.avar('wdel', 'achiev_wear', get_wear_var('wdel')) == 'school_sport'", "images/Sprite/wdel/wdel body_wear school_sport.webp",
        "len(WChar.gvar('wdel', 'achiev_wear')) > 0 and WChar.avar('wdel', 'achiev_wear', get_wear_var('wdel')) == 'soap'", "images/Sprite/wdel/wdel body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "WDEL HEADFG",
    (-600,0), ConditionSwitch(
        "WChar.gvar('wdel', 'itemL') == 0", "images/Sprite/_General/item_l 0.webp",
        "WChar.gvar('wdel', 'itemL') == 1", "images/Sprite/_General/item_l 1.webp",
        "True", "images/Sprite/_General/item_l 0.webp"
    ),
    (-600,0), ConditionSwitch(
        "WChar.gvar('wdel', 'itemR') == 0", "images/Sprite/_General/item_r 0.webp",
        "WChar.gvar('wdel', 'itemR') == 1", "images/Sprite/_General/item_r 1.webp",
        "True", "images/Sprite/_General/item_r 0.webp"
    ),
    )

# WGOT

image WGOT STYLE = Composite(
    (720,1080),
    (0,0), "WGOT HEADBG",
    (0,0), ConditionSwitch(
        "isinstance(WChar.gvar('wgot', 'wear'), str)", "images/Sprite/wgot/wgot body 1.webp",
        "True", "images/Sprite/wgot/wgot body 0.webp"
    ),
    (0,0), ConditionSwitch(
        "len(WChar.gvar('wgot', 'achiev_wear')) > 0 and WChar.avar('wgot', 'achiev_wear', get_wear_var('wgot')) == 'home'", "images/Sprite/wgot/wgot body_wear home.webp",
        "len(WChar.gvar('wgot', 'achiev_wear')) > 0 and WChar.avar('wgot', 'achiev_wear', get_wear_var('wgot')) == 'under'", "images/Sprite/wgot/wgot body_wear under.webp",
        "len(WChar.gvar('wgot', 'achiev_wear')) > 0 and WChar.avar('wgot', 'achiev_wear', get_wear_var('wgot')) == 'sleep'", "images/Sprite/wgot/wgot body_wear sleep.webp",
        "len(WChar.gvar('wgot', 'achiev_wear')) > 0 and WChar.avar('wgot', 'achiev_wear', get_wear_var('wgot')) == 'casual'", "images/Sprite/wgot/wgot body_wear casual.webp",
        "len(WChar.gvar('wgot', 'achiev_wear')) > 0 and WChar.avar('wgot', 'achiev_wear', get_wear_var('wgot')) == 'school'", "images/Sprite/wgot/wgot body_wear school.webp",
        "len(WChar.gvar('wgot', 'achiev_wear')) > 0 and WChar.avar('wgot', 'achiev_wear', get_wear_var('wgot')) == 'school_swim'", "images/Sprite/wgot/wgot body_wear school_swim.webp",
        "len(WChar.gvar('wgot', 'achiev_wear')) > 0 and WChar.avar('wgot', 'achiev_wear', get_wear_var('wgot')) == 'school_sport'", "images/Sprite/wgot/wgot body_wear school_sport.webp",
        "len(WChar.gvar('wgot', 'achiev_wear')) > 0 and WChar.avar('wgot', 'achiev_wear', get_wear_var('wgot')) == 'soap'", "images/Sprite/wgot/wgot body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "WGOT HEADFG",
    (-600,0), ConditionSwitch(
        "WChar.gvar('wgot', 'itemL') == 0", "images/Sprite/_General/item_l 0.webp",
        "WChar.gvar('wgot', 'itemL') == 1", "images/Sprite/_General/item_l 1.webp",
        "True", "images/Sprite/_General/item_l 0.webp"
    ),
    (-600,0), ConditionSwitch(
        "WChar.gvar('wgot', 'itemR') == 0", "images/Sprite/_General/item_r 0.webp",
        "WChar.gvar('wgot', 'itemR') == 1", "images/Sprite/_General/item_r 1.webp",
        "True", "images/Sprite/_General/item_r 0.webp"
    ),
    )

# WDAN

image WDAN STYLE = Composite(
    (720,1080),
    (0,0), "WDAN HEADBG",
    (0,0), ConditionSwitch(
        "isinstance(WChar.gvar('wdan', 'wear'), str)", "images/Sprite/wdan/wdan body 1.webp",
        "True", "images/Sprite/wdan/wdan body 0.webp"
    ),
    (0,0), ConditionSwitch(
        "len(WChar.gvar('wdan', 'achiev_wear')) > 0 and WChar.avar('wdan', 'achiev_wear', get_wear_var('wdan')) == 'home'", "images/Sprite/wdan/wdan body_wear home.webp",
        "len(WChar.gvar('wdan', 'achiev_wear')) > 0 and WChar.avar('wdan', 'achiev_wear', get_wear_var('wdan')) == 'under'", "images/Sprite/wdan/wdan body_wear under.webp",
        "len(WChar.gvar('wdan', 'achiev_wear')) > 0 and WChar.avar('wdan', 'achiev_wear', get_wear_var('wdan')) == 'sleep'", "images/Sprite/wdan/wdan body_wear sleep.webp",
        "len(WChar.gvar('wdan', 'achiev_wear')) > 0 and WChar.avar('wdan', 'achiev_wear', get_wear_var('wdan')) == 'casual'", "images/Sprite/wdan/wdan body_wear casual.webp",
        "len(WChar.gvar('wdan', 'achiev_wear')) > 0 and WChar.avar('wdan', 'achiev_wear', get_wear_var('wdan')) == 'school'", "images/Sprite/wdan/wdan body_wear school.webp",
        "len(WChar.gvar('wdan', 'achiev_wear')) > 0 and WChar.avar('wdan', 'achiev_wear', get_wear_var('wdan')) == 'school_swim'", "images/Sprite/wdan/wdan body_wear school_swim.webp",
        "len(WChar.gvar('wdan', 'achiev_wear')) > 0 and WChar.avar('wdan', 'achiev_wear', get_wear_var('wdan')) == 'school_sport'", "images/Sprite/wdan/wdan body_wear school_sport.webp",
        "len(WChar.gvar('wdan', 'achiev_wear')) > 0 and WChar.avar('wdan', 'achiev_wear', get_wear_var('wdan')) == 'soap'", "images/Sprite/wdan/wdan body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "WDAN HEADFG",
    (-600,0), ConditionSwitch(
        "WChar.gvar('wdan', 'itemL') == 0", "images/Sprite/_General/item_l 0.webp",
        "WChar.gvar('wdan', 'itemL') == 1", "images/Sprite/_General/item_l 1.webp",
        "True", "images/Sprite/_General/item_l 0.webp"
    ),
    (-600,0), ConditionSwitch(
        "WChar.gvar('wdan', 'itemR') == 0", "images/Sprite/_General/item_r 0.webp",
        "WChar.gvar('wdan', 'itemR') == 1", "images/Sprite/_General/item_r 1.webp",
        "True", "images/Sprite/_General/item_r 0.webp"
    ),
    )

# WKUU

image WKUU STYLE = Composite(
    (720,1080),
    (0,0), "WKUU HEADBG",
    (0,0), ConditionSwitch(
        "isinstance(WChar.gvar('wkuu', 'wear'), str)", "images/Sprite/wkuu/wkuu body 1.webp",
        "True", "images/Sprite/wkuu/wkuu body 0.webp"
    ),
    (0,0), ConditionSwitch(
        "len(WChar.gvar('wkuu', 'achiev_wear')) > 0 and WChar.avar('wkuu', 'achiev_wear', get_wear_var('wkuu')) == 'home'", "images/Sprite/wkuu/wkuu body_wear home.webp",
        "len(WChar.gvar('wkuu', 'achiev_wear')) > 0 and WChar.avar('wkuu', 'achiev_wear', get_wear_var('wkuu')) == 'under'", "images/Sprite/wkuu/wkuu body_wear under.webp",
        "len(WChar.gvar('wkuu', 'achiev_wear')) > 0 and WChar.avar('wkuu', 'achiev_wear', get_wear_var('wkuu')) == 'sleep'", "images/Sprite/wkuu/wkuu body_wear sleep.webp",
        "len(WChar.gvar('wkuu', 'achiev_wear')) > 0 and WChar.avar('wkuu', 'achiev_wear', get_wear_var('wkuu')) == 'casual'", "images/Sprite/wkuu/wkuu body_wear casual.webp",
        "len(WChar.gvar('wkuu', 'achiev_wear')) > 0 and WChar.avar('wkuu', 'achiev_wear', get_wear_var('wkuu')) == 'school'", "images/Sprite/wkuu/wkuu body_wear school.webp",
        "len(WChar.gvar('wkuu', 'achiev_wear')) > 0 and WChar.avar('wkuu', 'achiev_wear', get_wear_var('wkuu')) == 'school_swim'", "images/Sprite/wkuu/wkuu body_wear school_swim.webp",
        "len(WChar.gvar('wkuu', 'achiev_wear')) > 0 and WChar.avar('wkuu', 'achiev_wear', get_wear_var('wkuu')) == 'school_sport'", "images/Sprite/wkuu/wkuu body_wear school_sport.webp",
        "len(WChar.gvar('wkuu', 'achiev_wear')) > 0 and WChar.avar('wkuu', 'achiev_wear', get_wear_var('wkuu')) == 'soap'", "images/Sprite/wkuu/wkuu body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "WKUU HEADFG",
    (-600,0), ConditionSwitch(
        "WChar.gvar('wkuu', 'itemL') == 0", "images/Sprite/_General/item_l 0.webp",
        "WChar.gvar('wkuu', 'itemL') == 1", "images/Sprite/_General/item_l 1.webp",
        "True", "images/Sprite/_General/item_l 0.webp"
    ),
    (-600,0), ConditionSwitch(
        "WChar.gvar('wkuu', 'itemR') == 0", "images/Sprite/_General/item_r 0.webp",
        "WChar.gvar('wkuu', 'itemR') == 1", "images/Sprite/_General/item_r 1.webp",
        "True", "images/Sprite/_General/item_r 0.webp"
    ),
    )

# WRIN

image WRIN STYLE = Composite(
    (720,1080),
    (0,0), "WRIN HEADBG",
    (0,0), ConditionSwitch(
        "isinstance(WChar.gvar('wrin', 'wear'), str)", "images/Sprite/wrin/wrin body 1.webp",
        "True", "images/Sprite/wrin/wrin body 0.webp"
    ),
    (0,0), ConditionSwitch(
        "len(WChar.gvar('wrin', 'achiev_wear')) > 0 and WChar.avar('wrin', 'achiev_wear', get_wear_var('wrin')) == 'home'", "images/Sprite/wrin/wrin body_wear home.webp",
        "len(WChar.gvar('wrin', 'achiev_wear')) > 0 and WChar.avar('wrin', 'achiev_wear', get_wear_var('wrin')) == 'under'", "images/Sprite/wrin/wrin body_wear under.webp",
        "len(WChar.gvar('wrin', 'achiev_wear')) > 0 and WChar.avar('wrin', 'achiev_wear', get_wear_var('wrin')) == 'sleep'", "images/Sprite/wrin/wrin body_wear sleep.webp",
        "len(WChar.gvar('wrin', 'achiev_wear')) > 0 and WChar.avar('wrin', 'achiev_wear', get_wear_var('wrin')) == 'casual'", "images/Sprite/wrin/wrin body_wear casual.webp",
        "len(WChar.gvar('wrin', 'achiev_wear')) > 0 and WChar.avar('wrin', 'achiev_wear', get_wear_var('wrin')) == 'school'", "images/Sprite/wrin/wrin body_wear school.webp",
        "len(WChar.gvar('wrin', 'achiev_wear')) > 0 and WChar.avar('wrin', 'achiev_wear', get_wear_var('wrin')) == 'school_swim'", "images/Sprite/wrin/wrin body_wear school_swim.webp",
        "len(WChar.gvar('wrin', 'achiev_wear')) > 0 and WChar.avar('wrin', 'achiev_wear', get_wear_var('wrin')) == 'school_sport'", "images/Sprite/wrin/wrin body_wear school_sport.webp",
        "len(WChar.gvar('wrin', 'achiev_wear')) > 0 and WChar.avar('wrin', 'achiev_wear', get_wear_var('wrin')) == 'soap'", "images/Sprite/wrin/wrin body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "WRIN HEADFG",
    (-600,0), ConditionSwitch(
        "WChar.gvar('wrin', 'itemL') == 0", "images/Sprite/_General/item_l 0.webp",
        "WChar.gvar('wrin', 'itemL') == 1", "images/Sprite/_General/item_l 1.webp",
        "True", "images/Sprite/_General/item_l 0.webp"
    ),
    (-600,0), ConditionSwitch(
        "WChar.gvar('wrin', 'itemR') == 0", "images/Sprite/_General/item_r 0.webp",
        "WChar.gvar('wrin', 'itemR') == 1", "images/Sprite/_General/item_r 1.webp",
        "True", "images/Sprite/_General/item_r 0.webp"
    ),
    )

# WSUK

image WSUK STYLE = Composite(
    (720,1080),
    (0,0), "WSUK HEADBG",
    (0,0), ConditionSwitch(
        "isinstance(WChar.gvar('wsuk', 'wear'), str)", "images/Sprite/wsuk/wsuk body 1.webp",
        "True", "images/Sprite/wsuk/wsuk body 0.webp"
    ),
    (0,0), ConditionSwitch(
        "len(WChar.gvar('wsuk', 'achiev_wear')) > 0 and WChar.avar('wsuk', 'achiev_wear', get_wear_var('wsuk')) == 'home'", "images/Sprite/wsuk/wsuk body_wear home.webp",
        "len(WChar.gvar('wsuk', 'achiev_wear')) > 0 and WChar.avar('wsuk', 'achiev_wear', get_wear_var('wsuk')) == 'under'", "images/Sprite/wsuk/wsuk body_wear under.webp",
        "len(WChar.gvar('wsuk', 'achiev_wear')) > 0 and WChar.avar('wsuk', 'achiev_wear', get_wear_var('wsuk')) == 'sleep'", "images/Sprite/wsuk/wsuk body_wear sleep.webp",
        "len(WChar.gvar('wsuk', 'achiev_wear')) > 0 and WChar.avar('wsuk', 'achiev_wear', get_wear_var('wsuk')) == 'casual'", "images/Sprite/wsuk/wsuk body_wear casual.webp",
        "len(WChar.gvar('wsuk', 'achiev_wear')) > 0 and WChar.avar('wsuk', 'achiev_wear', get_wear_var('wsuk')) == 'school'", "images/Sprite/wsuk/wsuk body_wear school.webp",
        "len(WChar.gvar('wsuk', 'achiev_wear')) > 0 and WChar.avar('wsuk', 'achiev_wear', get_wear_var('wsuk')) == 'school_swim'", "images/Sprite/wsuk/wsuk body_wear school_swim.webp",
        "len(WChar.gvar('wsuk', 'achiev_wear')) > 0 and WChar.avar('wsuk', 'achiev_wear', get_wear_var('wsuk')) == 'school_sport'", "images/Sprite/wsuk/wsuk body_wear school_sport.webp",
        "len(WChar.gvar('wsuk', 'achiev_wear')) > 0 and WChar.avar('wsuk', 'achiev_wear', get_wear_var('wsuk')) == 'soap'", "images/Sprite/wsuk/wsuk body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "WSUK HEADFG",
    (-600,0), ConditionSwitch(
        "WChar.gvar('wsuk', 'itemL') == 0", "images/Sprite/_General/item_l 0.webp",
        "WChar.gvar('wsuk', 'itemL') == 1", "images/Sprite/_General/item_l 1.webp",
        "True", "images/Sprite/_General/item_l 0.webp"
    ),
    (-600,0), ConditionSwitch(
        "WChar.gvar('wsuk', 'itemR') == 0", "images/Sprite/_General/item_r 0.webp",
        "WChar.gvar('wsuk', 'itemR') == 1", "images/Sprite/_General/item_r 1.webp",
        "True", "images/Sprite/_General/item_r 0.webp"
    ),
    )

# ----------------------------------------------------------------------------------------------------
# WMAM
# ----------------------------------------------------------------------------------------------------

image WMAM EYES:
    "images/Sprite/wmam/wmam eyes0.webp",
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
    "images/Sprite/wmam/wmam eyes2.webp",
    0.15
    "images/Sprite/wmam/wmam eyes1.webp",
    0.1
    repeat

image WMAM MOUTH:
    ConditionSwitch(
        "WChar.gvar('wmam', 'mood') == 'A1'", "images/Sprite/_General/mouth 0 A1.webp",
        "WChar.gvar('wmam', 'mood') == 'A2'", "images/Sprite/_General/mouth 0 A2.webp",
        "WChar.gvar('wmam', 'mood') == 'A3'", "images/Sprite/_General/mouth 0 A3.webp",
        "WChar.gvar('wmam', 'mood') == 'A4'", "images/Sprite/_General/mouth 0 A4.webp",
        "WChar.gvar('wmam', 'mood') == 'O1'", "images/Sprite/_General/mouth 0 O1.webp",
        "WChar.gvar('wmam', 'mood') == 'O2'", "images/Sprite/_General/mouth 0 O2.webp",
        "WChar.gvar('wmam', 'mood') == 'O3'", "images/Sprite/_General/mouth 0 O3.webp",
        "WChar.gvar('wmam', 'mood') == 'O4'", "images/Sprite/_General/mouth 0 O4.webp",
        "True", "images/Sprite/_General/mouth 0 A1.webp"
    ),
    .15
    ConditionSwitch(
        "WChar.gvar('wmam', 'mood') == 'A1'", "images/Sprite/_General/mouth 1 A1.webp",
        "WChar.gvar('wmam', 'mood') == 'A2'", "images/Sprite/_General/mouth 1 A2.webp",
        "WChar.gvar('wmam', 'mood') == 'A3'", "images/Sprite/_General/mouth 1 A3.webp",
        "WChar.gvar('wmam', 'mood') == 'A4'", "images/Sprite/_General/mouth 1 A4.webp",
        "WChar.gvar('wmam', 'mood') == 'O1'", "images/Sprite/_General/mouth 1 O1.webp",
        "WChar.gvar('wmam', 'mood') == 'O2'", "images/Sprite/_General/mouth 1 O2.webp",
        "WChar.gvar('wmam', 'mood') == 'O3'", "images/Sprite/_General/mouth 1 O3.webp",
        "WChar.gvar('wmam', 'mood') == 'O4'", "images/Sprite/_General/mouth 1 O4.webp",
        "True", "images/Sprite/_General/mouth 1 A1.webp"
    ),
    .15
    repeat

image WMAM WEAR:
    ConditionSwitch(
        "WChar.gvar('wmam', 'wear') == 'home'", "images/Sprite/wmam/wmam body_wear home.webp",
        "WChar.gvar('wmam', 'wear') == 'under'", Null(),
        "WChar.gvar('wmam', 'wear') == 'sleep'", Null(),
        "WChar.gvar('wmam', 'wear') == 'casual'", Null(),
        "WChar.gvar('wmam', 'wear') == 'dressy'", Null(),
        "WChar.gvar('wmam', 'wear') == 'formal'", Null(),
        "WChar.gvar('wmam', 'wear') == 'sport'", Null(),
        "WChar.gvar('wmam', 'wear') == 'swim'", Null(),
        "WChar.gvar('wmam', 'wear') == 'school'", Null(),
        "WChar.gvar('wmam', 'wear') == 'school_swim'", Null(),
        "WChar.gvar('wmam', 'wear') == 'school_sport'", Null(),
        "WChar.gvar('wmam', 'wear') == 'work'", Null(),
        "WChar.gvar('wmam', 'wear') == 'soap'", Null(),
        "True", Null()
    ),

image WMAM HEADFG PARTS = Composite(
    (720,1080),
    (0,0), "images/Sprite/wmam/wmam eyes3.webp",
    (0,0), "images/Sprite/wmam/wmam head_mg.webp",
    (0,0), "images/Sprite/wmam/wmam head_fg1.webp",
    (0,0), ConditionSwitch(
        "WChar.gvar('wmam', 'fx') == 0", "images/Sprite/_General/fx 0.webp",
        "WChar.gvar('wmam', 'fx') == 1", "images/Sprite/_General/fx 1.webp",
        "WChar.gvar('wmam', 'fx') == 2", "images/Sprite/_General/fx 2.webp",
        "WChar.gvar('wmam', 'fx') == 3", "images/Sprite/_General/fx 3.webp",
        "True", "images/Sprite/_General/fx 0.webp"
    ),
    (0,0), WhileSpeaking("wmam", "WMAM MOUTH", ConditionSwitch(
        "WChar.gvar('wmam', 'mood') == 'A1'", "images/Sprite/_General/mouth 0 A1.webp",
        "WChar.gvar('wmam', 'mood') == 'A2'", "images/Sprite/_General/mouth 0 A2.webp",
        "WChar.gvar('wmam', 'mood') == 'A3'", "images/Sprite/_General/mouth 0 A3.webp",
        "WChar.gvar('wmam', 'mood') == 'A4'", "images/Sprite/_General/mouth 0 A4.webp",
        "WChar.gvar('wmam', 'mood') == 'O1'", "images/Sprite/_General/mouth 0 O1.webp",
        "WChar.gvar('wmam', 'mood') == 'O2'", "images/Sprite/_General/mouth 0 O2.webp",
        "WChar.gvar('wmam', 'mood') == 'O3'", "images/Sprite/_General/mouth 0 O3.webp",
        "WChar.gvar('wmam', 'mood') == 'O4'", "images/Sprite/_General/mouth 0 O4.webp",
        "True", "images/Sprite/_General/mouth 0 A1.webp"
    )),
    (0,0), "WMAM EYES",
    (0,0), ConditionSwitch(
        "WChar.gvar('wmam', 'mood') == 'A1'", "images/Sprite/wmam/wmam eyebrow A1.webp",
        "WChar.gvar('wmam', 'mood') == 'A2'", "images/Sprite/wmam/wmam eyebrow A2.webp",
        "WChar.gvar('wmam', 'mood') == 'A3'", "images/Sprite/wmam/wmam eyebrow A3.webp",
        "WChar.gvar('wmam', 'mood') == 'A4'", "images/Sprite/wmam/wmam eyebrow A4.webp",
        "WChar.gvar('wmam', 'mood') == 'O1'", "images/Sprite/wmam/wmam eyebrow O1.webp",
        "WChar.gvar('wmam', 'mood') == 'O2'", "images/Sprite/wmam/wmam eyebrow O2.webp",
        "WChar.gvar('wmam', 'mood') == 'O3'", "images/Sprite/wmam/wmam eyebrow O3.webp",
        "WChar.gvar('wmam', 'mood') == 'O4'", "images/Sprite/wmam/wmam eyebrow O4.webp",
        "True", "images/Sprite/wmam/wmam eyebrow A1.webp"
    ),
    )

image WMAM HEADFG:
    "WMAM HEADFG PARTS"
    #zoom 1.5/wmam_size

image WMAM PARTS = Composite(
    (720,1080),
    (0,0), "images/Sprite/wmam/wmam head_bg.webp",
    (0,0), ConditionSwitch(
        "isinstance(wmam_wear, str)", "images/Sprite/wmam/wmam body 1.webp",
        "True", "images/Sprite/wmam/wmam body 0.webp"
    ),
    (0,0), "WMAM WEAR",
    (0,0), "WMAM HEADFG",
    )

image WMAM STYLE = Composite(
    (720,1080),
    (0,0), "images/Sprite/wmam/wmam head_bg.webp",
    (0,0), ConditionSwitch(
        "isinstance(wmam_wear, str)", "images/Sprite/wmam/wmam body 1.webp",
        "True", "images/Sprite/wmam/wmam body 0.webp"
    ),
    (0,0), ConditionSwitch(
        "len(WChar.gvar('wmam', 'achiev_wear')) > 0 and WChar.avar('wmam', 'achiev_wear', get_wear_var('wmam')) == 'home'", "images/Sprite/wmam/wmam body_wear home.webp",
        "len(WChar.gvar('wmam', 'achiev_wear')) > 0 and WChar.avar('wmam', 'achiev_wear', get_wear_var('wmam')) == 'under'", "images/Sprite/wmam/wmam body_wear under.webp",
        "len(WChar.gvar('wmam', 'achiev_wear')) > 0 and WChar.avar('wmam', 'achiev_wear', get_wear_var('wmam')) == 'sleep'", "images/Sprite/wmam/wmam body_wear sleep.webp",
        "len(WChar.gvar('wmam', 'achiev_wear')) > 0 and WChar.avar('wmam', 'achiev_wear', get_wear_var('wmam')) == 'casual'", "images/Sprite/wmam/wmam body_wear casual.webp",
        "len(WChar.gvar('wmam', 'achiev_wear')) > 0 and WChar.avar('wmam', 'achiev_wear', get_wear_var('wmam')) == 'school'", "images/Sprite/wmam/wmam body_wear school.webp",
        "len(WChar.gvar('wmam', 'achiev_wear')) > 0 and WChar.avar('wmam', 'achiev_wear', get_wear_var('wmam')) == 'school_swim'", "images/Sprite/wmam/wmam body_wear school_swim.webp",
        "len(WChar.gvar('wmam', 'achiev_wear')) > 0 and WChar.avar('wmam', 'achiev_wear', get_wear_var('wmam')) == 'school_sport'", "images/Sprite/wmam/wmam body_wear school_sport.webp",
        "len(WChar.gvar('wmam', 'achiev_wear')) > 0 and WChar.avar('wmam', 'achiev_wear', get_wear_var('wmam')) == 'soap'", "images/Sprite/wmam/wmam body_wear soap.webp",
        "True", Null()
    ),
    (0,0), "WMAM HEADFG",
    )

image WMAM:
    "WMAM PARTS"
    yalign 1.0
    ypos 1400
    zoom 0+(0.25+(1*wmam_size))*(0.25+(1*wmam_size))/2.5

# ----------------------------------------------------------------------------------------------------
# HPAP
# ----------------------------------------------------------------------------------------------------

image HPAP WEAR:
    ConditionSwitch(
        "WChar.gvar('hpap', 'wear') == 'home'", "images/Sprite/hpap/hpap body_wear home.webp",
        "WChar.gvar('hpap', 'wear') == 'under'", Null(),
        "WChar.gvar('hpap', 'wear') == 'sleep'", Null(),
        "WChar.gvar('hpap', 'wear') == 'casual'", Null(),
        "WChar.gvar('hpap', 'wear') == 'dressy'", Null(),
        "WChar.gvar('hpap', 'wear') == 'formal'", Null(),
        "WChar.gvar('hpap', 'wear') == 'sport'", Null(),
        "WChar.gvar('hpap', 'wear') == 'swim'", Null(),
        "WChar.gvar('hpap', 'wear') == 'school'", Null(),
        "WChar.gvar('hpap', 'wear') == 'school_swim'", Null(),
        "WChar.gvar('hpap', 'wear') == 'school_sport'", Null(),
        "WChar.gvar('hpap', 'wear') == 'work'", Null(),
        "WChar.gvar('hpap', 'wear') == 'soap'", Null(),
        "True", Null()
    ),

image HPAP HEAD:
    "images/Sprite/hpap/hpap head_mg.webp",
    zoom 1.5/hpap_size
    xoffset int((hpap_size - 1.50) * 250)
    yoffset int((hpap_size - 1.50) * 900)

image HPAP PARTS = Composite(
    (720,1080),
    (0,0), "images/Sprite/hpap/hpap body 0.webp",
    (0,0), "HPAP HEAD",
    (0,0), "HPAP WEAR",
    )

image HPAP STYLE = Composite(
    (720,1080),
    (0,0), "images/Sprite/hpap/hpap body 0.webp",
    (0,0), "HPAP HEAD",
    (0,0), ConditionSwitch(
        "len(WChar.gvar('hpap', 'achiev_wear')) > 0 and WChar.avar('hpap', 'achiev_wear', get_wear_var('hpap')) == 'home'", "images/Sprite/hpap/hpap body_wear home.webp",
        "len(WChar.gvar('hpap', 'achiev_wear')) > 0 and WChar.avar('hpap', 'achiev_wear', get_wear_var('hpap')) == 'under'", "images/Sprite/hpap/hpap body_wear under.webp",
        "len(WChar.gvar('hpap', 'achiev_wear')) > 0 and WChar.avar('hpap', 'achiev_wear', get_wear_var('hpap')) == 'sleep'", "images/Sprite/hpap/hpap body_wear sleep.webp",
        "len(WChar.gvar('hpap', 'achiev_wear')) > 0 and WChar.avar('hpap', 'achiev_wear', get_wear_var('hpap')) == 'casual'", "images/Sprite/hpap/hpap body_wear casual.webp",
        "len(WChar.gvar('hpap', 'achiev_wear')) > 0 and WChar.avar('hpap', 'achiev_wear', get_wear_var('hpap')) == 'school'", "images/Sprite/hpap/hpap body_wear school.webp",
        "len(WChar.gvar('hpap', 'achiev_wear')) > 0 and WChar.avar('hpap', 'achiev_wear', get_wear_var('hpap')) == 'school_swim'", "images/Sprite/hpap/hpap body_wear school_swim.webp",
        "len(WChar.gvar('hpap', 'achiev_wear')) > 0 and WChar.avar('hpap', 'achiev_wear', get_wear_var('hpap')) == 'school_sport'", "images/Sprite/hpap/hpap body_wear school_sport.webp",
        "len(WChar.gvar('hpap', 'achiev_wear')) > 0 and WChar.avar('hpap', 'achiev_wear', get_wear_var('hpap')) == 'soap'", "images/Sprite/hpap/hpap body_wear soap.webp",
        "True", Null()
    ),
    )

image HPAP:
    "HPAP PARTS"
    yalign 1.0
    ypos 1400
    zoom 0+(0.25+(1*hpap_size))*(0.25+(1*hpap_size))/2.5