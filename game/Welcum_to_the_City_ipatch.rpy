default incest_patch_on = True

# Icons & Emojis
define C_Heart_Icon = "{outlinecolor=#960000}{color=#FF3232}{b}❤{/b}{/color}{/outlinecolor}"
define C_Pencil_Icon = "{outlinecolor=#960000}{color=#FFFF64}{b}✏{/b}{/color}{/outlinecolor}"
define C_X_Icon = "{outlinecolor=#960000}{color=#FF3232}{b}✖{/b}{/color}{/outlinecolor}"
define C_Checkmark_Icon = "{outlinecolor=#960000}{color=#32FF32}{b}✔{/b}{/color}{/outlinecolor}"

######################################################  MADE BY simple_human   

######################################################  DOWNLOADED FROM https://f95zone.to/threads/welcum-to-the-city-v0-15-0-quiquersson.168621/post-12597838

init 1 python hide:
######################################################
    translate = renpy.translation.StringTranslator.translate

    def set_incest_patch_on(set):
        incest_patch_on = set

######################################################
    from re import compile

    mom = compile(r"(?i)step(?:[-\s]?mom|[-\s]?mother)")  
    sis = compile(r"(?i)step(?:[-\s]?sis(?:ter)?)") 
    bro = compile(r"(?i)step(?:[-\s]?bro(?:ther)?)") 
    gmom = compile(r"(?i)step(?:[-\s]?grandma|[-\s]?grandmother)")   
    cuz = compile(r"(?i)step(?:[-\s]?cuz|[-\s]?cousin)")

    momr = compile(r"Mother")  
    sisr = compile(r"Sister") 
    bror = compile(r"Brother") 
    gmomr = compile(r"Grandmother")   
    cuzr = compile(r"Cousin")

    heart_icon = compile(r"\[❤\]")
    pencil_icon = compile(r"\[✏\]") 
    x_icon = compile(r"\[✖\]")
    checkmark_icon = compile(r"\[✔\]")

    del compile

    def incest_sub(character, t):
        if character == "Mother":
           if incest_patch_on:
              t = mom.sub(character, t)
           else:
              t = momr.sub("Step-"+character, t)

        elif character == "Sister":
           if incest_patch_on:
              t = sis.sub(character, t)
           else:
              t = sisr.sub("Step-"+character, t)

        elif character == "Brother":
           if incest_patch_on:
              t = bro.sub(character, t)
           else:
              t = bror.sub("Step-"+character, t)

        elif character == "Grandmother":
           if incest_patch_on:
              t = gmom.sub(character, t)
           else:
              t = gmomr.sub("Step-"+character, t)

        elif character == "Cousin":
           if incest_patch_on:
              t = cuz.sub(character, t)
           else:
              t = cuzr.sub("Step-"+character, t)

        return t

    def incest_replace(t,old,new):
        if incest_patch_on:
           t = t.replace(old, new)
        else:
           t = t.replace(new, old)

        return t

######################################################
    def sim_hum_ipatch(self, t):
        t = translate(self, t)

        t = t.replace("[❤]", "[C_Heart_Icon]")
        t = t.replace("[✏]", "[C_Pencil_Icon]")
        t = t.replace("[✖]", "[C_X_Icon]")
        t = t.replace("[✔]", "[C_Checkmark_Icon]")

        t = heart_icon.sub("[C_Heart_Icon]", t)
        t = pencil_icon.sub("[C_Pencil_Icon]", t)
        t = x_icon.sub("[C_X_Icon]", t)
        t = checkmark_icon.sub("[C_Checkmark_Icon]", t)

