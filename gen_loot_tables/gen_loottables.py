import os
import pathlib
import json
import ast
import copy
import itertools


PATH = pathlib.Path(os.path.dirname(os.path.abspath(__file__)))


# 入力
all_id_path = PATH / 'data' / 'blocktags' / 'all.json'
all_id = json.loads(all_id_path.read_text())

blockstates_path = PATH / 'data' / 'blockstates.json'
blockstates_dict = json.loads(blockstates_path.read_text())


# テンプレ読み込み
templete_path = PATH / 'data' / 'template.json'
template = json.loads(templete_path.read_text())

tpl_id = template["pools"][0]["entries"][0]
tpl_state = template["pools"][0]["entries"][1]


# id表示のみの辞書リスト作成
id_dic_list = [ast.literal_eval((str(tpl_id)).replace('$', id)) for id in all_id["values"]]     # '$' → 'minecraft:...'


# blockstates表示の辞書リスト作成
block_list = list(blockstates_dict.keys())

for id in block_list:
    dic = blockstates_dict[id]
    
    # [[("level":0), ("level":1), ("level":2)], [("waterlogged":False), ("waterlogged":True)]]
    l = list()
    for key, val_list in zip(list(dic.keys()), list(dic.values())):
        dic_list = [(key, temp) for temp in val_list]
        l.append(dic_list)
    
    # stateの積和を作成
    l += [[None], [None], [None], [None], [None], [None]]
    l_p = itertools.product(l[0], l[1], l[2], l[3], l[4], l[5])

    # stateの組み合わせごとに追加
    state_dic_list = list()
    for com in l_p:
        # Noneを除去したうえで辞書にする
        d_ = [temp for temp in com if temp != None]
        d = dict(d_)
        
        # set_nbt用の文字列を生成
        d_str_l = [str(k) + ":" + "\"" + str(v) + "\"" for k, v in d.items()]
        set_nbt_tag = "{" + ",".join(d_str_l) + "}"

        # 辞書リストに追加
        value = ast.literal_eval((str(tpl_state)).replace('$', id).replace('=', set_nbt_tag))
        value["conditions"][0]["predicate"]["block"]["state"] = d
        state_dic_list.append(copy.deepcopy(value))


# 出力する辞書作成
out_id = copy.deepcopy(template)
out_id["pools"][0]["entries"] = id_dic_list

out_state = copy.deepcopy(template)
out_state["pools"][0]["entries"] = state_dic_list

# export
id_ex_path = PATH / 'id.json'
id_ex_path.write_text(json.dumps(out_id, indent=4))

state_ex_path = PATH / 'states.json'
state_ex_path.write_text(json.dumps(out_state, indent=4))