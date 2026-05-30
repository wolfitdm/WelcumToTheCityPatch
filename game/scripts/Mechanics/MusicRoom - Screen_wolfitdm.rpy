init python:
    def wolfitdm_add_audio(mname, martist, mpath, mdescription, mlyrics):
        try:
            music_room.add(
               name=mname,
               artist=martist,
               path=mpath,
               description=_(mdescription),
               unlock_condition="True",
               lyrics=mlyrics,
            )
        except:
           pass

    wolfitdm_add_audio("Family Guy - Quahog is Your Home!", "Family Guy", "wolfitdm_audio/familyguy1.mp3", "Family Guy", "Family Guy")
    wolfitdm_add_audio("Best Remix - Gamer Music Part 1!", "Unknown", "wolfitdm_audio/bestremix0.mp3", "Unknown", "Unknown")
    wolfitdm_add_audio("Best Remix - Gamer Music Part 2!", "Unknown", "wolfitdm_audio/bestremix1.mp3", "Unknown", "Unknown")
    wolfitdm_add_audio("Nightcore - Broken Crazy!", "Nightcore", "wolfitdm_audio/broken.mp3", "Unknown", "Unknown")
    wolfitdm_add_audio("Nightcore - Super Psycho Love!", "Nightcore", "wolfitdm_audio/superpsycholove.mp3", "Unknown", "Unknown")
    wolfitdm_add_audio("Family Guy - Bird is the word!", "Family Guy", "wolfitdm_audio/birdistheword.mp3", "Unknown", "Unknown")
    wolfitdm_add_audio("Nightcore - Psycho!", "Nightcore", "wolfitdm_audio/psycho.mp3", "Unknown", "Unknown")
    wolfitdm_add_audio("Nightcore - Slave!", "Nightcore", "wolfitdm_audio/slave.mp3", "Unknown", "Unknown")
    wolfitdm_add_audio("Nightcore - Do Me!", "Nightcore", "wolfitdm_audio/dome.mp3", "Unknown", "Unknown")
    wolfitdm_add_audio("South Park - Cartmans Mom is a Bitch!", "South Park", "wolfitdm_audio/cmbitch.mp3", "Unknown", "Unknown")
    wolfitdm_add_audio("South Park - Pokerface!", "South Park", "wolfitdm_audio/pokerfacecm.mp3", "Unknown", "Unknown")