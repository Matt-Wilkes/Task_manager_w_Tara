def task_manager(string = None):
    if string == None:
        raise Exception("You haven't entered anything")
    elif '#TODO' not in string:
        return False
    return True