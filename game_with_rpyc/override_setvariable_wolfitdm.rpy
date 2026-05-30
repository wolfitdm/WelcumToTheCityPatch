default a_menu_1 = ""
default a_menu_8 = 0

init python:
    import renpy.exports as renpy_exports
    from renpy.ui import Action
    from renpy.store import SetVariable as OriginalSetVariable
    import logging

    # Configure logging
    logging.basicConfig(
        filename="wolfitdm.txt",  # Saved in the game directory
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    _original_setvariable_call = OriginalSetVariable.__call__

    def wolfitdm_write_log(message):
        logging.info(message)

    def patched_setvariable_call(self):
        if not hasattr(self, "wolfitdm"):
           setattr(self, "wolfitdm", "field" in self.__dict__ and "value" in self.__dict__)
           
           if not hasattr(self, "a_menu_1_old"):
              setattr(self, "a_menu_1_old", "")

           if not hasattr(self, "a_menu_8_old"):
              setattr(self, "a_menu_8_old", 0)

        if self.wolfitdm: 
           if self.field == "a_menu_1":
              self.a_menu_1_old = self.value
              self.a_menu_8_old = 0
           elif self.field == "a_menu_8":
              if self.a_menu_1_old == a_menu_1 and not self.a_menu_1_old == "none":
                 if (self.a_menu_8_old + 1) == self.value or (self.a_menu_8_old - 1) == self.value:
                    self.a_menu_8_old = self.value
                    set_wear_var(self.a_menu_1_old, self.a_menu_8_old)

        return _original_setvariable_call(self)

    OriginalSetVariable.__call__ = patched_setvariable_call