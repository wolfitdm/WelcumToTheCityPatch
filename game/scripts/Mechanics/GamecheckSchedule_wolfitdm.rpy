default Char_Data = {}
default wolfitdm_hero_name = "hero"
default wolfitdm_full_nudist = False

init 90000 python:
    wolfitdm_Get_NPCWear = None

    if wolfitdm_Get_NPCWear == None and callable(Get_NPCWear):
       wolfitdm_Get_NPCWear = Get_NPCWear
    
    def Get_NPCWear(npc_id):
        if wolfitdm_hero_name == npc_id:
           return Char_Data[npc_id]["wear"]
        else:
           if wolfitdm_full_nudist:
              return Char_Data[npc_id]["wear"]
           return wolfitdm_Get_NPCWear(npc_id)
