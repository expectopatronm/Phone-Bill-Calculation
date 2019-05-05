import numpy as np
from collections import Counter

def Solution(S):
    dictlist = []
    count = 0
    final_string = ''
    strings = S.split('\n')
    no_of_strings = len(strings)
    for i in range(0, no_of_strings):
        strings[i] = '{},'.format(i) + strings[i]
    m = np.char.split(strings, ',').tolist()
    for i in range(no_of_strings):
        dictlist.append({'original_order': i, 'name': m[i][1], 'place': m[i][2], 'timestamp': m[i][3],'occurance_order': None})
    sorted_dict = sorted(dictlist, key=lambda k: (k['place'], k['timestamp']))
    place_list = list((Counter(x['place'] for x in sorted_dict)).keys())
    count_list = list((Counter(x['place'] for x in sorted_dict)).values())
    for i in range(0, len(place_list)):
        for j in range(0, no_of_strings):
            if(place_list[i] == sorted_dict[j]['place']):
                count+=1
                sorted_dict[j].update({'occurance_order': str(count).zfill(len(str(count_list[i])))})
            if(place_list[i] != sorted_dict[j]['place']):
                count = 0
    sorted_dict = sorted(sorted_dict, key=lambda k: (k['original_order']))
    for i in range(0, no_of_strings):
        head, sep, tail = str.partition(sorted_dict[i]['name'], '.')
        final_string = final_string + str(sorted_dict[i]['place']) + str(sorted_dict[i]['occurance_order'])+ sep + tail + '\n'
    return final_string