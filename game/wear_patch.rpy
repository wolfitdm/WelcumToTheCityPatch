label popup(message):
    # This label receives the arguments
    window show
    "Popup received: [message]"

default Cur_Wear = {}
default Char_Data = {}
default a_menu_1 = ""
default a_menu_8 = 0

default wolfitdm_hero_name = "hero"

init -1000000 python:
    wear_all_chars_init = False

    def init_char_data_achiev(i):
        if not hasattr(store, "Char_Data"):
           setattr(store, "Char_Data", {})

        if not i in Char_Data:
           Char_Data[i] = {}

        if not "achiev" in Char_Data[i]:
           Char_Data[i]['achiev'] = {}

        if not "wear" in Char_Data[i]['achiev']:
           Char_Data[i]['achiev']['wear'] = []

    def wear_get_chars():
        wear_hero_chars = ["hero", "wmom", "wsis", "wnei", "wpre", "wota", "wdis", "wgal", "wric", "wgot", "wdel", "wuza", "wlaz", "hprv", "hine", "hriv", "wcou", "wgma", "wsuk", "wdan", "wkuu", "wrin"]
        # wear_hero_chars.extend(["wemo","wido","wtec","wnem","wahu","hbul","hfem","whip","wfat","hbla","hfre","wtpe"])

        wear_hero_chars.extend(["wmam", "hpap"])

        global wear_all_chars_init

        if not wear_all_chars_init:
           for i in wear_hero_chars:
               init_char_data_achiev(i)

           wear_all_chars_init = True

        return wear_hero_chars

    def wear_get_old_attrs_cheat():
        wear_char_attrs = ["int", "cha", "phy", "ene", "hyg", "eat", "lust", "love", "money", "inti", "bonus"]
        return wear_char_attrs

    def wear_get_char_attrs():
        wear_char_attrs = ["size", "body", "itemL", "itemR", "dressed", "wear", "mood", "fx", "map", "quest", "act", "know", "item", "item_love", "prey", "achiev_wear"]
        return wear_char_attrs

    def wear_get_char_attrs_cheat_int():
        wear_char_attrs = ["sex", "purity", "diligence"]
        return wear_char_attrs

    def wear_get_char_attrs_cheat_str():
        wear_char_attrs = ["gaming"]
        return wear_char_attrs

    def wear_get_char_attrs_all():
        wear_char_attrs = wear_get_old_attrs_cheat()
        wear_char_attrs.extend(wear_get_char_attrs())
        wear_char_attrs.extend(wear_get_char_attrs_cheat_int())
        wear_char_attrs.extend(wear_get_char_attrs_cheat_str())

        return wear_char_attrs

    def wear_get_quests():
        wear_all_hero_quests = ["A New Journey", "Forgiveness"]

        return wear_all_hero_quests

    def wear_get_styles():
        wear_get_styles_ = ["common", "gracious"]
        return wear_get_styles_

    def wear_get_styles_dict():
        wear_get_styles_ = {}

        wear_get_styles_["None"] = 0
        wear_get_styles_["none"] = 0
        wear_get_styles_["common"] = 0
        wear_get_styles_["gracious"] = 1

        return wear_get_styles_

    class Wolfitdm_Transformer:
       def __init__(self):
           if not hasattr(store, "Char_Data"):
              setattr(store, "Char_Data", {})

           self.contains_point_in_version = False

           if "." in config.version:
              self.version_splitted = config.version.split(".")
              self.contains_point_in_version = True
           else:
              self.version_splitted = [config.version]

           self.version_splitted_int = []

           if self.contains_point_in_version:
              for i in self.version_splitted:
                 self.version_splitted_int.append(self.get_int(i))

           self.is_really_old_version = False

           if len(self.version_splitted_int) >= 2:
              if self.version_splitted_int[0] == 0 and self.version_splitted_int[1] < 36: 
                 self.is_really_old_version = True
              elif self.version_splitted_int[0] == 0 and self.version_splitted_int[1] == 36 and len(self.version_splitted_int) == 3:
                 if self.version_splitted_int[2] == 1:
                    self.is_really_old_version = True   

           self.is_old_version = config.version == "0.36.1" or self.is_really_old_version
           self.setup_vars_all()

       def get_int(self, i):
           try:
              num = int(i)
           except:
              num = 0
           return num

       def get_is_old_version(self):
           return self.is_old_version

       def get_old_version(self):
           return self.is_old_version

       def get_name(self, hero):
           fname = "UNKNOWN"
           lname = "UNKNOWN"

           fnameattr = "fname" + str(hero)
           lnameattr = "lname" + str(hero)

           if hasattr(store, fnameattr):
              fname = str(getattr(store, fnameattr))

           if hero in ["wsis", "wmom"]:
              if hasattr(store, "lnamestep"):
                 lname = str(getattr(store, "lnamestep"))
           elif hero in ["wcou", "wgma", "waun"]:
              if hasattr(store, "lnamerela"):
                 lname = str(getattr(store, "lnamerela"))
           elif hero in ["wmam", "hpap"]:
              if hasattr(store, "lnamewnei"):
                 lname = str(getattr(store, "lnamewnei")) 
           elif hasattr(store, lnameattr):
              lname = str(getattr(store, lnameattr))

           return (fname, lname)

       def get_first_name(self, hero):
           fname, lname = self.get_name(hero)
           return fname

       def get_last_name(self, hero):
           fname, lname = self.get_name(hero)
           return lname

       def setup_quests(self, hero, varv):
           if not "quest" in Char_Data[hero]:
              Char_Data[hero]["quest"] = {}

           if hero == "hero":
              if not "A New Journey" in Char_Data[hero]["quest"]:
                 Char_Data[hero]["quest"]["A New Journey"] = 0

           return  

       def update_quest_attr(self, hero, varv):
           if hero == "hero":
              if varv == "A New Journey":
                 setattr("hero_quest_3", Char_Data[hero]["quest"]["A New Journey"])
           elif hero == "wsis":
              if varv == "Forgiveness":
                 setattr(store, "wsis_quest_2", Char_Data[hero]["quest"]["Forgiveness"])

       def update_quest_char(self, hero, varv):
           if hero == "hero":
              if varv == "A New Journey":
                 if hasattr(store, "hero_quest_3"):
                    Char_Data[hero]["quest"]["A New Journey"] = getattr(store, "hero_quest_3")
           elif hero == "wsis":
              if varv == "Forgiveness":
                 if hasattr(store, "wsis_quest_2"):
                    Char_Data[hero]["quest"]["Forgiveness"] = getattr(store, "wsis_quest_2")


       def get_quest_attr(self, hero, varv):
           if hero == "hero":
              if varv == "A New Journey":
                 if hasattr(store, "hero_quest_3"):
                    return getattr(store, "hero_quest_3")
           elif hero == "wsis":
              if varv == "Forgiveness":
                 if hasattr(store, "wsis_quest_2"):
                    return getattr(store, "wsis_quest_2")

           return None

       def get_quest_char(self, hero, varv):
           if hero == "hero":
              if varv == "A New Journey":
                 return Char_Data[hero]["quest"]["A New Journey"]
           elif hero == "wsis":
              if varv == "Forgiveness":
                 return Char_Data[hero]["quest"]["Forgiveness"]

           return None

       def set_quest_attr(self, hero, varv, varvv):
           if hero == "hero":
              if varv == "A New Journey":
                 if hasattr(store, "hero_quest_3"):
                    setattr(store, "hero_quest_3", varvv)
           elif hero == "wsis":
              if varv == "Forgiveness":
                 if hasattr(store, "wsis_quest_2"):
                    setattr(store, "wsis_quest_2", varvv)

       def set_quest_char(self, hero, varv, varvv):
           if hero == "hero":
              if varv == "A New Journey":
                 Char_Data[hero]["quest"]["A New Journey"] = varvv
           elif hero == "wsis":
              if varv == "Forgiveness":
                 Char_Data[hero]["quest"]["Forgiveness"] = varvv

           return None

       def setup_vars(self, hero, varv):
           if not hero in Char_Data:
              Char_Data[hero] = {}

           if not "style" in Char_Data[hero]:
              Char_Data[hero]["style"] = 0

           if not "stat" in Char_Data:
              Char_Data[hero]["stat"] = {}

           for i in wear_get_old_attrs_cheat():
              if not i in Char_Data[hero]["stat"]:
                 Char_Data[hero]["stat"][i] = 0

           if not "know" in Char_Data:
              Char_Data[hero]["know"] = []

           self.setup_quests(hero, varv)

           if varv in wear_get_old_attrs_cheat():
              if not varv in Char_Data[hero]["stat"]:
                 Char_Data[hero]["stat"][varv] = 0

           elif varv == "itemR" or varv == "itemL":
              if not "item" in Char_Data[hero]:
                 Char_Data[hero]["item"] = {}  

              if not "hold_left" in Char_Data[hero]["item"]:
                 Char_Data[hero]["item"]["hold_left"] = 0
             
              if not "hold_right" in Char_Data[hero]["item"]:
                 Char_Data[hero]["item"]["hold_right"] = 0

           elif varv == "achiev_wear":
              if not "achiev" in Char_Data[hero]:
                 Char_Data[hero]["achiev"] = {}

              if not "wear" in Char_Data[hero]["achiev"]:
                 Char_Data[hero]["achiev"]["wear"] = ""

           else:
              if varv not in Char_Data[hero]:
                 getvarv = None

                 if varv == "wear":
                    getvarv = ""

                 Char_Data[hero][varv] = getvarv

       def update_vars_specific(self, hero, varv):
           self.setup_vars(hero,varv)
           if self.is_old_version:

              if varv == "style":
                 setattr(store, hero + "_" + varv, Char_Data[hero]["style"])

              elif varv == "know":
                 setattr(store, hero + "_" + varv, Char_Data[hero]["know"])

              elif varv == "itemR":
                 setattr(store, hero + "_" + varv, Char_Data[hero]["item"]["hold_right"])

              elif varv == "itemL":
                 setattr(store, hero + "_" + varv, Char_Data[hero]["item"]["hold_left"])

              elif varv == "achiev_wear":
                 setattr(store, hero + "_" + varv, Char_Data[hero]["achiev"]["wear"])

              elif varv in wear_get_quests():
                 self.update_quest_attr(hero, varv)

              elif varv in wear_get_old_attrs_cheat():
                 setattr(store, hero + "_" + varv, Char_Data[hero]["stat"][varv])

              elif varv in Char_Data[hero]:
                 setattr(store, hero + "_" + varv, Char_Data[hero][varv])
           else:
              getvarv = None

              if varv in wear_get_quests():
                 self.update_quest_char(hero, varv)

              elif hasattr(store, hero + "_" + varv):
                 getvarv = getattr(store, hero + "_" + varv)

                 if varv == "style":
                    Char_Data[hero]["style"] = getvarv
                 elif varv == "know":
                    Char_Data[hero]["know"] = getvarv
                 elif varv == "itemR":
                    Char_Data[hero]["item"]["hold_right"] = getvarv
                 elif varv == "itemL":
                    Char_Data[hero]["item"]["hold_left"] = getvarv
                 elif varv == "achiev_wear":
                    Char_Data[hero]["achiev"]["wear"] = getvarv
                 elif varv in wear_get_old_attrs_cheat():
                    Char_Data[hero]["stat"][varv] = getvarv
                 elif varv in Char_Data[hero]:
                    Char_Data[hero][varv] = getvarv

       def update_vars(self):
          for i in wear_get_chars():
              for j in wear_get_char_attrs_all():
                  self.update_vars_specific(i,j)

       def setup_vars_all(self):
          for i in wear_get_chars():
              for j in wear_get_char_attrs_all():
                  self.setup_vars(i, j)

       def gvar(self, hero, varv):
           if self.is_old_version:

              if varv == "style":
                 return Char_Data[hero]["style"]

              elif varv == "know":
                 return Char_Data[hero]["know"]

              elif varv == "itemR":
                 return Char_Data[hero]["item"]["hold_right"]

              elif varv == "itemL":
                 return Char_Data[hero]["item"]["hold_left"]

              elif varv == "achiev_wear":
                 return Char_Data[hero]["achiev"]["wear"]

              elif varv in wear_get_quests():
                 return self.get_quest_char(hero, varv)

              elif varv in wear_get_old_attrs_cheat():
                 return Char_Data[hero]["stat"][varv]

              elif varv in Char_Data[hero]:
                 return Char_Data[hero][varv]

              else:
                 return None

           else:
              getvarv = None

              if varv in wear_get_quests():
                 getvarv = self.get_quest_attr(hero, varv)

              elif hasattr(store, hero + "_" + varv):
                 getvarv = getattr(store, hero + "_" + varv)

              return getvarv  

       def avar(self, hero, varv, index):
           val = self.gvar(hero, varv)

           if not val == None:
              if isinstance(val, list):
                 if index < len(val):
                    return val[index]

           return ""

       def svar(self, hero, varv, varvv):
           if self.is_old_version:

              if varv == "style":
                 Char_Data[hero]["style"] = varvv

              elif varv == "know":
                 Char_Data[hero]["know"] = varvv

              elif varv == "itemR":
                 Char_Data[hero]["item"]["hold_right"] = varvv

              elif varv == "itemL":
                 Char_Data[hero]["item"]["hold_left"] = varvv

              elif varv == "achiev_wear":
                 Char_Data[hero]["achiev"]["wear"] = varvv

              elif varv in wear_get_quests():
                 self.set_quest_char(hero, varv, varvv)

              elif varv in wear_get_old_attrs_cheat():
                 Char_Data[hero]["stat"][varv] = varvv

              elif varv in Char_Data[hero]:
                 Char_Data[hero][varv] = varvv

           else:
              if varv in wear_get_quests():
                 self.set_quest_attr(hero, varv, varvv)
              else:
                 setattr(store, hero + "_" + varv, varvv)

       def inc_var(self, hero, varv, step=1):
           inc_val = self.gvar(hero, varv)

           if inc_val is None:
              return

           if self.is_int(inc_val):
              inc_val = int(inc_val)
           elif self.is_float(inc_val):
              inc_val = float(inc_val)
           else:
              return

           inc_val += step

           self.svar(hero, varv, inc_val)

       def dec_var(self, hero, varv, step=1):
           inc_val = self.gvar(hero, varv)

           if inc_val is None:
              return

           if self.is_int(inc_val):
              inc_val = int(inc_val)
           elif self.is_float(inc_val):
              inc_val = float(inc_val)
           else:
              return

           inc_val -= step

           self.svar(hero, varv, inc_val)

       def is_float(self, num):
           try:
               float(num)
               return True
           except:
               return False

       def is_int(self, num):
           try:
               int(num)
               return True
           except:
               return False

       def inc_or_dec_var_style(self, hero, inc=True, set_string=True):
           current_style = self.gvar(hero, "style")

           if current_style is None:
              self.svar(hero, "style", 0)
              return

           inc_val = current_style

           cur_styles = wear_get_styles()
           cur_styles_ = wear_get_styles_dict()

           current_style_index = -1

           is_inc_or_dec = False

           if self.is_int(inc_val) or self.is_float(inc_val):
              is_inc_or_dec = True

              if inc:
                 self.inc_var(hero, "style", 1)
              else:
                 self.dec_var(hero, "style", 1)

              current_style = self.get_int(self.gvar(hero, "style"))
              for index, value in enumerate(cur_styles):
                  if index == current_style:
                     current_style_index = index
                     break

              if current_style_index == -1:
                 current_style_index = 0

           else:
              current_style = str(current_style)
              
              for index, value in enumerate(cur_styles):
                  if value == current_style:
                     current_style_index = index
                     break

              if current_style_index == -1:
                 if current_style in cur_styles_:
                    current_style_index = cur_styles_[current_style]
                 else:
                    current_style_index = 0

           if inc:

              if not is_inc_or_dec:
                 current_style_index += 1

           else:

              if not is_inc_or_dec:
                 current_style_index -= 1

           if current_style_index  >= len(cur_styles):
              current_style_index = 0

           if current_style_index <= 0:
              current_style_index = 0

           if set_string:
              current_style = cur_styles[current_style_index]
           else:
              current_style = current_style_index
              
           WChar.svar(hero, "style", current_style)

       def nvar(self, hero, varv):
           if self.is_old_version:

              if not hero in Char_Data:
                 Char_Data[hero] = {}

              if not varv in Char_Data[hero]:
                 Char_Data[hero][varv] = None

           else:
              if not hasattr(store, hero + "_" + varv):
                 setattr(store, hero + "_" + varv, None)  

       def gnvar(self, hero, varv):
           self.nvar(hero, varv)
           
           if self.is_old_version:
              return Char_Data[hero][varv]
           else:
              return getattr(store, hero + "_" + varv)

       def snvar(self, hero, varv, varvv):
           self.nvar(hero, varv)
           
           if self.is_old_version:
              Char_Data[hero][varv] = varvv
           else:
              setattr(store, hero + "_" + varv, varvv)

       def dnvar(self, hero, varv):
           self.snvar(hero, varv, None)

       def dvar(self, hero, varv):
           self.svar(hero, varv, None)

       def remove_caps(self, hero, stat, val=100):
           varattr = hero + "_" + stat + "_cap"
           if hasattr(store, varattr):
              varval = getattr(store, varattr)
              if isinstance(varval, (int, float)):
                 if varval <= val:
                    setattr(store, varattr, val)
                    msg.msg("remove_caps " + hero)


            varattr = "char_" + stat + "_cap"
            if hasattr(store, varattr):
               varval = getattr(store, varattr)
               if isinstance(varval, (int, float)):
                  if varval <= val:
                     setattr(store, varattr, val)
                     msg.msg("remove_caps char " + hero)

       def inc_cheat_vars(self, hero, val, val_money):
           if self.is_old_version:
              if not "stat" in Char_Data[hero]:
                 Char_Data[hero]["stat"] = {}

              for i in wear_get_old_attrs_cheat():
                  self.remove_caps(hero, i)
                  if not i in Char_Data[hero]["stat"]:
                     Char_Data[hero]["stat"][i] = 0
                  inc_val = val_money if i == "money" else val
                  Char_Data[hero]["stat"][i] += inc_val
           else:
              for i in wear_get_old_attrs_cheat():
                  self.remove_caps(hero, i)
                  inc_val = val_money if i == "money" else val
                  gstr = hero + "_" + i
                  if hasattr(store, gstr):
                     valv = getattr(store, gstr)
                     valv += inc_val
                     setattr(store, gstr, valv)

              for i in wear_get_char_attrs_cheat_int():
                  self.remove_caps(hero, i)
                  gstr = hero + "_" + i
                  if hasattr(store, gstr):
                     valv = getattr(store, gstr)
                     if i == "purity":
                        valv = 0
                     else:
                        valv += val
                     setattr(store, gstr, valv)

    WChar = Wolfitdm_Transformer()

    def wear_test_head(part, name):
        test_string = "kawaii_" + name
        image = "kawaii/head/" + name + "/kawaii_head_" + part + "_" + name + ".png"
        return WChar.gvar("hero", "wear") == test_string and wear_is_image(image)

    def wear_is_image(path):
        try:
            width, height = renpy.image_size(filename)
            return (width == 1 and height == 1) == False
        except Exception as e:
            renpy.log(f"Error getting size for {filename}: {e}")
            return False

    def wear_get_clothes():
        return ["home", "under", "sleep", "casual", "dressy", "formal", "sport", "swim", "school", "school_swim", "school_sport", "work", "soap", "nude", "work2"]

    def wear_kawaii_get_clothes():
        kawaii_clothes = []

        for i in wear_get_clothes():
            kawaii_clothes.append("kawaii_" + i)

        return kawaii_clothes

    def my_renpy_say(text):
        renpy.call_in_new_context("popup", text)

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
        is_old_version = WChar.get_is_old_version()

        for i in wear_get_chars():

            if is_old_version:
               init_char_data_wear(i)
               init_char_data_achiev(i)

            init_cur_wear(i)

            if not Cur_Wear[i]["wear_string"] == None:
               WChar.svar(i, "wear", Cur_Wear[i]["wear_string"])
               #my_renpy_say("Current wear: " + i + ":" + Char_Data[i]['wear'])   

    def set_wear_var(i, var):
        init_cur_wear(i)

        if WChar.get_is_old_version():
           init_char_data_wear(i)
           init_char_data_achiev(i)

        achiev_wear = WChar.gvar(i, "achiev_wear")

        len_achiev_var = len(achiev_wear) if isinstance(achiev_wear, list) else 0

        if var < len_achiev_var:
           Cur_Wear[i]["wear_string"] = achiev_wear[var]
           if i == "hero" and not Cur_Wear[i]["wear_string"].startswith("kawaii"):
              if not wolfitdm_hero_name == i:
                 set_wear_var(wolfitdm_hero_name, var)
           WChar.svar(i, "wear", Cur_Wear[i]["wear_string"])
           #my_renpy_say("Current wear: " + i + ":" + Cur_Wear[i]["wear_string"])

        Cur_Wear[i]["wear"] = var

    def get_wear_var(i):
        init_cur_wear(i)

        if WChar.get_is_old_version():
           init_char_data_wear(i)
           init_char_data_achiev(i)

        var = Cur_Wear[i]["wear"]

        achiev_wear = WChar.gvar(i, "achiev_wear")

        len_achiev_var = len(achiev_wear) if isinstance(achiev_wear, list) else 0

        if var < len_achiev_var:
           Cur_Wear[i]["wear_string"] = achiev_wear[var]
           WChar.svar(i, "wear", Cur_Wear[i]["wear_string"])          
           #my_renpy_say("Current wear: " + i + ":" + Cur_Wear[i]["wear_string"])   

        return var