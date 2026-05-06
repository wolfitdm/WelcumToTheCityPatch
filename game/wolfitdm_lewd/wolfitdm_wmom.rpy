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

label wolfitdm_fuck_wmom:

      $ choice = renpy.random.choice(["wmom_son", "wmom_friend"])

      if choice == "wmom_son":
         $ wolfitdm_wmom_son_var = renpy.random.randint(0, 2)

         show wolfitdm_wmom_son at wolfitdm_fill_screen

         wmom "Honey. Give it to me right. I love you so much."
         hero "I love you too"

         "You two have great sex"

         hide wolfitdm_wmom_son

      elif choice == "wmom_friend":
         $ wolfitdm_wmom_friend_var = renpy.random.randint(0, 0)
        
         show wolfitdm_wmom_friend at wolfitdm_fill_screen

         "You look through the keyhole and see someone having sex."

         "You're silent and savor the moment."

         hide wolfitdm_wmom_friend

      return