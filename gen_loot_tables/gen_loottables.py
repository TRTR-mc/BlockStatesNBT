import os
import pathlib
import json
import ast
import copy
import itertools


PATH = pathlib.Path(os.path.dirname(os.path.abspath(__file__)))


# load files
all_id = json.loads((PATH / 'data/blocktags/all.json').read_text())

blockstates_dict = json.loads((PATH / 'data/blockstates.json').read_text())
del blockstates_dict['version']     # delete version comment


# template
TEMPLATE = json.loads((PATH / 'data/template.json').read_text())
TPL_ID = TEMPLATE["pools"][0]["entries"][0]
TPL_STATE = TEMPLATE["pools"][0]["entries"][1]


# entries for 'id.json'
id_dic_list = [ast.literal_eval((str(TPL_ID)).replace('$', id)) for id in all_id["values"]]


# entries for 'all.json'
all_id_ = set(all_id["values"]) - set(blockstates_dict.keys())
id_dic_list_ = [ast.literal_eval((str(TPL_ID)).replace('$', id)) for id in sorted(list(all_id_))]


# entries for 'state.json'
state_dic_list = []
for id in (list(blockstates_dict.keys())):
    dic = blockstates_dict[id]
    
    # [[("level":0), ("level":1), ("level":2)], [("waterlogged":False), ("waterlogged":True)]]
    l = []
    for key, val_list in zip(list(dic.keys()), list(dic.values())):
        dic_list = [(key, temp) for temp in val_list]
        l.append(dic_list)
    
    # iterator
    l += [[None], [None], [None], [None], [None], [None]]
    l_p = itertools.product(l[0], l[1], l[2], l[3], l[4], l[5])

    # append data to the list
    for com in l_p:
        d_ = [temp for temp in com if temp != None]
        d = dict(d_)
        
        # generate string for set_nbt
        d_str_l = list()
        for k, v in d.items():
            if type(v) is str:
                d_str_l.append(str(k) + ":" + "\"" + str(v) + "\"")
            elif type(v) is int:
                d_str_l.append(str(k) + ":" + str(v))
            else:   # bool
                d_str_l.append(str(k) + ":" + str.lower(str(v)))

        set_nbt_tag = "{" + ",".join(d_str_l) + "}"

        # append
        value = ast.literal_eval((str(TPL_STATE)).replace('$', id).replace('=', set_nbt_tag))
        value["conditions"][0]["predicate"]["block"]["state"] = d
        state_dic_list.append(copy.deepcopy(value))


# loot_tables for export
out_id = copy.deepcopy(TEMPLATE)
out_id["pools"][0]["entries"] = id_dic_list

out_id_ = ast.literal_eval((str(out_id)).replace('id:\"minecraft:', 'id:\"'))


out_state = copy.deepcopy(TEMPLATE)
out_state["pools"][0]["entries"] = state_dic_list

out_state_ = ast.literal_eval((str(out_state)).replace('id:\"minecraft:', 'id:\"'))


out_all = copy.deepcopy(TEMPLATE)
out_all["pools"][0]["entries"] = id_dic_list_ + state_dic_list

out_all_ = ast.literal_eval((str(out_all)).replace('id:\"minecraft:', 'id:\"'))


# export
(PATH / 'id.json').write_text(json.dumps(out_id, indent=4))
(PATH / 'id_.json').write_text(json.dumps(out_id_, indent=4))

(PATH / 'state.json').write_text(json.dumps(out_state, indent=4))
(PATH / 'state_.json').write_text(json.dumps(out_state_, indent=4))

(PATH / 'all.json').write_text(json.dumps(out_all, indent=4))
(PATH / 'all_.json').write_text(json.dumps(out_all_, indent=4))


# update datapack
dp_loottable_path = PATH.parent / 'BlockStatesNBT/data/blockstates_nbt/loot_tables'
if dp_loottable_path.exists() == True:
    input = input('Input "o" to override datapack loottables: ')
    if input == 'o':
        (dp_loottable_path /'id.json').write_text(json.dumps(out_id, indent=4))
        (dp_loottable_path /'state.json').write_text(json.dumps(out_state, indent=4))
        (dp_loottable_path /'all.json').write_text(json.dumps(out_all, indent=4))

        (dp_loottable_path /'id_.json').write_text(json.dumps(out_id_, indent=4))
        (dp_loottable_path /'state_.json').write_text(json.dumps(out_state_, indent=4))
        (dp_loottable_path /'all_.json').write_text(json.dumps(out_all_, indent=4))