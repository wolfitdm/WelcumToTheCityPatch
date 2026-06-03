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

    def wear_get_quests(hero):
        wear_all_hero_quests = {}
        wear_all_hero_quests["hero"] = ["Day 1: Memories", "Day 2: City Life", "A New Journey"]
        wear_all_hero_quests["wsis"] = ["Memories I", "Forgiveness", "Memories II", "Late Night Snack", "Sleep Together", "Girl's Sleepover", "Movie_Action", "Movie_Romance", "Movie_Horror"]
        wear_all_hero_quests["wnei"] = ["Cartoons Aint Borin'", "Appropriate Goodbye", "Copy & Paste DNA", "Parents Care", "Watch TV Together", "Neighbors Reunion"]
        wear_all_hero_quests["wcou"] = ["A Drive Around The City"]
        wear_all_hero_quests["wpre"] = ["Body Formula"]
        wear_all_hero_quests["wric"] = ["School Princess"]
        wear_all_hero_quests["wgal"] = ["Hard To Deal"]
        wear_all_hero_quests["wdis"] = ["Weird Girl"]
        wear_all_hero_quests["wota"] = ["Vivid Imagination Problems"]
        wear_all_hero_quests["wdel"] = ["School Is A Prison, Let's Rebel!"]
        wear_all_hero_quests["wgot"] = ["Lady of Death"]
        wear_all_hero_quests["wlaz"] = ["Video Game > Sports"]
        wear_all_hero_quests["wuza"] = ["THERE'S NO SUCH THING AS A BAD DAY!"]
        wear_all_hero_quests["hprv"] = ["Technical Analysis of Female Anatomy and Underwears"]
        wear_all_hero_quests["hine"] = ["Clubs Start"]
        wear_all_hero_quests["wdan"] = ["Meeting"]
        wear_all_hero_quests["wnem"] = ["Meeting"]
        wear_all_hero_quests["wahu"] = ["Meeting"]
        wear_all_hero_quests["wkuu"] = ["Meeting"]
        wear_all_hero_quests["wido"] = ["Meeting"]
        wear_all_hero_quests["wemo"] = ["Meeting"]
        wear_all_hero_quests["hriv"] = ["Meeting"]
        wear_all_hero_quests["hbul"] = ["Meeting"]
        wear_all_hero_quests["hfem"] = ["Meeting"]
        wear_all_hero_quests["wtec"] = ["Meeting"]
        wear_all_hero_quests["wrin"] = ["Meeting"]
        wear_all_hero_quests["wsuk"] = ["Meeting", "Trigger Enable"]
        wear_all_hero_quests["wtpe"] = ["Meeting"]

        if hero in wear_all_hero_quests:
           return wear_all_hero_quests[hero]
        else:
           return []

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
              self.version_splitted = self.get_version().split(".")
              self.contains_point_in_version = True
           else:
              self.version_splitted = [self.get_version()]

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

           self.is_old_version = self.get_version() == "0.36.1" or self.is_really_old_version
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

       def get_version(self):
           if hasattr(config, "version"):
              return getattr(config, "version")

           return "0.40.0"

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

       def setup_quests(self, hero):
           if not "quest" in Char_Data[hero]:
              Char_Data[hero]["quest"] = {}

           if hero == "hero":
              if not "A New Journey" in Char_Data[hero]["quest"]:
                 Char_Data[hero]["quest"]["A New Journey"] = 0

              if not "Day 1: Memories" in Char_Data[hero]["quest"]:
                 Char_Data[hero]["quest"]["Day 1: Memories"] = 0

              if not "Day 2: City Life" in Char_Data[hero]["quest"]:
                 Char_Data[hero]["quest"]["Day 2: City Life"] = 0

           if hero == "wmom":
              if not "Morning Routine" in Char_Data[hero]["quest"]:
                 Char_Data[hero]["quest"]["Morning Routine"] = 0

              if not "Cooking Together" in Char_Data[hero]["quest"]:
                 Char_Data[hero]["quest"]["Cooking Together"] = 0

              if not "Family Dinner" in Char_Data[hero]["quest"]:
                 Char_Data[hero]["quest"]["Family Dinner"] = 0

              if not "Late Night Talk" in Char_Data[hero]["quest"]:
                 Char_Data[hero]["quest"]["Late Night Talk"] = 0

           if hero == "wsis":
              if not "Memories I" in Char_Data[hero]["quest"]:
                 Char_Data[hero]["quest"]["Memories I"] = 0

              if not "Forgiveness" in Char_Data[hero]["quest"]:
                 Char_Data[hero]["quest"]["Forgiveness"] = 0

              if not "Memories II" in Char_Data[hero]["quest"]:
                 Char_Data[hero]["quest"]["Memories II"] = 0

              if not "Late Night Snack" in Char_Data[hero]["quest"]:
                 Char_Data[hero]["quest"]["Late Night Snack"] = 0

              if not "Sleep Together" in Char_Data[hero]["quest"]:
                 Char_Data[hero]["quest"]["Sleep Together"] = 0

              if not "Girl's Sleepover" in Char_Data[hero]["quest"]:
                 Char_Data[hero]["quest"]["Girl's Sleepover"] = 0

              if not "Movie_Action" in Char_Data[hero]["quest"]:
                 Char_Data[hero]["quest"]["Movie_Action"] = 0

              if not "Movie_Romance" in Char_Data[hero]["quest"]:
                 Char_Data[hero]["quest"]["Movie_Romance"] = 0

              if not "Movie_Horror" in Char_Data[hero]["quest"]:
                 Char_Data[hero]["quest"]["Movie_Horror"] = 0

           if hero == "wnei":
              if not "Cartoons Aint Borin'" in Char_Data[hero]["quest"]:
                 Char_Data[hero]["quest"]["Cartoons Aint Borin'"] = 0

              if not "Appropriate Goodbye" in Char_Data[hero]["quest"]:
                 Char_Data[hero]["quest"]["Appropriate Goodbye"] = 0

              if not "Copy & Paste DNA" in Char_Data[hero]["quest"]:
                 Char_Data[hero]["quest"]["Copy & Paste DNA"] = 0

              if not "Parents Care" in Char_Data[hero]["quest"]:
                 Char_Data[hero]["quest"]["Parents Care"] = 0

              if not "Watch TV Together" in Char_Data[hero]["quest"]:
                 Char_Data[hero]["quest"]["Watch TV Together"] = 0

              if not "Neighbors Reunion" in Char_Data[hero]["quest"]:
                 Char_Data[hero]["quest"]["Neighbors Reunion"] = 0

           if hero == "wcou":
              if not "A Drive Around The City" in Char_Data[hero]["quest"]:
                 Char_Data[hero]["quest"]["A Drive Around The City"] = 0

           if hero == "wpre":
              if not "Body Formula" in Char_Data[hero]["quest"]:
                 Char_Data[hero]["quest"]["Body Formula"] = 0

           if hero == "wric":
              if not "School Princess" in Char_Data[hero]["quest"]:
                 Char_Data[hero]["quest"]["School Princess"] = 0

           if hero == "wgal":
              if not "Hard To Deal" in Char_Data[hero]["quest"]:
                 Char_Data[hero]["quest"]["Hard To Deal"] = 0

           if hero == "wdis":
              if not "Weird Girl" in Char_Data[hero]["quest"]:
                 Char_Data[hero]["quest"]["Weird Girl"] = 0

           if hero == "wota":
              if not "Vivid Imagination Problems" in Char_Data[hero]["quest"]:
                 Char_Data[hero]["quest"]["Vivid Imagination Problems"] = 0

           if hero == "wdel":
              if not "School Is A Prison, Let's Rebel!" in Char_Data[hero]["quest"]:
                 Char_Data[hero]["quest"]["School Is A Prison, Let's Rebel!"] = 0

           if hero == "wgot":
              if not "Lady of Death" in Char_Data[hero]["quest"]:
                 Char_Data[hero]["quest"]["Lady of Death"] = 0

           if hero == "wlaz":
              if not "Video Game > Sports" in Char_Data[hero]["quest"]:
                 Char_Data[hero]["quest"]["Video Game > Sports"] = 0

           if hero == "wuza":
              if not "THERE'S NO SUCH THING AS A BAD DAY!" in Char_Data[hero]["quest"]:
                 Char_Data[hero]["quest"]["THERE'S NO SUCH THING AS A BAD DAY!"] = 0

           if hero == "hprv":
              if not "Technical Analysis of Female Anatomy and Underwears" in Char_Data[hero]["quest"]:
                 Char_Data[hero]["quest"]["Technical Analysis of Female Anatomy and Underwears"] = 0

           if hero == "hine":
              if not "Clubs Start" in Char_Data[hero]["quest"]:
                 Char_Data[hero]["quest"]["Clubs Start"] = 0

           if hero in ["wdan", "wnem", "wahu", "wkuu", "wido", "wemo", "hriv", "hbul", "hfem", "wtec", "wrin", "wsuk", "wtpe"]:
              if not "Meeting" in Char_Data[hero]["quest"]:
                 Char_Data[hero]["quest"]["Meeting"] = 0

           if hero == "wsuk":
              if not "Trigger Enable" in Char_Data[hero]["quest"]:
                 Char_Data[hero]["quest"]["Trigger Enable"] = 0 

           return                                                        

       def update_quest_attr(self, hero, varv):
           if hero == "hero":
              if varv == "A New Journey":
                 setattr(store, "hero_quest_3", Char_Data[hero]["quest"]["A New Journey"])
              elif varv == "Day 1: Memories":
                 setattr(store, "hero_quest_1", Char_Data[hero]["quest"]["Day 1: Memories"])
              elif varv == "Day 2: City Life":
                 setattr(store, "hero_quest_2", Char_Data[hero]["quest"]["Day 2: City Life"])

           if hero == "wmom":
              if varv == "Morning Routine":
                 setattr(store, "wmom_quest_1", Char_Data[hero]["quest"]["Morning Routine"])
              elif varv == "Cooking Together":
                 setattr(store, "wmom_quest_2", Char_Data[hero]["quest"]["Cooking Together"])
              elif varv == "Family Dinner":
                 setattr(store, "wmom_quest_3", Char_Data[hero]["quest"]["Family Dinner"])
              elif varv == "Late Night Talk":
                 setattr(store, "wmom_quest_4", Char_Data[hero]["quest"]["Late Night Talk"])

           if hero == "wsis":
              if varv == "Memories I":
                 setattr(store, "wsis_quest_1", Char_Data[hero]["quest"]["Memories I"])
              elif varv == "Forgiveness":
                 setattr(store, "wsis_quest_2", Char_Data[hero]["quest"]["Forgiveness"])
              elif varv == "Memories II":
                 setattr(store, "wsis_quest_3", Char_Data[hero]["quest"]["Memories II"])
              elif varv == "Late Night Snack":
                 setattr(store, "wsis_quest_4", Char_Data[hero]["quest"]["Late Night Snack"])
              elif varv == "Sleep Together":
                 setattr(store, "wsis_quest_5", Char_Data[hero]["quest"]["Sleep Together"])
              elif varv == "Girl's Sleepover":
                 setattr(store, "wsis_quest_6", Char_Data[hero]["quest"]["Girl's Sleepover"])
              elif varv == "Movie_Action":
                 setattr(store, "wsis_quest_7", Char_Data[hero]["quest"]["Movie_Action"])
              elif varv == "Movie_Romance":
                 setattr(store, "wsis_quest_8", Char_Data[hero]["quest"]["Movie_Romance"])
              elif varv == "Movie_Horror":
                 setattr(store, "wsis_quest_9", Char_Data[hero]["quest"]["Movie_Horror"])

           if hero == "wnei":
              if varv == "Cartoons Aint Borin'":
                 setattr(store, "wnei_quest_1", Char_Data[hero]["quest"]["Cartoons Aint Borin'"])
              elif varv == "Appropriate Goodbye":
                 setattr(store, "wnei_quest_2", Char_Data[hero]["quest"]["Appropriate Goodbye"])
              elif varv == "Copy & Paste DNA":
                 setattr(store, "wnei_quest_3", Char_Data[hero]["quest"]["Copy & Paste DNA"])
              elif varv == "Parents Care":
                 setattr(store, "wnei_quest_4", Char_Data[hero]["quest"]["Parents Care"])
              elif varv == "Watch TV Together":
                 setattr(store, "wnei_quest_5", Char_Data[hero]["quest"]["Watch TV Together"])
              elif varv == "Neighbors Reunion":
                 setattr(store, "wnei_quest_6", Char_Data[hero]["quest"]["Neighbors Reunion"])

           if hero == "wcou":
              if varv == "A Drive Around The City":
                 setattr(store, "wcou_quest_1", Char_Data[hero]["quest"]["A Drive Around The City"])

           if hero == "wpre":
              if varv == "Body Formula":
                 setattr(store, "wpre_quest_1", Char_Data[hero]["quest"]["Body Formula"])           

           if hero == "wric":
              if varv == "School Princess":
                 setattr(store, "wric_quest_1", Char_Data[hero]["quest"]["School Princess"])    

           if hero == "wgal":
              if varv == "Hard To Deal":
                 setattr(store, "wgal_quest_1", Char_Data[hero]["quest"]["Hard To Deal"])  

           if hero == "wdis":
              if varv == "Weird Girl":
                 setattr(store, "wdis_quest_1", Char_Data[hero]["quest"]["Weird Girl"])  

           if hero == "wota":
              if varv == "Vivid Imagination Problems":
                 setattr(store, "wota_quest_1", Char_Data[hero]["quest"]["Vivid Imagination Problems"])  

           if hero == "wdel":
              if varv == "School Is A Prison, Let's Rebel!":
                 setattr(store, "wdel_quest_1", Char_Data[hero]["quest"]["School Is A Prison, Let's Rebel!"])  

           if hero == "wgot":
              if varv == "Lady of Death":
                 setattr(store, "wgot_quest_1", Char_Data[hero]["quest"]["Lady of Death"])  

           if hero == "wlaz":
              if varv == "Video Game > Sports":
                 setattr(store, "wlaz_quest_1", Char_Data[hero]["quest"]["Video Game > Sports"])  

           if hero == "wuza":
              if varv == "THERE'S NO SUCH THING AS A BAD DAY!":
                 setattr(store, "wuza_quest_1", Char_Data[hero]["quest"]["THERE'S NO SUCH THING AS A BAD DAY!"])  

           if hero == "hprv":
              if varv == "Technical Analysis of Female Anatomy and Underwears":
                 setattr(store, "hprv_quest_1", Char_Data[hero]["quest"]["Technical Analysis of Female Anatomy and Underwears"])  

           if hero == "hine":
              if varv == "Clubs Start":
                 setattr(store, "hine_quest_1", Char_Data[hero]["quest"]["Clubs Start"])

           if hero in ["wdan", "wnem", "wahu", "wkuu", "wido", "wemo", "hriv", "hbul", "hfem", "wtec", "wrin", "wsuk", "wtpe"]:
              if varv == "Meeting":
                 setattr(store, hero + "_quest_1", Char_Data[hero]["quest"]["Meeting"])  

           if hero == "wsuk":
              if varv == "Trigger Enable":
                 setattr(store, "wsuk_quest_2", Char_Data[hero]["quest"]["Trigger Enable"])  

       def update_quest_char(self, hero, varv):
           if hero == "hero":
              if varv == "A New Journey":
                 if hasattr(store, "hero_quest_3"):
                    Char_Data[hero]["quest"]["A New Journey"] = getattr(store, "hero_quest_3")
              elif varv == "Day 1: Memories":
                 if hasattr(store, "hero_quest_1"):
                    Char_Data[hero]["quest"]["Day 1: Memories"] = getattr(store, "hero_quest_1")
              elif varv == "Day 2: City Life":
                 if hasattr(store, "hero_quest_2"):
                    Char_Data[hero]["quest"]["Day 2: City Life"] = getattr(store, "hero_quest_2")

           if hero == "wmom":
              if varv == "Morning Routine":
                if hasattr(store, "wmom_quest_1"):
                   Char_Data[hero]["quest"]["Morning Routine"] = getattr(store, "wmom_quest_1")
              elif varv == "Cooking Together":
                if hasattr(store, "wmom_quest_2"):
                   Char_Data[hero]["quest"]["Cooking Together"] = getattr(store, "wmom_quest_2")
              elif varv == "Family Dinner":
                if hasattr(store, "wmom_quest_3"):
                   Char_Data[hero]["quest"]["Family Dinner"] = getattr(store, "wmom_quest_3")
              elif varv == "Late Night Talk":
                if hasattr(store, "wmom_quest_4"):
                   Char_Data[hero]["quest"]["Late Night Talk"] = getattr(store, "wmom_quest_4")
           
           if hero == "wsis":
              if varv == "Memories I":
                 if hasattr(store, "wsis_quest_1"):
                    Char_Data[hero]["quest"]["Memories I"] = getattr(store, "wsis_quest_1")
              elif varv == "Forgiveness":
                 if hasattr(store, "wsis_quest_2"):
                    Char_Data[hero]["quest"]["Forgiveness"] = getattr(store, "wsis_quest_2")
              elif varv == "Memories II":
                 if hasattr(store, "wsis_quest_3"):
                    Char_Data[hero]["quest"]["Memories II"] = getattr(store, "wsis_quest_3")
              elif varv == "Late Night Snack":
                 if hasattr(store, "wsis_quest_4"):
                    Char_Data[hero]["quest"]["Late Night Snack"] = getattr(store, "wsis_quest_4")
              elif varv == "Sleep Together":
                 if hasattr(store, "wsis_quest_5"):
                    Char_Data[hero]["quest"]["Sleep Together"] = getattr(store, "wsis_quest_5")
              elif varv == "Girl's Sleepover":
                 if hasattr(store, "wsis_quest_6"):
                    Char_Data[hero]["quest"]["Girl's Sleepover"] = getattr(store, "wsis_quest_6")
              elif varv == "Movie_Action":
                 if hasattr(store, "wsis_quest_7"):
                    Char_Data[hero]["quest"]["Movie_Action"] = getattr(store, "wsis_quest_7")
              elif varv == "Movie_Romance":
                 if hasattr(store, "wsis_quest_8"):
                    Char_Data[hero]["quest"]["Movie_Romance"] = getattr(store, "wsis_quest_8")
              elif varv == "Movie_Horror":
                 if hasattr(store, "wsis_quest_9"):
                    Char_Data[hero]["quest"]["Movie_Horror"] = getattr(store, "wsis_quest_9")

           if hero == "wnei":
              if varv == "Cartoons Aint Borin'":
                 if hasattr(store, "wnei_quest_1"):
                    Char_Data[hero]["quest"]["Cartoons Aint Borin'"] = getattr(store, "wnei_quest_1")
              elif varv == "Appropriate Goodbye":
                 if hasattr(store, "wnei_quest_2"):
                    Char_Data[hero]["quest"]["Appropriate Goodbye"] = getattr(store, "wnei_quest_2")
              elif varv == "Copy & Paste DNA":
                 if hasattr(store, "wnei_quest_3"):
                    Char_Data[hero]["quest"]["Copy & Paste DNA"] = getattr(store, "wnei_quest_3")
              elif varv == "Parents Care":
                 if hasattr(store, "wnei_quest_4"):
                    Char_Data[hero]["quest"]["Parents Care"] = getattr(store, "wnei_quest_4")
              elif varv == "Watch TV Together":
                 if hasattr(store, "wnei_quest_5"):
                    Char_Data[hero]["quest"]["Watch TV Together"] = getattr(store, "wnei_quest_5")
              elif varv == "Neighbors Reunion":
                 if hasattr(store, "wnei_quest_6"):
                    Char_Data[hero]["quest"]["Neighbors Reunion"] = getattr(store, "wnei_quest_6")

           if hero == "wcou":
              if varv == "A Drive Around The City":
                 if hasattr(store, "wcou_quest_1"):
                    Char_Data[hero]["quest"]["A Drive Around The City"] = getattr(store, "wcou_quest_1")

           if hero == "wpre":
              if varv == "Body Formula":
                 if hasattr(store, "wpre_quest_1"):
                    Char_Data[hero]["quest"]["Body Formula"] = getattr(store, "wpre_quest_1")         

           if hero == "wric":
              if varv == "School Princess":
                 if hasattr(store, "wric_quest_1"):
                    Char_Data[hero]["quest"]["School Princess"] = getattr(store, "wric_quest_1")            

           if hero == "wgal":
              if varv == "Hard To Deal":
                 if hasattr(store, "wgal_quest_1"):
                    Char_Data[hero]["quest"]["Hard To Deal"] = getattr(store, "wgal_quest_1")    

           if hero == "wdis":
              if varv == "Weird Girl":
                 if hasattr(store, "wdis_quest_1"):
                    Char_Data[hero]["quest"]["Weird Girl"] = getattr(store, "wdis_quest_1")

           if hero == "wota":
              if varv == "Vivid Imagination Problems":
                 if hasattr(store, "wota_quest_1"):
                    Char_Data[hero]["quest"]["Vivid Imagination Problems"] = getattr(store, "wota_quest_1")

           if hero == "wdel":
              if varv == "School Is A Prison, Let's Rebel!":
                 if hasattr(store, "wdel_quest_1"):
                    Char_Data[hero]["quest"]["School Is A Prison, Let's Rebel!"] = getattr(store, "wdel_quest_1") 

           if hero == "wgot":
              if varv == "Lady of Death":
                 if hasattr(store, "wgot_quest_1"):
                    Char_Data[hero]["quest"]["Lady of Death"] = getattr(store, "wgot_quest_1")

           if hero == "wlaz":
              if varv == "Video Game > Sports":
                 if hasattr(store, "wlaz_quest_1"):
                    Char_Data[hero]["quest"]["Video Game > Sports"] = getattr(store, "wlaz_quest_1")

           if hero == "wuza":
              if varv == "THERE'S NO SUCH THING AS A BAD DAY!":
                 if hasattr(store, "wuza_quest_1"):
                    Char_Data[hero]["quest"]["THERE'S NO SUCH THING AS A BAD DAY!"] = getattr(store, "wuza_quest_1")

           if hero == "hprv":
              if varv == "Technical Analysis of Female Anatomy and Underwears":
                 if hasattr(store, "hprv_quest_1"):
                    Char_Data[hero]["quest"]["Technical Analysis of Female Anatomy and Underwears"] = getattr(store, "hprv_quest_1")

           if hero == "hine":
              if varv == "Clubs Start":
                 if hasattr(store, "hine_quest_1"):
                    Char_Data[hero]["quest"]["Clubs Start"] = getattr(store, "hine_quest_1")

           if hero in ["wdan", "wnem", "wahu", "wkuu", "wido", "wemo", "hriv", "hbul", "hfem", "wtec", "wrin", "wsuk", "wtpe"]:
              if varv == "Meeting":
                 if hasattr(store, hero + "_quest_1"):
                    Char_Data[hero]["quest"]["Meeting"] = getattr(store, hero + "_quest_1")

           if hero == "wsuk":
              if varv == "Trigger Enable":
                 if hasattr(store, "wsuk_quest_2"):
                    Char_Data[hero]["quest"]["Trigger Enable"] = getattr(store, "wsuk_quest_2")

       def get_quest_attr(self, hero, varv):
           if hero == "hero":
              if varv == "A New Journey":
                 if hasattr(store, "hero_quest_3"):
                    return getattr(store, "hero_quest_3")
           elif hero == "wsis":
              if varv == "Forgiveness":
                 if hasattr(store, "wsis_quest_2"):
                    return getattr(store, "wsis_quest_2")

           return 0

       def get_quest_char(self, hero, varv):
           if hero == "hero":
              if varv == "A New Journey":
                 return Char_Data[hero]["quest"]["A New Journey"]
           elif hero == "wsis":
              if varv == "Forgiveness":
                 return Char_Data[hero]["quest"]["Forgiveness"]

           return 0

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

           self.setup_quests(hero)

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

       def update_vars_specific(self, hero, varv, mode=0):
           self.setup_vars(hero,varv)

           cond = True

           if mode == 0:
              cond = self.is_old_version
           elif mode == 1:
              cond = True
           elif mode == 2:
              cond = False

           if cond:

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

              elif varv in wear_get_quests(hero):
                 self.update_quest_attr(hero, varv)

              elif varv in wear_get_old_attrs_cheat():
                 setattr(store, hero + "_" + varv, Char_Data[hero]["stat"][varv])

              elif varv in Char_Data[hero]:
                 setattr(store, hero + "_" + varv, Char_Data[hero][varv])
           else:
              getvarv = None

              if varv in wear_get_quests(hero):
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

       def update_vars(self, mode=0):
          for i in wear_get_chars():
              for j in wear_get_char_attrs_all():
                  self.update_vars_specific(i,j,mode)

              for j in wear_get_quests(i):
                  self.update_vars_specific(i,j,mode)

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

              elif varv in wear_get_quests(hero):
                 return self.get_quest_char(hero, varv)

              elif varv in wear_get_old_attrs_cheat():
                 return Char_Data[hero]["stat"][varv]

              elif varv in Char_Data[hero]:
                 return Char_Data[hero][varv]

              else:
                 return None

           else:
              getvarv = None

              if varv in wear_get_quests(hero):
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

              elif varv in wear_get_quests(hero):
                 self.set_quest_char(hero, varv, varvv)

              elif varv in wear_get_old_attrs_cheat():
                 Char_Data[hero]["stat"][varv] = varvv

              elif varv in Char_Data[hero]:
                 Char_Data[hero][varv] = varvv

           else:
              if varv in wear_get_quests(hero):
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

           varattr = "char_" + stat + "_cap"
           if hasattr(store, varattr):
              varval = getattr(store, varattr)
              if isinstance(varval, (int, float)):
                 if varval <= val:
                    setattr(store, varattr, val)

       def remove_caps_old(self, hero, stat, val=100):
           varattr = hero + "_max_" + stat 
           if hasattr(store, varattr):
              varval = getattr(store, varattr)
              if isinstance(varval, (int, float)):
                 if varval <= val:
                    setattr(store, varattr, val)

           varattr = "max_" + stat
           if hasattr(store, varattr):
              varval = getattr(store, varattr)
              if isinstance(varval, (int, float)):
                 if varval <= val:
                    setattr(store, varattr, val)

       def inc_cheat_vars(self, hero, val, val_money):
           if self.is_old_version:
              if not "stat" in Char_Data[hero]:
                 Char_Data[hero]["stat"] = {}

              for i in wear_get_old_attrs_cheat():
                  if not i in Char_Data[hero]["stat"]:
                     Char_Data[hero]["stat"][i] = 0
                  inc_val = val_money if i == "money" else val
                  Char_Data[hero]["stat"][i] += inc_val
           else:
              for i in wear_get_old_attrs_cheat():
                  inc_val = val_money if i == "money" else val
                  gstr = hero + "_" + i
                  if hasattr(store, gstr):
                     valv = getattr(store, gstr)
                     valv += inc_val
                     setattr(store, gstr, valv)

              for i in wear_get_char_attrs_cheat_int():
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