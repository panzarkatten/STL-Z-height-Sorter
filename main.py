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

def find_groups(stl_list):
    divider = 0
    for stl in stl_list:
        z = stl['z']

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

    return main, accent, other


def max_gap(sorted_list):
    max_gap = 0
    height = 0
    for i in range(len(sorted_list)):
        print(f"File : {sorted_list[i]['file']}")
        z = sorted_list[i]['z']
        print(f'z : {z}')
        pz = sorted_list[i-1]['z']
        print(f'pz : {pz}')

        if z - pz > max_gap:
            max_gap = z - pz
            height = z

    return max_gap, height

        


stl_list = get_stl_list()

stl_list.sort(key=z_value)

main_stls, accent_stls, other_stls = split_stl_list(stl_list)

# pprint.pprint(main_stls)

# print(max_gap(main_stls))

gap, split_height = max_gap(main_stls)

print(split_height)

low_path = './Sorted/Main/Low/'
high_path = './Sorted/Main/High/'

if not os.path.exists(low_path):
    os.makedirs(low_path)

if not os.path.exists(high_path):
    os.makedirs(high_path)

for stl in main_stls:
    file = stl['file']
    z = stl['z']

    if z < split_height:
        shutil.copy(file, low_path)
    else:
        shutil.copy(file, high_path)
    



# print(cluster(stl_list, 10))

# pprint.pprint(stl_list)


# pprint.pprint(z_heights_sorted)
