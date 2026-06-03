init python:
    import os

    wolfitdm_loaded_audios = []

    import zipfile
    import urllib.request
    import shutil
    import ssl

    wolfitdm_songs_downloaded = False
    
    context = ssl._create_unverified_context()

    def wolfitdm_add_modloader_path():
        mod_loader_path = os.path.join(config.basedir, "game", "wolfitdm")

        os.makedirs(mod_loader_path, exist_ok=True)

        if not mod_loader_path in config.searchpath:
           config.searchpath.append(mod_loader_path)

    def download_file(url, dest_path, progress_callback=None):
        try:
            with urllib.request.urlopen(url, context=context) as response:
                total_size = int(response.getheader('Content-Length', 0))
                block_size = 8192
                downloaded = 0

                with open(dest_path, 'wb') as out_file:
                    while True:
                        buffer = response.read(block_size)
                        if not buffer:
                            break
                        out_file.write(buffer)
                        downloaded += len(buffer)
                        if progress_callback and total_size > 0:
                            percent = int(downloaded * 100 / total_size)
                            progress_callback(percent)
            return True
        except Exception as e:
            wolfitdm_write_log(str(e))
            return False

    def extract_zip(zip_path, extract_to):
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_to)
            return True
        except zipfile.BadZipFile:
            renpy.notify("Error: Bad ZIP file.")
            return False
        except Exception as e:
            renpy.notify(f"Extraction failed: {e}")
            return False

    def download_and_extract(url, zip_filename, extract_dir):
        if not os.path.exists(extract_dir):
            os.makedirs(extract_dir)

        zip_path = os.path.join(extract_dir, zip_filename)

        # Step 1: Download
        renpy.notify("Starting download...")
        success = download_file(url, zip_path, lambda p: renpy.notify(f"Downloading... {p}%"))
        if not success:
            renpy.notify("Download failed")
            return False

        # Step 2: Extract
        renpy.notify("Extracting files...")
        if extract_zip(zip_path, extract_dir):
            renpy.notify("Download & extraction complete!")
            # Optional: delete ZIP after extraction
            try:
                os.remove(zip_path)
            except:
                pass
            return True
        else:
            renpy.notify("Extraction failed.")
            return False

    def wolfitdm_supported_audios(file_path):
        for i in ["mp3"]:
            if file_path.endswith("." + i):
               return True

        return False

    def wolfitdm_add_audio(mname, martist, mpath, mdescription, mlyrics):
        test_path = mpath

        if test_path.startswith("wolfitdm_audio"):
           test_path = os.path.join(config.basedir, "game", "wolfitdm", mpath)

        if test_path.startswith("my_audio"):
           test_path = os.path.join(config.basedir, "game", "wolfitdm", mpath)

        if not os.path.isfile(test_path):
           return

        if not wolfitdm_supported_audios(test_path):
           return

        if mpath in wolfitdm_loaded_audios:
           return

        wolfitdm_loaded_audios.append(mpath)

        wolfitdm_write_log("added voice " + mpath)

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

    def wolfitdm_add_audios():
        root_path =  os.path.join(config.basedir, "game", "wolfitdm", "my_audio")

        os.makedirs(root_path, exist_ok=True)

        wolfitdm_write_log(root_path)

        if not isinstance(root_path, str):
           return

        if not os.path.exists(root_path):
           return

        if not os.path.isdir(root_path):
           return

        for current_path, dirs, files in os.walk(root_path):
            for d in dirs:
                full_path = os.path.abspath(os.path.join(current_path, d))

                for current_path_2, dirs_2, files_2 in os.walk(full_path):
                    for f in files_2:
                        file_path = os.path.abspath(os.path.join(current_path_2, f))
                        audio_file_path = "my_audio/" + d + "/" + f
                        base_name = os.path.basename(file_path)
                        name, ext = os.path.splitext(base_name)

                        wolfitdm_write_log(audio_file_path)

                        if not wolfitdm_supported_audios(f):
                           continue

                        wolfitdm_add_audio(name, d, audio_file_path, "Unknown", "Unknown")

            for f in files:
                file_path = os.path.abspath(os.path.join(current_path, f))
                audio_file_path = "my_audio/" + f
                base_name = os.path.basename(file_path)
                name, ext = os.path.splitext(base_name)

                wolfitdm_write_log(audio_file_path)

                if not wolfitdm_supported_audios(f):
                   continue

                wolfitdm_add_audio(name, "Unknown", audio_file_path, "Unknown", "Unknown")

    def wolfitdm_add_audios_to_me():
        wolfitdm_add_modloader_path()

        audio_dir_one = os.path.join(config.basedir, "game", "wolfitdm", "wolfitdm_audio")
        audio_dir_two = os.path.join(config.basedir, "game", "wolfitdm", "my_audio")

        os.makedirs(audio_dir_one, exist_ok=True)
        os.makedirs(audio_dir_two, exist_ok=True)
        
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
        wolfitdm_add_audio("Brooke Candy - Honey Pussy!", "Brooke Candy", "wolfitdm_audio/brokecandy_honeypussy.mp3", "Unknown", "Unknown")
        wolfitdm_add_audio("Only Fire - ASMR!", "Only Fire", "wolfitdm_audio/OnlyFire_Asmr.mp3", "Unknown", "Unknown")
        wolfitdm_add_audio("Only Fire - Double Penetration", "Only Fire", "wolfitdm_audio/OnlyFire_DoublePenetration.mp3", "Unknown", "Unknown")
        wolfitdm_add_audio("Nightcore - My Humps", "Nightcore", "wolfitdm_audio/Nightcore_MyHumps.mp3", "Unknown", "Unknown")
        wolfitdm_add_audio("Brooke Candy - Nymph", "Brooke Candy", "wolfitdm_audio/Brooke_CandyNymph.mp3", "Unknown", "Unknown")
        wolfitdm_add_audio("Only Fire - Rain On Me", "Only Fire", "wolfitdm_audio/OnlyFire_RainonMe.mp3", "Unknown", "Unknown")
        wolfitdm_add_audio("Only Fire - Cruel Summer", "Only Fire", "wolfitdm_audio/OnlyFire_CruelSummer.mp3", "Unknown", "Unknown")
        wolfitdm_add_audio("Brooke Candy - Freak Like Me", "Brooke Candy", "wolfitdm_audio/BrookeCandy_FreakLikeMe.mp3", "Unknown", "Unknown")
        wolfitdm_add_audio("Brooke Candy - Cum", "Brooke Candy", "wolfitdm_audio/BrookeCandy_Cum.mp3", "Unknown", "Unknown")
        wolfitdm_add_audio("South Park Top 10 Songs", "South Park", "wolfitdm_audio/top10southpark.mp3", "Unknown", "Unknown")
        wolfitdm_add_audio("Family Guy Pop Tart", "Family Guy", "wolfitdm_audio/familyguypoptart.mp3", "Unknown", "Unknown")
        wolfitdm_add_audio("Family Guy Harmony", "Family Guy", "wolfitdm_audio/familyguyharmony.mp3", "Unknown", "Unknown")
        wolfitdm_add_audio("Avril Lavigne - Girlfriend", "Avril Lavigne", "wolfitdm_audio/AvrilLavigne_Girlfriend.mp3", "Unknown", "Unknown")
        wolfitdm_add_audio("Carly Rae Jepson - Call Me Maybe", "Carly Rae Jepson", "wolfitdm_audio/CarlyRaeJepsen_CallMeMaybe.mp3", "Unknown", "Unknown")
        wolfitdm_add_audio("Kesha - Tik Tok", "Kesha", "wolfitdm_audio/Kesha_TiKToK.mp3", "Unknown", "Unknown")
        wolfitdm_add_audio("Wake Me Up Before You Go Go", "WHAM!", "wolfitdm_audio/WakeMeUpBeforeYouGoGo.mp3", "Unknown", "Unknown")

        wolfitdm_add_audios()

    def download_wolfitdm_music():
        global wolfitdm_songs_downloaded

        if wolfitdm_songs_downloaded:
           renpy.notify("Songs already downloaded & extracted")
           wolfitdm_add_audios_to_me()
           return

        all_downloaded = download_and_extract("https://github.com/wolfitdm/WelcumToTheCityPatch/releases/download/v1.0.0/wolfitdm_welcum_audios.zip", "wolfitdm_welcum_audios.zip", os.path.join(renpy.config.gamedir, "wolfitdm"))

        if all_downloaded:
           wolfitdm_add_audios_to_me()
           wolfitdm_songs_downloaded = True

        return

    wolfitdm_add_audios_to_me()