default wolfitdm_wcou_cou_oma_hero_var = 0
default wolfitdm_wcou_cou_friend_hero_var = 0
default wolfitdm_wcou_cou_friend_oma_hero_var = 0
default wolfitdm_wcou_cou_hero_var = 0
default wolfitdm_wcou_cou_oma_var = 0

image wolfitdm_wcou_cou_oma_hero:
    ConditionSwitch(
        "True", "wolfitdm_lewd/wcou/cou_oma_hero/%s.png" % wolfitdm_wcou_cou_oma_hero_var
    )

image wolfitdm_wcou_cou_friend_hero:
    ConditionSwitch(
        "True", "wolfitdm_lewd/wcou/cou_friend_hero/%s.png" % wolfitdm_wcou_cou_friend_hero_var
    )

image wolfitdm_wcou_cou_friend_oma_hero:
    ConditionSwitch(
        "True", "wolfitdm_lewd/wcou/cou_friend_oma_hero/%s.png" % wolfitdm_wcou_cou_friend_oma_hero_var
    )

image wolfitdm_wcou_cou_hero:
    ConditionSwitch(
        "True", "wolfitdm_lewd/wcou/cou_hero/%s.png" % wolfitdm_wcou_cou_hero_var
    )

image wolfitdm_wcou_cou_oma:
    ConditionSwitch(
        "True", "wolfitdm_lewd/wcou/cou_oma/%s.png" % wolfitdm_wcou_cou_oma_var
    )

transform wolfitdm_fill_screen:
    size (config.screen_width, config.screen_height)  # Match game resolution

label wolfitdm_fuck_wcou_scene(choice, image):

      if choice == "cou_oma_hero":

         $ select_scene = image

         $ max_scene = 21

         if image >= max_scene:
            $ select_scene = image = max_scene            
         elif image <= 0:
            $ select_scene = image = 0

         $ wolfitdm_wcou_cou_oma_hero_var = select_scene

         show wolfitdm_wcou_cou_oma_hero at wolfitdm_fill_screen

         hero "Oh yes, we can have really great threesome sex again."
         wcou "Please fuck me really hard... Please give it to me properly."
         wgma "She learned from me. Yes, that's what I want."

         "The three of you are having sex with each other."

         hide wolfitdm_wcou_cou_oma_hero

      elif choice == "cou_friend_hero":

         $ select_scene = image

         $ max_scene = 0

         if image >= max_scene:
            $ select_scene = image = max_scene            
         elif image <= 0:
            $ select_scene = image = 0

         $ wolfitdm_wcou_cou_friend_hero_var = select_scene
        
         show wolfitdm_wcou_cou_friend_hero at wolfitdm_fill_screen

         wcou "Please fuck my friend properly"
         hero "Ok. I'm going to do it. I'm going to fuck her really hard. Oh yeah."

         "You're really fucking your classmate."

         hide wolfitdm_wcou_cou_friend_hero

      elif choice == "cou_friend_oma_hero":

         $ select_scene = image

         $ max_scene = 2

         if image >= max_scene:
            $ select_scene = image = max_scene            
         elif image <= 0:
            $ select_scene = image = 0

         $ wolfitdm_wcou_cou_friend_oma_hero_var = select_scene
        
         show wolfitdm_wcou_cou_friend_oma_hero at wolfitdm_fill_screen

         hero "A foursome? Really? Oh, I can't keep that up."
         wcou "Please fuck us all."
         wgma "We're counting on you."

         "You're exhausted from all the sex you're having."

         hide wolfitdm_wcou_cou_friend_oma_hero

      elif choice == "cou_hero":
         $ select_scene = image

         $ max_scene = 6

         if image >= max_scene:
            $ select_scene = image = max_scene            
         elif image <= 0:
            $ select_scene = image = 0

         $ wolfitdm_wcou_cou_hero_var = select_scene
        
         show wolfitdm_wcou_cou_hero at wolfitdm_fill_screen

         wcou "Please fuck me really hard. Please give me everything."
         hero "I love you so much."

         "You two have great sex with each other."

         hide wolfitdm_wcou_cou_hero

      elif choice == "cou_oma":
         $ select_scene = image

         $ max_scene = 0

         if image >= max_scene:
            $ select_scene = image = max_scene            
         elif image <= 0:
            $ select_scene = image = 0

         $ wolfitdm_wcou_cou_oma_var = select_scene
        
         show wolfitdm_wcou_cou_oma at wolfitdm_fill_screen

         "You walk into the room and see your loved ones having sex."

         hero "Oh no. Again?"
         wcou "Oh yes. Hot."
         wgma "I love you so much."

         hide wolfitdm_wcou_cou_oma

      return

