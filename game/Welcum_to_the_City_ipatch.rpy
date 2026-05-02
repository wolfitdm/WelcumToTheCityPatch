default incest_patch_on = True

######################################################  MADE BY simple_human   

######################################################  DOWNLOADED FROM https://f95zone.to/threads/welcum-to-the-city-v0-15-0-quiquersson.168621/post-12597838

init 1 python hide:

######################################################
    translate = renpy.translation.StringTranslator.translate

    def set_incest_patch_on(set):
        incest_patch_on = set

        f = renpy.translation.StringTranslator

        if not hasattr(f, "incest_patch_on"):
           setattr(f, "incest_patch_on", incest_patch_on)

        setattr(f, "incest_patch_on", set)

######################################################
    from re import compile

    mom = compile(r"(?i)step(?:[-\s]?mom|[-\s]?mother)")  
    sis = compile(r"(?i)step(?:[-\s]?sis(?:ter)?)") 
    bro = compile(r"(?i)step(?:[-\s]?bro(?:ther)?)") 
    gmom = compile(r"(?i)step(?:[-\s]?grandma|[-\s]?grandmother)")   
    cuz = compile(r"(?i)step(?:[-\s]?cuz|[-\s]?cousin)")  

    del compile

######################################################
    def sim_hum_ipatch(self, t):
        t = translate(self, t)

        if not hasattr(self, "incest_patch_on"):
           setattr(self, "incest_patch_on", incest_patch_on)

        if not self.incest_patch_on:
           return t

##################
        t = t.replace("It's a strange feeling, knowing that my father is gone.{w=[wt4]} Well{w=[wt2]}, now he must be happy with my mother again...{w=[wt2]} But now I'm alone.{w=[wt3]} And my situation has become very difficult in the countryside without their support.)","It's a strange feeling, knowing that my father is gone.)")
        t = t.replace("{mind}(Well...{w=[wt2]} maybe not much{w=[wt2]}, but it can't be that bad, right?{w=[wt3]} She's not my biological grandmother{w=[wt1]}, but it would still be good to see {nm}[talkto_wgma]{/nm} again.){/mind}","{mind}(Well...{w=[wt2]} maybe not much{w=[wt2]}, but it can't be that bad, right?{w=[wt3]} It would be nice to see {nm}[talkto_wgma]{/nm} again.){/mind}")
        t = t.replace("(Wait{w=[wt2]}, is it some kind of karma for {nm}[talkabout_wsis]{/nm}?{w=[wt3]} Or maybe this is all just a family tradition of shaming the next generation?)","(Geez, {nm}[talkto_wgma]{/nm}...)")

        t = t.replace("Tell she's your step-sister","Tell that you're her brother")
        t = t.replace("She's my step-sister!","I'm her brother!")
        t = t.replace("{lg}BWA HA HA HA...{/lg}{w=[wt3]} Did he say {bt}STEP?!{/bt}{w=[wt3]} No, no, no, no, serious!{w=[wt2]} Her mother wanted so much to have a husband who didn't leave her that she really just spread her legs to{w=[wt1]}, like{w=[wt2]}, {bt}everyone on the way!{/bt} {lg}BWA HA HA HA...{/lg}","{lg}BWA HA HA HA...{/lg}{w=[wt3]} Did he say {bt}HER BROTHER?!{/bt}{w=[wt3]} No, no, no, no, serious!{w=[wt2]} Where did you even come from? Your mother is such a whore she doesn't even know how many kids she's had, she really just spread her legs to{w=[wt1]}, like{w=[wt2]}, {bt}everyone on the way!{/bt} {lg}BWA HA HA HA...{/lg}")

        t = t.replace("I see him as my real father{w=[wt2]}, since the man who brought me into the world never had the courage to acknowledge me, you know?{w=[wt3]} S{w=[wt1]}-sorry for bringing this up!{w=[wt1]} I just...","S{w=[wt1]}-sorry for bringing this up!{w=[wt1]} I just...")

##################
        t = t.replace("[talkabout_wmom]","my mother")
        t = t.replace("[talkabout_wsis]","my sister")
        t = t.replace("[talkabout_wcou]","my cousin")
        t = t.replace("[talkabout_wgma]","my grandmother")

        t = t.replace("[talkabout_wmom!c]","My mother")
        t = t.replace("[talkabout_wsis!c]","My sister")
        t = t.replace("[talkabout_wcou!c]","My cousin")
        t = t.replace("[talkabout_wgma!c]","My grandmother")

        t = t.replace("[talkto_wmom]","Mom")
        t = t.replace("[talkto_wsis]","Sis")
        t = t.replace("[talkto_wcou]","Cousin")
        t = t.replace("[talkto_wgma]","Grandma")

        t = t.replace("[hero_about_wmom]","my mother")
        t = t.replace("[hero_about_wsis]","my sister")
        t = t.replace("[hero_about_wcou]","my cousin")
        t = t.replace("[hero_about_wcou]","my aunt")
        t = t.replace("[hero_about_wgma]","my grandmother")

        t = t.replace("[hero_about_wmom!c]","My mother")
        t = t.replace("[hero_about_wsis!c]","My sister")
        t = t.replace("[hero_about_wcou!c]","My cousin")
        t = t.replace("[hero_about_wcou!c]","My aunt")
        t = t.replace("[hero_about_wgma!c]","My grandmother")

        t = t.replace("[hero_to_wmom]","Mom")
        t = t.replace("[hero_to_wsis]","Sis")
        t = t.replace("[hero_to_wcou]","Cousin")
        t = t.replace("[hero_to_waun]","Auntie")
        t = t.replace("[hero_to_wgma]","Grandma")

        t = mom.sub("Mother", t)
        t = sis.sub("Sister", t)
        t = bro.sub("Brother", t)
        t = gmom.sub("Grandmother", t)
        t = cuz.sub("Cousin", t)

##################
        return t

    renpy.translation.StringTranslator.translate = sim_hum_ipatch
    del sim_hum_ipatch

######################################################
    def replace_text(text):

        if not incest_patch_on:

           return text

        text = text.replace("Home - Step-mother's bedroom","Home - Mother's bedroom")
        text = text.replace("Home - Step-sis' bedroom","Home - Sister's bedroom")

        return text

    config.replace_text = replace_text

######################################################

######################################################  MADE BY simple_human   

######################################################  DOWNLOADED FROM https://f95zone.to/threads/welcum-to-the-city-v0-15-0-quiquersson.168621/post-12597838
