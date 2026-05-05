default wolfitdm_hook_labels = {}

init -100000 python:
    def wolfitdm_label_hook(labels)

        if isinstance(labels, str):
           labels = [labels]


        for i in labels:
            if not i in wolfitdm_hook_labels:
               wolfitdm_hook_labels[i] = {}
               
            if not "original" in wolfitdm_hook_labels[i]:
               wolfitdm_hook_labels[i]["original"] = i

            if not "override" in wolfitdm_hook_labels[i]:
               wolfitdm_hook_labels[i]["override"] = i + "_wolfitdm_override"

            if not i in config.label_overrides:
               config.label_overrides[i] = wolfitdm_hook_labels[i]["override"]
               store.config.label_overrides[i] = wolfitdm_hook_labels[i]["override"]

    def wolfitdm_call_original(label_name, *args, **kwargs):
        if not label_name in wolfitdm_hook_labels:
           return
        if not "original" in wolfitdm_hook_labels[label_name]:
           return
        if not "override" in wolfitdm_hook_labels[label_name]:
           return

        config.label_overrides[label_name] = wolfitdm_hook_labels[label_name]["original"]
        store.config.label_overrides[label_name] = wolfitdm_hook_labels[label_name]["original"]

        try:
            renpy.call(label_name, *args, **kwargs)
        finally:
            config.label_overrides[label_name] = wolfitdm_hook_labels[label_name]["override"]
            store.config.label_overrides[label_name] = wolfitdm_hook_labels[label_name]["override"]