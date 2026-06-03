init -90001 python:
     def wolfitdm_get_load_any_saves():
         if not hasattr(persistent, "wolfitdm_load_any_saves"):
            setattr(persistent, "wolfitdm_load_any_saves", False)

            renpy.save_persistent()

         return persistent.wolfitdm_load_any_saves

     def wolfitdm_load_any_saves():
         if not hasattr(persistent, "wolfitdm_load_any_saves"):
            setattr(persistent, "wolfitdm_load_any_saves", False)

            renpy.save_persistent()

         if persistent.wolfitdm_load_any_saves:
            config.label_overrides["after_load"] = "after_load_wolfitdm"
            config.label_overrides["after_load_original"] = "after_load"
         else:
            config.label_overrides["after_load"] = "after_load"
            config.label_overrides["after_load_original"] = "after_load"

     def wolfitdm_set_load_any_saves(set=False):
         if not hasattr(persistent, "wolfitdm_load_any_saves"):
            setattr(persistent, "wolfitdm_load_any_saves", False)

            renpy.save_persistent()

         persistent.wolfitdm_load_any_saves = set
         renpy.save_persistent()

         wolfitdm_load_any_saves()

     wolfitdm_load_any_saves()

label after_load_wolfitdm:
     python:
        for i in range(36, 50, 1):
            for j in range(0, 10, 1):
                after_load_str = "afterload_" + str(j) + "_" + str(i)
                if not hasattr(store, after_load_str):
                   setattr(store, after_load_str, True)

        renpy.call("after_load_original")