label wolfitdm_fuck_wcou:

      # wcou_office
      
      python:
         menu_items = []

         cou_oma_hero_maxscene = 21
         cou_friend_hero_maxscene = 0
         cou_friend_oma_hero_maxscene = 2
         cou_hero_maxscene = 6
         cou_oma_maxscene = 0

         menu_items.append(("Random / Cousins Office", "random"))
         menu_items.append(("Cousin & Grandma & You / Cousins Office", "cou_oma_hero"))
         menu_items.append(("Cousin & Friend & You / Cousins Office", "cou_friend_hero"))
         menu_items.append(("Cousin & Friend & Grandma & You / Cousins Office", "cou_friend_oma_hero"))
         menu_items.append(("Cousin & You / Cousins Office", "cou_hero"))
         menu_items.append(("Cousin & Grandma / Cousins Office", "cou_oma"))
         menu_items.append(("Return", "nochoice"))

         choice = renpy.display_menu(menu_items)

         menu_items = []
         image = "nochoice"

         if choice == "cou_oma_hero":
            for i in range(0, cou_oma_hero_maxscene + 1):
                menu_items.append(("Scene " + str(i), i))
            menu_items.append(("Return", "nochoice"))
            image = renpy.display_menu(menu_items)
         elif choice == "cou_friend_hero":
            for i in range(0, cou_friend_hero_maxscene + 1):
                menu_items.append(("Scene " + str(i), i))
            menu_items.append(("Return", "nochoice"))
            image = renpy.display_menu(menu_items)
         elif choice == "cou_friend_oma_hero":
            for i in range(0, cou_friend_oma_hero_maxscene + 1):
                menu_items.append(("Scene " + str(i), i))
            menu_items.append(("Return", "nochoice"))
            image = renpy.display_menu(menu_items)
         elif choice == "cou_hero":
            for i in range(0, cou_hero_maxscene + 1):
                menu_items.append(("Scene " + str(i), i))
            menu_items.append(("Return", "nochoice"))
            image = renpy.display_menu(menu_items)
         elif choice == "cou_oma":
            for i in range(0, cou_oma_maxscene + 1):
                menu_items.append(("Scene " + str(i), i))
            menu_items.append(("Return", "nochoice"))
            image = renpy.display_menu(menu_items)
         elif choice == "random":
            choice = renpy.random.choice(["cou_oma_hero", "cou_friend_hero", "cou_friend_oma_hero", "cou_hero", "cou_oma"])

            if choice == "cou_oma_hero":
               image = renpy.random.randint(0, cou_oma_hero_maxscene)
            elif choice == "cou_friend_hero":
               image = renpy.random.randint(0, cou_friend_hero_maxscene)
            elif choice == "cou_friend_oma_hero":
               image = renpy.random.randint(0, cou_friend_oma_hero_maxscene)
            elif choice == "cou_hero":
               image = renpy.random.randint(0, cou_hero_maxscene)
            elif choice == "cou_oma":
               image = renpy.random.randint(0, cou_oma_maxscene)

         if choice == "nochoice" or image == "nochoice":
            pass
         else:
            renpy.call("wolfitdm_fuck_wcou_scene", choice, image)

      return