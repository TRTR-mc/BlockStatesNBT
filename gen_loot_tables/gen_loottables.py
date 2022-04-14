import os
import pathlib
import json
import ast
import copy
import itertools


PATH = pathlib.Path(os.path.dirname(os.path.abspath(__file__)))


# Load data files
all_id_path = PATH / 'data' / 'blocktags' / 'all.json'
all_id = json.loads(all_id_path.read_text())

blockstates_path = PATH / 'data' / 'blockstates.json'
blockstates_dict = json.loads(blockstates_path.read_text())
del blockstates_dict['version']     # delete version comment


# Load template
templete_path = PATH / 'data' / 'template.json'
template = json.loads(templete_path.read_text())

tpl_id = template["pools"][0]["entries"][0]
tpl_state = template["pools"][0]["entries"][1]


# Create dict-list for 'id.json'
id_dic_list = [ast.literal_eval((str(tpl_id)).replace('$', id)) for id in all_id["values"]]


# Create dict-list for 'all.json'
all_id_ = set(all_id["values"]) - set(blockstates_dict.keys())
id_dic_list_ = [ast.literal_eval((str(tpl_id)).replace('$', id)) for id in all_id_]


# Create dict-list for 'state.json'
block_list = list(blockstates_dict.keys())

state_dic_list = list()
for id in block_list:
    dic = blockstates_dict[id]
    
    # [[("level":0), ("level":1), ("level":2)], [("waterlogged":False), ("waterlogged":True)]]
    l = list()
    for key, val_list in zip(list(dic.keys()), list(dic.values())):
        dic_list = [(key, temp) for temp in val_list]
        l.append(dic_list)
    
    # Create blockstates combination
    l += [[None], [None], [None], [None], [None], [None]]
    l_p = itertools.product(l[0], l[1], l[2], l[3], l[4], l[5])

    # Add per blockstates combination
    for com in l_p:
        # Remove None and make it a dict
        d_ = [temp for temp in com if temp != None]
        d = dict(d_)
        
        # Generate string for set_nbt
        d_str_l = list()
        for k, v in d.items():
            if type(v) is str:
                d_str_l.append(str(k) + ":" + "\"" + str(v) + "\"")
            elif type(v) is int:
                d_str_l.append(str(k) + ":" + str(v))
            else:   # bool
                d_str_l.append(str(k) + ":" + str.lower(str(v)))

        set_nbt_tag = "{" + ",".join(d_str_l) + "}"

        # Add to dict-list
        value = ast.literal_eval((str(tpl_state)).replace('$', id).replace('=', set_nbt_tag))
        value["conditions"][0]["predicate"]["block"]["state"] = d
        state_dic_list.append(copy.deepcopy(value))


# Create dictionaries for output
out_id = copy.deepcopy(template)
out_id["pools"][0]["entries"] = id_dic_list

out_state = copy.deepcopy(template)
out_state["pools"][0]["entries"] = state_dic_list

out_all = copy.deepcopy(template)
out_all["pools"][0]["entries"] = id_dic_list_ + state_dic_list


# Export
id_ex_path = PATH / 'id.json'
id_ex_path.write_text(json.dumps(out_id, indent=4))

state_ex_path = PATH / 'states.json'
state_ex_path.write_text(json.dumps(out_state, indent=4))

all_ex_path = PATH / 'all.json'
all_ex_path.write_text(json.dumps(out_all, indent=4))

# Update datapack
dp_loottable_path = PATH.parent / 'BlockStateNBT' / 'data' / 'fallingblock_utils' / 'loot_tables'
if dp_loottable_path.exists() == True:
    input = input('Input "o" to override datapack loottables: ')
    if input == 'o':
        (dp_loottable_path /'id.json').write_text(json.dumps(out_id, indent=4))
        (dp_loottable_path /'states.json').write_text(json.dumps(out_state, indent=4))
        (dp_loottable_path /'all.json').write_text(json.dumps(out_all, indent=4))