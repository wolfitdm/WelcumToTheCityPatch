init 90000 python:
    wolfitdm_check_stat = None

    if wolfitdm_check_stat == None and callable(check_stat):
       wolfitdm_check_stat = check_stat
    
    def check_stat():
        wolfitdm_check_stat()
        update_wear_vars()
        rewrite_check_playermap_jumps()
