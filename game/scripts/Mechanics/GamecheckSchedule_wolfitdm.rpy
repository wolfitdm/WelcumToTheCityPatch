default Char_Data = {}
default wolfitdm_hero_name = "hero"
default wolfitdm_full_nudist = False
default wolfitdm_override_map = {}

init 90000 python:
    wolfitdm_Get_NPCWear = None
    wolfitdm_Get_NPCMap =  None

    if wolfitdm_Get_NPCWear == None and callable(Get_NPCWear):
       wolfitdm_Get_NPCWear = Get_NPCWear

    if wolfitdm_Get_NPCMap == None and callable(Get_NPCMap):
       wolfitdm_Get_NPCMap = Get_NPCMap
    
    def Get_NPCWear(npc_id):
        if wolfitdm_hero_name == npc_id:
           return Char_Data[npc_id]["wear"]
        else:
           if wolfitdm_full_nudist:
              return Char_Data[npc_id]["wear"]
           return wolfitdm_Get_NPCWear(npc_id)

    def Get_NPCMap(npc_id):
        if npc_id in wolfitdm_override_map:
           if not wolfitdm_override_map[npc_id] == None:
              return wolfitdm_override_map[npc_id]

        return wolfitdm_Get_NPCMap(npc_id)