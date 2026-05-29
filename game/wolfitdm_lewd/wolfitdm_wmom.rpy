default wolfitdm_wmom_son_var = 0
default wolfitdm_wmom_friend_var = 0

image wolfitdm_wmom_son:
    ConditionSwitch(
        "True", "wolfitdm_lewd/wmom/wmom_son/%s.png" % wolfitdm_wmom_son_var
    )

image wolfitdm_wmom_friend:
    ConditionSwitch(
        "True", "wolfitdm_lewd/wmom/wmom_friend/%s.png" % wolfitdm_wmom_friend_var
    )

transform wolfitdm_fill_screen:
    size (config.screen_width, config.screen_height)  # Match game resolution

init python:
    def hero_in_wmom_bedroom():
        try:
            map = Map_Data["home"]["name"] + " - " + Map_Data["home"]["map"]["bedroom_wmom"]["name"]
            the_hero_map = WChar.gvar("hero", "map")

            return map == the_hero_map
        except:
            return True

label wolfitdm_fuck_wmom_scene(choice, image):
      if choice == "wmom_son":
         $ select_scene = image

         $ max_scene = 2

         if image >= max_scene:
            $ select_scene = image = max_scene            
         elif image <= 0:
            $ select_scene = image = 0

         $ wolfitdm_wmom_son_var = select_scene

         show wolfitdm_wmom_son at wolfitdm_fill_screen

         wmom "Honey. Give it to me right. I love you so much."
         hero "I love you too"

         "You two have great sex"

         hide wolfitdm_wmom_son

      elif choice == "wmom_friend":
         $ select_scene = image

         $ max_scene = 0

         if image >= max_scene:
            $ select_scene = image = max_scene    
         elif image <= 0:
            $ select_scene = image = 0

         $ wolfitdm_wmom_friend_var = select_scene
        
         show wolfitdm_wmom_friend at wolfitdm_fill_screen

         "You look through the keyhole and see someone having sex."

         "You're silent and savor the moment."

         hide wolfitdm_wmom_friend

      return

label wolfitdm_fuck_wmom:

      #if not hero_in_wmom_bedroom():
      #   "Only scenes available in Moms Bedroom!"
      #   return

      # wmom_bedroom
      
      python:
         menu_items = []

         wmom_son_maxscene = 2
         wmom_friend_maxscene = 0

         menu_items.append(("Random / Moms Bedroom", "random"))
         menu_items.append(("Mom and Son / Moms Bedroom", "wmom_son"))
         menu_items.append(("Mom and Friend / Moms Bedroom", "wmom_friend"))

         choice = renpy.display_menu(menu_items)

         menu_items = []

         if choice == "wmom_friend":
            for i in range(0, wmom_friend_maxscene + 1):
                menu_items.append(("Scene " + str(i), i))
            image = renpy.display_menu(menu_items)
         elif choice == "wmom_son":
            for i in range(0, wmom_son_maxscene + 1):
                menu_items.append(("Scene " + str(i), i))
            image = renpy.display_menu(menu_items)
         else:
            choice = renpy.random.choice(["wmom_son", "wmom_friend"])

            if choice == "wmom_son":
               image = renpy.random.randint(0, wmom_son_maxscene)
            elif choice == "wmom_friend":
               image = renpy.random.randint(0, wmom_friend_maxscene)

         renpy.call("wolfitdm_fuck_wmom_scene", choice, image)
      return