# Icons & Emojis

define C_Heart_Icon = "{outlinecolor=#960000}{color=#FF3232}{b}❤{/b}{/color}{/outlinecolor}"
define C_Pencil_Icon = "{outlinecolor=#960000}{color=#FFFF64}{b}✏{/b}{/color}{/outlinecolor}"
define C_X_Icon = "{outlinecolor=#960000}{color=#FF3232}{b}✖{/b}{/color}{/outlinecolor}"
define C_Checkmark_Icon = "{outlinecolor=#960000}{color=#32FF32}{b}✔{/b}{/color}{/outlinecolor}"

init 0 python:
    translate_scenefix = renpy.translation.StringTranslator.translate
    _orig_replace_text_scenefix = config.replace_text
    _exec_orig_replace_text_scenefix = not _orig_replace_text_scenefix == None
    _exec_orig_replace_text_scenefix = _exec_orig_replace_text_scenefix and callable(_orig_replace_text_scenefix)
    from re import compile

    heart_icon = compile(r"\[❤\]")
    pencil_icon = compile(r"\[✏\]") 
    x_icon = compile(r"\[✖\]")
    checkmark_icon = compile(r"\[✔\]")

    del compile

    def scenefix_patch(self, t):
        t = translate_scenefix(self, t)

        t = t.replace("[❤]", "[C_Heart_Icon]")
        t = t.replace("[✏]", "[C_Pencil_Icon]")
        t = t.replace("[✖]", "[C_X_Icon]")
        t = t.replace("[✔]", "[C_Checkmark_Icon]")

        t = heart_icon.sub("[C_Heart_Icon]", t)
        t = pencil_icon.sub("[C_Pencil_Icon]", t)
        t = x_icon.sub("[C_X_Icon]", t)
        t = checkmark_icon.sub("[C_Checkmark_Icon]", t)

        return t

    renpy.translation.StringTranslator.translate = scenefix_patch

    del scenefix_patch

    def replace_text_scenefix(text):
        
        if _exec_orig_replace_text_scenefix:
           text = _orig_replace_text_scenefix(text)

        text = text.replace("[❤]", "[C_Heart_Icon]")
        text = text.replace("[✏]", "[C_Pencil_Icon]")
        text = text.replace("[✖]", "[C_X_Icon]")
        text = text.replace("[✔]", "[C_Checkmark_Icon]")

        return text

    config.replace_text = replace_text_scenefix

    del replace_text_scenefix