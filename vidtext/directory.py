import os
import random
import string
def TempDir():
    random_dir = i = ''.join(random.choices(string.ascii_uppercase + string.digits))
    dir_path = random_dir+'/'
    directory = os.path.dirname(dir_path)
    if not os.path.exists(directory):
    	os.makedirs(directory)
    return dir_path
