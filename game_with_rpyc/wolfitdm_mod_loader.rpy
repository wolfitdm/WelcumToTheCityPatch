init python:
    import os

    mod_loader_path = os.path.join(config.basedir, "game", "wolfitdm")

    os.makedirs(mod_loader_path, exist_ok=True)

    config.searchpath.append(mod_loader_path)