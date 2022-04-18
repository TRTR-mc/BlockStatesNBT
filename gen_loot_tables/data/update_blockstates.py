import os
import pathlib
import json


DIR_PATH = pathlib.Path(os.path.dirname(os.path.abspath(__file__)))

BOOLEAN = [False, True]
DIT_4 = ["east", "north", "south", "west"]
DIT_6 = ["east", "north", "south", "west", "up", "down"]


# update
def update_dict(keys: list, values: list, id: set):
    s_dict = dict(zip(keys, values))
    dic = {k: s_dict for k in id}
    blockstates.update(dic)

    return

# refer to the block tags and return the id list
def set_id(block_tags: set, except_id: set = set()):      # (block tag name[set], exclude id[set])
    ids = set()

    for f_name in block_tags:
        path = DIR_PATH / 'blocktags/vanilla' / (f_name + '.json')
        dic = json.loads(path.read_text())
        ids |= set(dic["values"])
        
    return ids.difference(except_id)


# load
blockstates = json.loads((DIR_PATH / 'blockstates.json').read_text())

# version
blockstates.update(version = '1.18.2')

# update
#   keys:list = ["facing", "waterlogged"]
#   values:list = [DIT_4, [False, True]]
#   id:set = {"minecraft:foo"}
#   update_dict(keys, values, id)

# export
print(blockstates)
input = input('Input "o" to override blockstates.json: ')
if input == 'o':
    (DIR_PATH / 'blockstates.json').write_text(json.dumps(blockstates, indent=4))