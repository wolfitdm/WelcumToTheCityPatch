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

label wolfitdm_fuck_wsis:

      $ choice = renpy.random.choice(["bro_sis", "bro_sis_friend"])

      if choice == "bro_sis":
         $ wolfitdm_wsis_bro_sis_var = renpy.random.randint(0, 8)

         show wolfitdm_wsis_bro_sis at wolfitdm_fill_screen

         wsis "Please fuck me really hard. Give me what I desperately crave. I've waited so long for this."
         hero "I've been waiting so long for this too, let's have sex."

         "You two have wonderful sex."

         hide wolfitdm_wsis_bro_sis

      elif choice == "bro_sis_friend":
         $ wolfitdm_wsis_bro_sis_friend_var = renpy.random.randint(0, 0)
        
         show wolfitdm_wsis_bro_sis_friend at wolfitdm_fill_screen

         "You watch her have sex with a classmate. Not bad either."

         hide wolfitdm_wsis_bro_sis_friend

      return