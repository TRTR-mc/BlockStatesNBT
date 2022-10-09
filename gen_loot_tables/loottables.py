import os
from pathlib import Path
import json
import ast
import copy
import itertools


PATH = Path(os.path.dirname(__file__))
TPL: dict = json.loads((PATH / 'data/template.json').read_text())
ALL_ID_D: dict = json.loads((PATH / 'data/blocktags/all.json').read_text())
BLOCKSTATES: dict = json.loads((PATH / 'data/blockstates.json').read_text())


def main():
    id_entries = [gen_dict(id) for id in ALL_ID_D['values']]
    state_entries = []
    for id in BLOCKSTATES.keys():
        if id != 'version':
            state_entries.extend(state_entry(id))

    id_entries_ = [gen_dict(id) for id in ALL_ID_D['values'] if id not in BLOCKSTATES.keys()]
    all_entries = id_entries_ + state_entries

    id_loottable = copy.deepcopy(TPL['POOLS'])
    id_loottable["pools"][0]["entries"] = id_entries
    state_loottable = copy.deepcopy(TPL['POOLS'])
    state_loottable["pools"][0]["entries"] = state_entries
    all_loottable = copy.deepcopy(TPL['POOLS'])
    all_loottable["pools"][0]["entries"] = all_entries

    (PATH / 'id.json').write_text(json.dumps(id_loottable, indent=4))
    (PATH / 'state.json').write_text(json.dumps(state_loottable, indent=4))
    (PATH / 'all.json').write_text(json.dumps(all_loottable, indent=4))

    i = input('Update?\n(Y/n):')
    if i == 'Y':
        dp_loottable_path = PATH.parent / 'BlockStatesNBT/data/blockstates_nbt/loot_tables'
        (dp_loottable_path / 'id.json').write_text(json.dumps(id_loottable, indent=4))
        (dp_loottable_path / 'state.json').write_text(json.dumps(state_loottable, indent=4))
        (dp_loottable_path / 'all.json').write_text(json.dumps(all_loottable, indent=4))


def gen_dict(mc_id: str, set_nbt=None):
    mc_id_ = mc_id.replace('minecraft:', '')
    if set_nbt is None:
        out_s = (str(TPL['ID'])).replace('%id%', mc_id).replace('%id_%', mc_id_)
    else:
        out_s = (str(TPL['STATE'])).replace('%id%', mc_id).replace('%id_%', mc_id_).replace('%state%', set_nbt)

    return ast.literal_eval(out_s)


def state_entry(mc_id):
    states_dic = BLOCKSTATES[mc_id]

    # [[("level":0), ("level":1), ("level":2)], [("waterlogged":False), ("waterlogged":True)]]
    state_l = []
    for key, val_list in zip(list(states_dic.keys()), list(states_dic.values())):
        dic_list = [(key, temp) for temp in val_list]
        state_l.append(dic_list)

    state_l += [["_"], ["_"], ["_"], ["_"], ["_"], ["_"]]
    state_p = itertools.product(state_l[0], state_l[1], state_l[2], state_l[3], state_l[4], state_l[5])

    out_l = []
    for com in state_p:
        state_ = [temp for temp in com if temp != "_"]
        state = dict(state_)

        d_str_l = []
        for k, v in state.items():
            if type(v) is str:
                d_str_l.append(str(k) + ":" + "\"" + str(v) + "\"")
            elif type(v) is int:
                d_str_l.append(str(k) + ":" + str(v))
            else:
                d_str_l.append(str(k) + ":" + str.lower(str(v)))

        set_nbt = "{" + ",".join(d_str_l) + "}"

        value = gen_dict(mc_id, set_nbt)
        value["conditions"][0]["predicate"]["block"]["state"] = state

        out_l.append(copy.deepcopy(value))
        
    return out_l


if __name__ == '__main__':
    main()
