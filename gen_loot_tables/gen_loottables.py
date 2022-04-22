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
ID_TPL = TEMPLATE["pools"][0]["entries"][0]
STATE_TPL = TEMPLATE["pools"][0]["entries"][1]


# replace $,@,=
def gen_dict(mc_id: str, set_nbt=None):
    mc_id_ = mc_id.replace('minecraft:', '')
    if set_nbt is None:
        out_s = (str(ID_TPL)).replace('$', mc_id).replace('@', mc_id_)
    else:
        print(set_nbt)
        out_s = (str(STATE_TPL)).replace('$', mc_id).replace('@', mc_id_).replace('=', set_nbt)

    return ast.literal_eval(out_s)


# entries for 'id.json'
id_dic_list = [gen_dict(id) for id in all_id["values"]]


# entries for 'all.json'
all_id_ = set(all_id["values"]) - set(blockstates_dict.keys())
id_dic_list_ = [gen_dict(id) for id in sorted(list(all_id_))]


# entries for 'state.json'
state_dic_list = []
for id in (list(blockstates_dict.keys())):
    dic = blockstates_dict[id]

    # [[("level":0), ("level":1), ("level":2)], [("waterlogged":False), ("waterlogged":True)]]
    state_list = []
    for key, val_list in zip(list(dic.keys()), list(dic.values())):
        dic_list = [(key, temp) for temp in val_list]
        state_list.append(dic_list)

    # iterator
    state_list += [["_"], ["_"], ["_"], ["_"], ["_"], ["_"]]
    state_list_p = itertools.product(state_list[0], state_list[1], state_list[2], state_list[3], state_list[4], state_list[5])

    # append data to the list
    for com in state_list_p:
        state_ = [temp for temp in com if temp != "_"]
        state = dict(state_)

        # generate string for set_nbt
        d_str_l = []
        for k, v in state.items():
            if type(v) is str:
                d_str_l.append(str(k) + ":" + "\"" + str(v) + "\"")
            elif type(v) is int:
                d_str_l.append(str(k) + ":" + str(v))
            else:   # bool
                d_str_l.append(str(k) + ":" + str.lower(str(v)))

        set_nbt_tag = "{" + ",".join(d_str_l) + "}"

        # append
        value = gen_dict(id, set_nbt_tag)
        value["conditions"][0]["predicate"]["block"]["state"] = state
        state_dic_list.append(copy.deepcopy(value))


# loot_tables for export
out_id = copy.deepcopy(TEMPLATE)
out_id["pools"][0]["entries"] = id_dic_list

out_state = copy.deepcopy(TEMPLATE)
out_state["pools"][0]["entries"] = state_dic_list

out_all = copy.deepcopy(TEMPLATE)
out_all["pools"][0]["entries"] = id_dic_list_ + state_dic_list


# export
(PATH / 'id.json').write_text(json.dumps(out_id, indent=4))
(PATH / 'state.json').write_text(json.dumps(out_state, indent=4))
(PATH / 'all.json').write_text(json.dumps(out_all, indent=4))


# update datapack
dp_loottable_path = PATH.parent / 'BlockStatesNBT/data/blockstates_nbt/loot_tables'
if dp_loottable_path.exists() is True:
    input = input('Would overwrite:\n BlockStatesNBT/data/blockstates_nbt/loot_tables/**\nProceed (Y/n)? ')
    if input == 'Y':
        (dp_loottable_path / 'id.json').write_text(json.dumps(out_id, indent=4))
        (dp_loottable_path / 'state.json').write_text(json.dumps(out_state, indent=4))
        (dp_loottable_path / 'all.json').write_text(json.dumps(out_all, indent=4))
