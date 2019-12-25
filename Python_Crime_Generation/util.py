'''
This is a utility file that does common things.
Keep adding methods as I go
'''
import os
import json

def get_current_path():
    return os.getcwd()


def import_project_path():
    return "/Users/myfatduck/OneDrive/Programs/Databases/Databases-US_Crime"


'''
Finds all files from the root directory of the project
'''
def find_all(name):
    result = []
    for root, dirs, files in os.walk(import_project_path()):
        if name in files:
            result.append(os.path.join(root, name))

    if len(result) == 1:
        return result[0]
    else:
        return result
