default wolfitdm_hpap_wnei_school_sc_var = 0
default wolfitdm_wmam_wnei_school_sc_var = 0

image wolfitdm_hpap_wnei_school_sc:
    ConditionSwitch(
        "True", "wolfitdm_lewd/wnei/hpap_wnei_school_sc/%s.png" % wolfitdm_hpap_wnei_school_sc_var
    )

image wolfitdm_wmam_wnei_school_sc:
    ConditionSwitch(
        "True", "wolfitdm_lewd/wnei/wmam_wnei_school_sc/%s.png" % wolfitdm_wmam_wnei_school_sc_var
    )

transform wolfitdm_fill_screen:
    size (config.screen_width, config.screen_height)  # Match game resolution

label wolfitdm_fuck_wnei_scene(choice, image):

      if choice == "hpap_wnei_school_sc":
         $ select_scene = image

         $ max_scene = 1

         if image >= max_scene:
            $ select_scene = image = max_scene            
         elif image <= 0:
            $ select_scene = image = 0

         $ wolfitdm_hpap_wnei_school_sc_var = select_scene

         show wolfitdm_hpap_wnei_school_sc at wolfitdm_fill_screen

         if image == 0:

            "You go to the sports field and are surprised."

            "You see something you can hardly believe."

            "You watch as your childhood friend's father fucks her vagina, you can't believe it."

            wnei "Dad, if you’ve fucked me really good, then I don’t have to do my homework, right?"
            hpap "Right, and now let's continue training our abdominal muscles."

            "You decide to leave, as you are somewhat shocked and cannot believe what just happened."

         elif image == 1:

            "You go to the sports field and are surprised."

            "You see something you can hardly believe."

            wnei "Am I doing the exercise correctly?"
            hpap "Oh, you're doing that very well, sweetheart."

            "You decide to leave, as you are somewhat shocked and cannot believe what just happened."

         else:

            "No dialogue available."

         hide wolfitdm_hpap_wnei_school_sc

      elif choice == "wmam_wnei_school_sc":
         $ select_scene = image

         $ max_scene = 0

         if image >= max_scene:
            $ select_scene = image = max_scene            
         elif image <= 0:
            $ select_scene = image = 0

         $ wolfitdm_wmam_wnei_school_sc_var = select_scene
        
         show wolfitdm_wmam_wnei_school_sc at wolfitdm_fill_screen

         if image == 0:

            "You go to the sports field and are surprised."

            "You see something you can hardly believe."

            wmam "Look, daughter, that one over there wants to be licked."
            wnei "Mom, you're so cringe, first you force me to take off my clothes, and now you want me to lick your pussy, too?"

            wmam "Come here now, sweetheart. Right now."

            "You decide to leave, as you are somewhat shocked and cannot believe what just happened."

         elif image == 1:

            "You go to the sports field and are surprised."

            "You see something you can hardly believe."

            "You think to yourself, This can't be real, you can't believe your eyes at what you're seeing right now."

            wmam "There, Sweetheart, that’s how you give a French kiss."
            wnei "Oh, I wouldn't have thought that this would feel so good."

            "You decide to leave, as you are somewhat shocked and cannot believe what just happened."

         else:

            "No dialogue available."

         hide wolfitdm_wmam_wnei_school_sc

      return

label wolfitdm_fuck_wnei:

      # wnei school sports court
      
      python:
         menu_items = []

         hpap_wnei_school_sc_maxscene = 1
         wmam_wnei_school_sc_maxscene = 1

         menu_items.append(("Random", "random"))
         menu_items.append(("Father & Daughter / School - Sports Court", "hpap_wnei_school_sc"))
         menu_items.append(("Mom & Daughter / School - Sports Court", "wmam_wnei_school_sc"))

         choice = renpy.display_menu(menu_items)

         menu_items = []
         image = "nochoice"

         if choice == "hpap_wnei_school_sc":
            for i in range(0, hpap_wnei_school_sc_maxscene + 1):
                menu_items.append(("Scene " + str(i), i))
            menu_items.append(("Return", "nochoice"))
            image = renpy.display_menu(menu_items)
         elif choice == "wmam_wnei_school_sc":
            for i in range(0, wmam_wnei_school_sc_maxscene + 1):
                menu_items.append(("Scene " + str(i), i))
            menu_items.append(("Return", "nochoice"))
            image = renpy.display_menu(menu_items)
         elif choice == "random":
            choice = renpy.random.choice(["hpap_wnei_school_sc", "wmam_wnei_school_sc"])

            if choice == "hpap_wnei_school_sc":
               image = renpy.random.randint(0, hpap_wnei_school_sc_maxscene)
            elif choice == "wmam_wnei_school_sc":
               image = renpy.random.randint(0, wmam_wnei_school_sc_maxscene)

         if choice == "nochoice" or image == "nochoice":
            pass
         else:
            renpy.call("wolfitdm_fuck_wnei_scene", choice, image)      

      return