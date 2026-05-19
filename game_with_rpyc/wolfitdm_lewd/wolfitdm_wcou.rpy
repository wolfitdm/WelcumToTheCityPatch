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

label wolfitdm_fuck_wcou:

      $ choice = renpy.random.choice(["cou_oma_hero", "cou_friend_hero", "cou_friend_oma_hero", "cou_hero", "cou_oma"])

      if choice == "cou_oma_hero":
         $ wolfitdm_wcou_cou_oma_hero_var = renpy.random.randint(0, 21)

         show wolfitdm_wcou_cou_oma_hero at wolfitdm_fill_screen

         hero "Oh yes, we can have really great threesome sex again."
         wcou "Please fuck me really hard... Please give it to me properly."
         wgma "She learned from me. Yes, that's what I want."

         "The three of you are having sex with each other."

         hide wolfitdm_wcou_cou_oma_hero

      elif choice == "cou_friend_hero":
         $ wolfitdm_wcou_cou_friend_hero_var = renpy.random.randint(0, 0)
        
         show wolfitdm_wcou_cou_friend_hero at wolfitdm_fill_screen

         wcou "Please fuck my friend properly"
         hero "Ok. I'm going to do it. I'm going to fuck her really hard. Oh yeah."

         "You're really fucking your classmate."

         hide wolfitdm_wcou_cou_friend_hero

      elif choice == "cou_friend_oma_hero":
         $ wolfitdm_wcou_cou_friend_oma_hero_var = renpy.random.randint(0, 2)
        
         show wolfitdm_wcou_cou_friend_oma_hero at wolfitdm_fill_screen

         hero "A foursome? Really? Oh, I can't keep that up."
         wcou "Please fuck us all."
         wgma "We're counting on you."

         "You're exhausted from all the sex you're having."

         hide wolfitdm_wcou_cou_friend_oma_hero

      elif choice == "cou_hero":
         $ wolfitdm_wcou_cou_hero_var = renpy.random.randint(0, 6)
        
         show wolfitdm_wcou_cou_hero at wolfitdm_fill_screen

         wcou "Please fuck me really hard. Please give me everything."
         hero "I love you so much."

         "You two have great sex with each other."

         hide wolfitdm_wcou_cou_hero

      elif choice == "cou_oma":
         $ wolfitdm_wcou_cou_oma_var = renpy.random.randint(0, 0)
        
         show wolfitdm_wcou_cou_oma at wolfitdm_fill_screen

         "You walk into the room and see your loved ones having sex."

         hero "Oh no. Again?"
         wcou "Oh yes. Hot."
         wgma "I love you so much."

         hide wolfitdm_wcou_cou_oma

      return