##################
        t = incest_replace(t, "It's a strange feeling, knowing that my father is gone.{w=[wt4]} Well{w=[wt2]}, now he must be happy with my mother again...{w=[wt2]} But now I'm alone.{w=[wt3]} And my situation has become very difficult in the countryside without their support.)","It's a strange feeling, knowing that my father is gone.)")
        t = incest_replace(t, "{mind}(Well...{w=[wt2]} maybe not much{w=[wt2]}, but it can't be that bad, right?{w=[wt3]} She's not my biological grandmother{w=[wt1]}, but it would still be good to see {nm}[talkto_wgma]{/nm} again.){/mind}","{mind}(Well...{w=[wt2]} maybe not much{w=[wt2]}, but it can't be that bad, right?{w=[wt3]} It would be nice to see {nm}[talkto_wgma]{/nm} again.){/mind}")
        t = incest_replace(t, "(Wait{w=[wt2]}, is it some kind of karma for {nm}[talkabout_wsis]{/nm}?{w=[wt3]} Or maybe this is all just a family tradition of shaming the next generation?)","(Geez, {nm}[talkto_wgma]{/nm}...)")

        t = incest_replace(t, "Tell she's your step-sister","Tell that you're her brother")
        t = incest_replace(t, "She's my step-sister!","I'm her brother!")
        t = incest_replace(t, "{lg}BWA HA HA HA...{/lg}{w=[wt3]} Did he say {bt}STEP?!{/bt}{w=[wt3]} No, no, no, no, serious!{w=[wt2]} Her mother wanted so much to have a husband who didn't leave her that she really just spread her legs to{w=[wt1]}, like{w=[wt2]}, {bt}everyone on the way!{/bt} {lg}BWA HA HA HA...{/lg}","{lg}BWA HA HA HA...{/lg}{w=[wt3]} Did he say {bt}HER BROTHER?!{/bt}{w=[wt3]} No, no, no, no, serious!{w=[wt2]} Where did you even come from? Your mother is such a whore she doesn't even know how many kids she's had, she really just spread her legs to{w=[wt1]}, like{w=[wt2]}, {bt}everyone on the way!{/bt} {lg}BWA HA HA HA...{/lg}")

        t = incest_replace(t, "I see him as my real father{w=[wt2]}, since the man who brought me into the world never had the courage to acknowledge me, you know?{w=[wt3]} S{w=[wt1]}-sorry for bringing this up!{w=[wt1]} I just...","S{w=[wt1]}-sorry for bringing this up!{w=[wt1]} I just...")

##################
        t = incest_replace(t, "[talkabout_wmom]","my mother")
        t = incest_replace(t, "[talkabout_wsis]","my sister")
        t = incest_replace(t, "[talkabout_wcou]","my cousin")
        t = incest_replace(t, "[talkabout_wgma]","my grandmother")

        t = incest_replace(t, "[talkabout_wmom!c]","My mother")
        t = incest_replace(t, "[talkabout_wsis!c]","My sister")
        t = incest_replace(t, "[talkabout_wcou!c]","My cousin")
        t = incest_replace(t, "[talkabout_wgma!c]","My grandmother")

        t = incest_replace(t, "[talkto_wmom]","Mom")
        t = incest_replace(t, "[talkto_wsis]","Sis")
        t = incest_replace(t, "[talkto_wcou]","Cousin")
        t = incest_replace(t, "[talkto_wgma]","Grandma")

        t = incest_replace(t, "[hero_about_wmom]","my mother")
        t = incest_replace(t, "[hero_about_wsis]","my sister")
        t = incest_replace(t, "[hero_about_wcou]","my cousin")
        t = incest_replace(t, "[hero_about_wcou]","my aunt")
        t = incest_replace(t, "[hero_about_wgma]","my grandmother")

        t = incest_replace(t, "[hero_about_wmom!c]","My mother")
        t = incest_replace(t, "[hero_about_wsis!c]","My sister")
        t = incest_replace(t, "[hero_about_wcou!c]","My cousin")
        t = incest_replace(t, "[hero_about_wcou!c]","My aunt")
        t = incest_replace(t, "[hero_about_wgma!c]","My grandmother")

        t = incest_replace(t, "[hero_to_wmom]","Mom")
        t = incest_replace(t, "[hero_to_wsis]","Sis")
        t = incest_replace(t, "[hero_to_wcou]","Cousin")
        t = incest_replace(t, "[hero_to_waun]","Auntie")
        t = incest_replace(t, "[hero_to_wgma]","Grandma")

        t = incest_sub("Mother", t)
        t = incest_sub("Sister", t)
        t = incest_sub("Brother", t)
        t = incest_sub("Grandmother", t)
        t = incest_sub("Cousin", t)

##################
        return t

    renpy.translation.StringTranslator.translate = sim_hum_ipatch
    del sim_hum_ipatch

######################################################
    def replace_text(text):

        text = text.replace("[❤]", "[C_Heart_Icon]")
        text = text.replace("[✏]", "[C_Pencil_Icon]")
        text = text.replace("[✖]", "[C_X_Icon]")
        text = text.replace("[✔]", "[C_Checkmark_Icon]")

        text = incest_replace(text, "Home - Step-mother's bedroom","Home - Mother's bedroom")
        text = incest_replace(text, "Home - Step-sis' bedroom","Home - Sister's bedroom")

        return text

    config.replace_text = replace_text

######################################################

######################################################  MADE BY simple_human   

######################################################  DOWNLOADED FROM https://f95zone.to/threads/welcum-to-the-city-v0-15-0-quiquersson.168621/post-12597838
