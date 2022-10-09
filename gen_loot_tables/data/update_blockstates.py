import os
from pathlib import Path
import json


DIR_PATH = Path(os.path.dirname(__file__))

BOOLEAN = [False, True]
DIT_4 = ["east", "north", "south", "west"]
DIT_6 = ["east", "north", "south", "west", "up", "down"]
XYZ = ["x", "y", "z"]


# update
def update_dict(keys: list, values: list, id: set):
    id_l = [_ if _.startswith('minecraft:') else 'minecraft:' + _ for _ in id]
    s_dict = dict(zip(keys, values))
    dic = {k: s_dict for k in id_l}
    blockstates.update(dic)

    return


# return the id list
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
blockstates.update(version='1.19')


# 1.19 update
# froglight
keys = ["axis"]
values = [XYZ]
id = {"pearlescent_froglight", "verdant_froglight", "ochre_froglight"}
update_dict(keys, values, id)

# leaves
keys = ['distance', 'persistent', 'waterlogged']
values = [list(range(1, 8)), BOOLEAN, BOOLEAN]
id = set_id({'leaves'})
update_dict(keys, values, id)

# mangrove_logs
keys = ["axis"]
values = [XYZ]
id = set_id({'mangrove_logs'})
update_dict(keys, values, id)

# mangrove_slab
keys = ["type", "waterlogged"]
values = [["bottom", "top", "double"], BOOLEAN]
id = {"mangrove_slab"}
update_dict(keys, values, id)

# mangrove_stair
keys = ["facing", "half", "shape", "waterlogged"]
values = [DIT_4, ["bottom", "top"], ["inner_left", "inner_right", "outer_left", "outer_right", "straight"], BOOLEAN]
id = {"mangrove_stairs"}
update_dict(keys, values, id)

# mangrove_fence
keys = ["east", "north", "south", "waterlogged", "west"]
values = [BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN]
id = {"mangrove_fence"}
update_dict(keys, values, id)

# mangrove_fence_gate
keys = ["facing", "in_wall", "open", "powered"]
values = [DIT_4, BOOLEAN, BOOLEAN, BOOLEAN]
id = {"mangrove_fence_gate"}
update_dict(keys, values, id)

# mangrove_plate
keys = ["powered"]
values = [BOOLEAN]
id = {"mangrove_pressure_plate"}
update_dict(keys, values, id)

# mangrove_sign
keys = ["rotation", "lit", "waterlogged"]
values = [list(range(1, 16)), BOOLEAN, BOOLEAN]
id = {"mangrove_sign", "mangrove_wall_sign"}
update_dict(keys, values, id)

# mangrove_button
keys = ["face", "facing", "powered"]
values = [["ceiling", "floor", "wall"], DIT_4, BOOLEAN]
id = {"mangrove_button"}
update_dict(keys, values, id)

# mangrove_door
keys = ["facing", "half", "hinge", "open", "powered"]
values = [DIT_4, ["lower", "upper"], ["left", "right"], BOOLEAN, BOOLEAN]
id = {"mangrove_door"}
update_dict(keys, values, id)

# mangrove_td
keys = ["facing", "half", "open", "powered", "waterlogged"]
values = [DIT_4, ["bottom", "top"], BOOLEAN, BOOLEAN, BOOLEAN]
id = {"mangrove_trapdoor"}
update_dict(keys, values, id)

# mangrove_propagule
keys = ["age", "hanging", "stage", "waterlogged"]
values = [list(range(4)), BOOLEAN, [0, 1], BOOLEAN]
id = {"mangrove_propagule"}
update_dict(keys, values, id)

# mangrove_roots
keys = ["waterlogged"]
values = [BOOLEAN]
id = {"mangrove_roots"}
update_dict(keys, values, id)

# mud_brick_slab
keys = ["type", "waterlogged"]
values = [["bottom", "top", "double"], BOOLEAN]
id = {"mud_brick_slab"}
update_dict(keys, values, id)

# mud_brick_stairs
keys = ["facing", "half", "shape", "waterlogged"]
values = [DIT_4, ["bottom", "top"], ["inner_left", "inner_right", "outer_left", "outer_right", "straight"], BOOLEAN]
id = {"mud_brick_stairs"}
update_dict(keys, values, id)

# mud_brick_wall # wall
keys = ["east", "north", "south", "waterlogged", "west", "up"]
values = [BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN]
id = {"mud_brick_wall"}
update_dict(keys, values, id)

# muddy_mangrove_roots
keys = ["axis"]
values = [XYZ]
id = {"muddy_mangrove_roots"}
update_dict(keys, values, id)

# sculk_catalyst
keys = ["bloom"]
values = [BOOLEAN]
id = {"sculk_catalyst"}
update_dict(keys, values, id)

# sculk_shrieker
keys = ["can_summon", "shrieking", "waterlogged"]
values = [BOOLEAN, BOOLEAN, BOOLEAN]
id = {"sculk_shrieker"}
update_dict(keys, values, id)

# sculk_vein
keys = ["east", "north", "south", "waterlogged", "west", "up", "down"]
values = [BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN]
id = {"sculk_vein"}

update_dict(keys, values, id)

# export
input = input('Would overwrite:\n gen_loot_tables/data/blockstates.json\nProceed (Y/n)? ')
if input == 'Y':
    (DIR_PATH / 'blockstates.json').write_text(json.dumps(blockstates, indent=4))
