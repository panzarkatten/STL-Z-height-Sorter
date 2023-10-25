# main.py

import os
import stldim
import pprint
import collections
import shutil

def get_stl_list():
    start_path = 'STLs/' # current directory
    stl_list = []
    for path,dirs,files in os.walk(start_path):
        for filename in files:
            ext = os.path.splitext(filename)
            if ext[1] == '.stl':
                filepath = os.path.join(path, filename)
                stl_list.append({   'file' : filepath, 
                                    'type' : get_model_type(filename), 
                                    'z'    : stldim.get_z_height(filepath)
                                })

    return stl_list

def get_model_type(filename):
    if filename[:1] != '[':
        return 'main'
    
    if filename[1:2] == 'a':
        return 'accent'

    return 'other'
        
def z_value(stl):
    return stl['z']

def split_stl_list(stl_list):
    main, accent, other = [], [], []
    for stl in stl_list:
        type = stl['type']
        if type == 'main':
            main.append(stl)
        if type == 'accent':
            accent.append(stl)
        if type == 'other':
            other.append(stl)

    return [main, accent, other]

def find_split(sorted_list):
    max_gap = height = 0
    for i in range(len(sorted_list)):
        z = sorted_list[i]['z']
        pz = sorted_list[i-1]['z']

        if z - pz > max_gap:
            max_gap = z - pz
            height = z

    return height


def sort_files(stl_list, basepath):
    type_list = split_stl_list(stl_list)
    types = ['main', 'accent', 'other']
    stl_paths = {}

    for type in types:
        short = os.path.join(basepath, type, 'short')
        tall = os.path.join(basepath, type, 'tall')

        if not os.path.exists(short):
            os.makedirs(short)

        if not os.path.exists(tall):
            os.makedirs(tall)

        stl_paths[type] = {'short' : short, 'tall' : tall}

        
    for stl_list in type_list:
        split_height = find_split(stl_list)

        for stl in stl_list:
            file = stl['file']
            type = stl['type']
            z = stl['z']

            if z < split_height:
                shutil.copy(file, stl_paths[type]['short'])
            else:
                shutil.copy(file, stl_paths[type]['tall'])



if __name__ == "__main__":
    stl_list = get_stl_list()

    stl_list.sort(key=z_value)

    sort_files(stl_list, 'Sorted')

    
