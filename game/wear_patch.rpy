label popup(message):
    # This label receives the arguments
    window show
    "Popup received: [message]"

default Cur_Wear = {}
default Char_Data = {}
default a_menu_1 = ""
default a_menu_8 = 0

default wolfitdm_hero_name = "hero"

init -1000 python:
    def wear_test_head(part, name):
        test_string = "kawaii_" + name
        image = "kawaii/head/" + name + "/kawaii_head_" + part + "_" + name + ".png"
        return Char_Data['hero']['wear'] == test_string and wear_is_image(image)

    def wear_is_image(path):
        try:
            width, height = renpy.image_size(filename)
            return (width == 1 and height == 1) == False
        except Exception as e:
            renpy.log(f"Error getting size for {filename}: {e}")
            return False

    def my_renpy_say(text):
        renpy.call_in_new_context("popup", text)

    def init_char_data_achiev(i):
        if not i in Char_Data:
           Char_Data[i] = {}

        if not "achiev" in Char_Data[i]:
           Char_Data[i]['achiev'] = {}

        if not "wear" in Char_Data[i]['achiev']:
           Char_Data[i]['achiev']['wear'] = []

    def init_char_data_wear(i):
        if not i in Char_Data:
           Char_Data[i] = {}

        if not "wear" in Char_Data[i]:
           Char_Data[i]['wear'] = ""

    def init_cur_wear(i):
        if not i in Cur_Wear:
           Cur_Wear[i] = {}

        if not "wear" in Cur_Wear[i]:
           Cur_Wear[i]["wear"] = 0

        if not "wear_string" in Cur_Wear[i]:
           Cur_Wear[i]["wear_string"] = None

    def update_wear_vars():
        for i in ["hero", "hriv", "hprv", "hine", "wsis", "wnei", "wmom", "wgma", "wcou", "wpre", "wgal", "wota", "wdis", "wric", "wuza", "wlaz", "wdel", "wgot", "wdan", "wkuu", "wrin", "wsuk"]:
            init_cur_wear(i)
            init_char_data_wear(i)
            if not Cur_Wear[i]["wear_string"] == None:
               Char_Data[i]['wear'] = Cur_Wear[i]["wear_string"]
               #my_renpy_say("Current wear: " + i + ":" + Char_Data[i]['wear'])   

    def set_wear_var(i, var):
        init_cur_wear(i)
        init_char_data_wear(i)
        init_char_data_achiev(i)

        if var < len(Char_Data[i]['achiev']['wear']):
           Cur_Wear[i]["wear_string"] = Char_Data[i]['achiev']['wear'][var]
           if i == "hero" and not Cur_Wear[i]["wear_string"].startswith("kawaii"):
              if not wolfitdm_hero_name == i:
                 set_wear_var(wolfitdm_hero_name, var)
           Char_Data[i]['wear'] = Cur_Wear[i]["wear_string"]
           #my_renpy_say("Current wear: " + i + ":" + Cur_Wear[i]["wear_string"])

        Cur_Wear[i]["wear"] = var

    def get_wear_var(i):
        init_cur_wear(i)
        init_char_data_wear(i)
        init_char_data_achiev(i)

        var = Cur_Wear[i]["wear"]

        if var < len(Char_Data[i]['achiev']['wear']):
           Cur_Wear[i]["wear_string"] = Char_Data[i]['achiev']['wear'][var]
           Char_Data[i]['wear'] = Cur_Wear[i]["wear_string"]           
           #my_renpy_say("Current wear: " + i + ":" + Cur_Wear[i]["wear_string"])   

        return var