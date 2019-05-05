import numpy as np
from collections import Counter

def Solution(S):
    dictlist = []
    strings = S.split('\n')
    no_of_strings = len(strings)
    for i in range(0, no_of_strings):
        strings[i] = '{},'.format(i) + strings[i]
    m = np.char.split(strings, ',').tolist()
    for i in range(no_of_strings):
        dictlist.append({'duration': m[i][1], 'number': m[i][2], 'cost':None})
    sorted_dict = sorted(dictlist, key=lambda k: (k['number']))

    for i in range(0, no_of_strings):
        split_duration = (sorted_dict[i]['duration']).split(':')
        if (int(split_duration[1]) * 60 + int(split_duration[2]) < 300):
            cost = (int(split_duration[0]) * 3600 + int(split_duration[1]) * 60 + int(split_duration[2])) * 3
            sorted_dict[i].update({'cost': int(cost)})
            sorted_dict[i].update({'duration': (int(split_duration[0]) * 3600 + int(split_duration[1]) * 60 + int(split_duration[2]))})
        if (int(split_duration[1]) * 60 + int(split_duration[2]) == 300):
            cost = (int(split_duration[0]) * 3600 + int(split_duration[1]) * 60 + int(split_duration[2])) * 2.5
            sorted_dict[i].update({'cost': int(cost)})
            sorted_dict[i].update({'duration': (int(split_duration[0]) * 3600 + int(split_duration[1]) * 60 + int(split_duration[2]))})
        if (int(split_duration[1]) * 60 + int(split_duration[2]) > 300):
            cost = (int(split_duration[0]) * 3600 + int(split_duration[1]) * 60 + int(split_duration[2]) * 60) * 2.5
            sorted_dict[i].update({'cost': int(cost)})
            sorted_dict[i].update({'duration': (int(split_duration[0]) * 3600 + int(split_duration[1]) * 60 + int(split_duration[2]))})

        dictlist.append({'duration': sorted_dict[i], 'number': sorted_dict[i], 'cost':sorted_dict[i]})

    def summer(input_list, index_key):
        output_dict = {}
        for d in input_list:
            index = d[index_key]
            if index not in output_dict:
                output_dict[index] = {}
            for k, v in d.items():
                if k not in output_dict[index]:
                    output_dict[index][k] = v
                elif k != index_key:
                    output_dict[index][k] += v
        return output_dict.values()

    final_dict = summer(sorted_dict, 'number')
    dictlist = final_dict

    minimum = min(dictlist, key=lambda k: (k['duration'], k['number']))
    return minimum['cost']
