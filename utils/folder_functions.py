import os

# create absolute path for given folder
def abspath(folder):
    return os.path.abspath(folder)

def create_project_dir(abs_path):
    if not os.path.exists(abs_path):
       res = os.makedirs(abs_path)
       return True
    else: False