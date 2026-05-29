default wolfitdm_wsis_bro_sis_var = 0
default wolfitdm_wsis_bro_sis_friend_var = 0

image wolfitdm_wsis_bro_sis:
    ConditionSwitch(
        "True", "wolfitdm_lewd/wsis/bro_sis/%s.png" % wolfitdm_wsis_bro_sis_var
    )

image wolfitdm_wsis_bro_sis_friend:
    ConditionSwitch(
        "True", "wolfitdm_lewd/wsis/bro_sis_friend/%s.png" % wolfitdm_wsis_bro_sis_friend_var
    )

transform wolfitdm_fill_screen:
    size (config.screen_width, config.screen_height)  # Match game resolution

label wolfitdm_fuck_wsis_scene(choice, image):

      if choice == "bro_sis":
         $ select_scene = image

         $ max_scene = 8

         if image >= max_scene:
            $ select_scene = image = max_scene            
         elif image <= 0:
            $ select_scene = image = 0

         $ wolfitdm_wsis_bro_sis_var = select_scene

         show wolfitdm_wsis_bro_sis at wolfitdm_fill_screen

         wsis "Please fuck me really hard. Give me what I desperately crave. I've waited so long for this."
         hero "I've been waiting so long for this too, let's have sex."

         "You two have wonderful sex."

         hide wolfitdm_wsis_bro_sis

      elif choice == "bro_sis_friend":
         $ select_scene = image

         $ max_scene = 0

         if image >= max_scene:
            $ select_scene = image = max_scene            
         elif image <= 0:
            $ select_scene = image = 0

         $ wolfitdm_wsis_bro_sis_friend_var = select_scene
        
         show wolfitdm_wsis_bro_sis_friend at wolfitdm_fill_screen

         "You watch her have sex with a classmate. Not bad either."

         hide wolfitdm_wsis_bro_sis_friend

      return

label wolfitdm_fuck_wsis:

      # wsis_bedroom
      
      python:
         menu_items = []

         bro_sis_maxscene = 8
         bro_sis_friend_maxscene = 0

         menu_items.append(("Random / Sis Bedroom", "random"))
         menu_items.append(("Brother and Sister / Sis Bedroom", "bro_sis"))
         menu_items.append(("Brother & Sister & Classmate / Sis Bedroom", "bro_sis_friend"))

         choice = renpy.display_menu(menu_items)

         menu_items = []

         if choice == "bro_sis":
            for i in range(0, bro_sis_maxscene + 1):
                menu_items.append(("Scene " + str(i), i))
            menu_items.append(("Return", "nochoice"))
            image = renpy.display_menu(menu_items)
         elif choice == "bro_sis_friend":
            for i in range(0, bro_sis_friend_maxscene + 1):
                menu_items.append(("Scene " + str(i), i))
            menu_items.append(("Return", "nochoice"))
            image = renpy.display_menu(menu_items)
         elif choice == "random":
            choice = renpy.random.choice(["bro_sis", "bro_sis_friend"])

            if choice == "bro_sis":
               image = renpy.random.randint(0, bro_sis_maxscene)
            elif choice == "bro_sis_friend":
               image = renpy.random.randint(0, bro_sis_friend_maxscene)

         if choice == "nochoice" or image == "nochoice":
            pass
         else:
            renpy.call("wolfitdm_fuck_wsis_scene", choice, image)      

      return