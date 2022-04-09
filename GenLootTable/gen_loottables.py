import json
import ast
import copy

# 入出力先の相対パス
InputPath = 'debug/all.json'
OutputPath = 'data/fallingblock_utils/loot_tables/all.json'

# 入力
with open(InputPath) as f:
    In = json.load(f)

# テンプレ読み込み
with open('debug/templete.json') as f:
    Templ = json.load(f)

# データ作成
def FUNC_GENERAL (id):
    Value = ast.literal_eval((str(Templ["pools"][0]["entries"][0])).replace('$', id))   # '$' → 'minecraft:...'
    return Value

List = []
for McId in In["values"]:
    Value = FUNC_GENERAL(McId)
    List.append(copy.deepcopy(Value))

# 出力する辞書作成
Out = Templ
Out["pools"][0]["entries"] = List

# jsonとして出力
with open(OutputPath, 'w') as f:
    json.dump(Out, f, indent=4)