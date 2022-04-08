import json
from turtle import bgcolor


## const
BOOLEAN = [False, True]
_0_1 = [0, 1]
DIT_4 = ["east", "north", "south", "west"]
DIT_6 = ["east", "north", "south", "west", "up", "down"]
AXIS = ["x", "y", "z"]

## define functions
# blockstates.jsonにする辞書データの項目追加
def gen_dict(keys: list, values: list, id: list):
    s_dict = dict(zip(keys, values))
    for f in id:
        Out[f] = s_dict

# バニラのブロックタグを参照してidリストを返す
def set_id(block_tags: str):
    path = 'debug/vanilla/' + block_tags + '.json'
    with open(path) as f:
        dic = json.load(f)

    return dic["values"]
    

##
Out = {}

# anvil
k = ["facing"]
v = [DIT_4]
id = ["minecraft:anvil"]
gen_dict(k, v, id)

# amethysts
k = ["facing", "waterlogged"]
v = [DIT_6, BOOLEAN]
id = ["minecraft:small_amethyst_bud", "minecraft:medium_amethyst_bud", "minecraft:large_amethyst_bud", "minecraft:amethyst_cluster"]
gen_dict(k, v, id)

# bamboo
k = ["age", "leaves", "stage"]
v = [_0_1, ["large", "none", "small"], _0_1]
id = ["minecraft:bamboo"]
gen_dict(k, v, id)

# banners
k = ["rotation"]
v = [list(range(16))]
id = set_id('banners')
gen_dict(k, v, id)

# barrel
k = ["facing", "open"]
v = [DIT_6, BOOLEAN]
id = ["minecraft:barrel"]
gen_dict(k, v, id)

# basalts
k = ["axis"]
v = [AXIS]
id = ["minecraft:basalt", "minecraft:polished_basalt"]
gen_dict(k, v, id)

# beds
k = ["facing", "occupied", "part"]
v = [DIT_4, BOOLEAN, ["foot", "head"]]
id = set_id('beds')
gen_dict(k, v, id)

# beehive
k = ["facing", "honey_level"]
v = [DIT_4, [list(range(6))]]
id = ["minecraft:beehive"]
gen_dict(k, v, id)

# beetroots
k = ["age"]
v = [[list(range(4))]]
id = ["minecraft:beetroots"]
gen_dict(k, v, id)

# bell
k = ["attachment", "facing", "powered"]
v = [["ceiling", "double_wall", "floor", "single_wall"], DIT_4, BOOLEAN]
id = ["minecraft:bell"]
gen_dict(k, v, id)

# big_dripleaf
k = ["facing", "tilt", "waterlogged"]
v = [DIT_4, ["full", "none"], BOOLEAN]
id = ["minecraft:big_dripleaf"]
gen_dict(k, v, id)

# big_dripleaf_stem
k = ["facing", "waterlogged"]
v = [DIT_4, BOOLEAN]
id = ["minecraft:big_dripleaf_stem"]
gen_dict(k, v, id)

# blast_furnace
k = ["facing", "lit"]
v = [DIT_4, BOOLEAN]
id = ["minecraft:blast_furnace"]
gen_dict(k, v, id)

# bone_block
k = ["axis"]
v = AXIS
id = ["minecraft:bone_block"]
gen_dict(k, v, id)

# brewing_stand
k = ["has_bottle_0", "has_bottle_1", "has_bottle_2"]
v = [BOOLEAN, BOOLEAN, BOOLEAN]
id = ["minecraft:brewing_stand"]
gen_dict(k, v, id)

# bobble_column
k = ["drag"]
v = [BOOLEAN]
id = ["minecraft:bobble_column"]
gen_dict(k, v, id)

# buttons
k = ["face", "facing", "powered"]
v = [["ceiling", "floor", "wall"], DIT_4, BOOLEAN]
id = set_id('buttons')
gen_dict(k, v, id)

# cactus
k = ["age"]
v = [list(range(16))]
id = ["minecraft:cactus"]
gen_dict(k, v, id)

# cake
k = ["bites"]
v = [list(range(7))]
id = ["minecraft:cake"]
gen_dict(k, v, id)

# candle_cake
k = ["lit"]
v = [BOOLEAN]
id = set_id('candle_cakes')
gen_dict(k, v, id)

# campfire
k = ["facing", "lit", "signal_fire", "waterlogged"]
v = [DIT_4, BOOLEAN, BOOLEAN, BOOLEAN]
id = ["minecraft:campfire"]
gen_dict(k, v, id)

# candles
k = ["candles", "lit", "waterlogged"]
v = [list(range(1, 5)), BOOLEAN, BOOLEAN]
id = set_id('candles')
gen_dict(k, v, id)

# carrots
k = ["age"]
v = [list(range(8))]
id = ["minecraft:carrot"]
gen_dict(k, v, id)

# cauldron
k = ["level"]
v = [list(range(4))]
id = set_id('cauldrons')
id = [temp for temp in id if temp != "minecraft:lava_cauldron"]
gen_dict(k, v, id)

# cave_vines
k = ["berries", "age"]
v = [BOOLEAN, list(range(26))]
id = ["minecraft:cave_vines"]
gen_dict(k, v, id)

# cave_vines_plant
k = ["berries"]
v = [BOOLEAN]
id = ["minecraft:cave_vines_plant"]
gen_dict(k, v, id)

# chain
k = ["waterlogged", "axis"]
v = [BOOLEAN, AXIS]
id = ["minecraft:chain"]
gen_dict(k, v, id)

# chests
k = ["facing", "type", "waterlogged"]
v = [DIT_4, ["left", "right", "single"], BOOLEAN]
id = ["minecraft:chest", "minecraft:trapped_chest"]
gen_dict(k, v, id)

# ender_chest
k = ["facing", "waterlogged"]
v = [DIT_4, BOOLEAN]
id = ["minecraft:ender_chest"]
gen_dict(k, v, id)

# chorus_flower
k = ["age"]
v = [list(range(6))]
id = ["minecraft:chorus_flower"]
gen_dict(k, v, id)

# chorus_plant
k = ["down", "east", "north", "south", "up", "west"]
v = [BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN]
id = ["minecraft:chrous_plant"]
gen_dict(k, v, id)

# cocoa
k = ["age", "facing"]
v = [list(range(3)), DIT_4]
id = ["minecraft:cocoa"]
gen_dict(k, v, id)

# command_block
k = ["conditional", "facing"]
v = [BOOLEAN, DIT_6]
id = ["minecraft:command_block", "minecraft:chain_command_block","minecraft:repeating_command_block"]
gen_dict(k, v, id)

# composter
k = ["level"]
v = [list(range(9))]
id = ["minecraft:composter"]
gen_dict(k, v, id)

# conduit
k = ["waterlogged"]
v = [BOOLEAN]
id = ["minecraft:conduit"]
gen_dict(k, v, id)

# coral
k = ["waterlogged"]
v = [BOOLEAN]
id = set_id('coral_plants')
id_ = [temp.replace('minecraft:', 'minecraft:dead_') for temp in id]
id += id_
gen_dict(k, v, id)

# coral_fan
k = ["waterlogged"]
v = [BOOLEAN]
id = set_id('corals')
id = [temp for temp in id if temp != '#minecraft:coral_plants']
id_ = [temp.replace('minecraft:', 'minecraft:dead_') for temp in id]
id += id_
gen_dict(k, v, id)

# coral_wall_fan
k = ["facing", "waterlogged"]
v = [DIT_4, BOOLEAN]
id = set_id('corals')
id = [temp.replace('coral', 'coral_wall') for temp in id if temp != '#minecraft:coral_plants']
id_ = [temp.replace('minecraft:', 'minecraft:dead_') for temp in id]
id += id_
gen_dict(k, v, id)

# daylight_detector
k = ["inverted", "power"]
v = [BOOLEAN, list(range(16))]
id = ["minecraft:daylight_detector"]
gen_dict(k, v, id)

# deepslate
k = ["axis"]
v = [AXIS]
id = ["minecraft:deepslate"]
gen_dict(k, v, id)

# dispenser and dropper
k = ["facing", "triggered"]
v = [DIT_6, BOOLEAN]
id = ["minecraft:dispenser", "minecraft:dropper"]
gen_dict(k, v, id)

# doors
k = ["facing", "half", "hinge", "open", "powered"]
v = [DIT_4, ["lower", "upper"], ["left", "right"], BOOLEAN, BOOLEAN]
id = set_id('wooden_doors')
id.append("minecraft:iron_door")
gen_dict(k, v, id)

# end_portal_frame
k = ["eye", "facing"]
v = [BOOLEAN, DIT_4]
id = ["minecraft:end_portal_frame"]
gen_dict(k, v, id)

# end_rod
k = ["facing"]
v = [DIT_6]
id = ["minecraft:end_rod"]
gen_dict(k, v, id)

# farmland
k = ["moisture"]
v = [list(range(8))]
id = ["minecraft:farmland"]
gen_dict(k, v, id)

# fences
k = ["east", "north", "south", "waterlogged", "west"]
v = [BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN]
id = set_id('wooden_fences')
id.append("minecraft:nether_brick_fence")
gen_dict(k, v, id)

# fence gates
k = ["facing", "in_wall", "open", "powered"]
v = [DIT_4, BOOLEAN, BOOLEAN, BOOLEAN]
id = set_id('fence_gates')
gen_dict(k, v, id)

# fire
k = ["age", "east", "north", "south", "up", "wast"]
v = [list(range(16)), BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN]
id = ["minecraft:fire"]
gen_dict(k, v, id)

# flowers
k = ["half"]
v = [["lower", "upper"]]
id = set_id('tall_flowers')
gen_dict(k, v, id)

# frosted ice
k = ["age"]
v = [list(range(4))]
id = ["minecraft:frosted_ice"]
gen_dict(k, v, id)

# furnace
k = ["facing", "lit"]
v = [DIT_4, BOOLEAN]
id = ["minecraft:furnace"]
gen_dict(k, v, id)

# glass_panes
k = ["east", "north", "south", "waterlogged", "west"]
v = [BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN]
id = set_id('impermeable')
gen_dict(k, v, id)

# glazed_terracotta
k = ["facing"]
v = [DIT_4]
id = set_id('terracotta')
id = [temp.replace('terracotta', 'glazed_terracotta') for temp in id]
gen_dict(k, v, id)

# glow_lichen
k = ["down", "east", "north", "south", "up", "waterlogged", "west"]
v = [BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN]
id = ["minecraft:glow_lichen"]
gen_dict(k, v, id)

# grass_block mycelium podzol
k = ["snowy"]
v = [BOOLEAN]
id = ["minecraft:grass_block", "minecraft:mycelium", "minecraft:podzol"]
gen_dict(k, v, id)

# grindstone
k = ["face", "facing"]
v = [["ceiling", "floor", "wall"], DIT_4]
id = ["minecraft:grindstone"]
gen_dict(k, v, id)

# hay_block
k = ["axis"]
v = [AXIS]
id = ["minecraft:hay_block"]
gen_dict(k, v, id)

# hopper
k = ["enabled", "facing"]
v = [BOOLEAN, ["east", "north", "south", "west", "down"]]
id = ["minecraft:hopper"]
gen_dict(k, v, id)

# iron_bars
k = ["east", "north", "south", "waterlogged", "west"]
v = [BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN]
id = ["minecraft:iron_bars"]
gen_dict(k, v, id)

# jigsaw_block
k = ["orientation"]
v = [["down_east", "down_north", "down_south", "down_west", "east_up", "north_up", "south_up", "up_east", "up_north", "up_south", "up_west", "west_up"]]
id = ["minecraft:jigsaw"]
gen_dict(k, v, id)

# jack_o_lantern
k = ["facing"]
v = [DIT_4]
id = ["minecraft:jack_o_lantern"]
gen_dict(k, v, id)

# jukebox
k = ["has_record"]
v = [BOOLEAN]
id = ["minecraft:jukebox"]
gen_dict(k, v, id)

# kelp
k = ["age"]
v = [list(range(26))]
id = ["minecraft:kelp"]
gen_dict(k, v, id)

# ladder
k = ["facing", "waterlogged"]
v = [DIT_4, BOOLEAN]
id = ["minecraft:ladder"]
gen_dict(k, v, id)

# lanterns
k = ["hanging", "waterlogged"]
v = [BOOLEAN, BOOLEAN]
id = ["minecraft:lantern", "minecraft:soul_lantern"]
gen_dict(k, v, id)

# lava
k = ["level"]
v = [list(range(16))]
id = ["minecraft:lava"]
gen_dict(k, v, id)

# leaves
k = ["distance", "persistant", "waterlogged"]
v = [list(range(1, 8)), BOOLEAN, BOOLEAN]
id = set_id('leaves')
gen_dict(k, v, id)

# lectern
k = ["facing", "has_book", "powered"]
v = [DIT_4, BOOLEAN, BOOLEAN]
id = ["minecraft:lectern"]
gen_dict(k, v, id)

# lever
k = ["face", "facing", "powered"]
v = [["ceiling", "floor", "wall"], DIT_4, BOOLEAN]
id = ["minecraft:lever"]
gen_dict(k, v, id)

# light_block
k = ["waterlogged", "level"]
v = [BOOLEAN, list(range(16))]
id = ["minecraft:light"]
gen_dict(k, v, id)

# lightning_rod
k = ["facing", "powered"]
v = [DIT_6, BOOLEAN]
id = ["minecraft:lightning_rod"]
gen_dict(k, v, id)

# logs
k = ["axis"]
v = [AXIS]
id = set_id('dark_oak_logs') + set_id('oak_logs') + set_id('acacia_logs') + set_id('birch_logs') + set_id('jungle_logs') + set_id('spruce_logs') + set_id('crimson_stems') + set_id('warped_stems')
gen_dict(k, v, id)

# loom
k = ["facing"]
v = [DIT_4]
id = ["minecraft:loom"]
gen_dict(k, v, id)

# melon_stem
k = ["age"]
v = [list(range(8))]
id = ["minecraft:melon_stem"]
gen_dict(k, v, id)

# attached_melon_stem
k = ["facing"]
v = [DIT_4]
id = ["minecraft:attached_melon_stem"]
gen_dict(k, v, id)

# mob_heads
k = ["rotation"]
v = [list(range(16))]
id = ["minecraft:skelton_skull", "minecraft:wither_skelton_skull", "minecraft:zombie_head", "minecraft:player_head", "minecraft:creeper_head", "minecraft:dragon_head"]
gen_dict(k, v, id)

# mob_wall_heads
k = ["facing"]
v = [DIT_4]
id = ["minecraft:skelton_wall_skull", "minecraft:wither_skelton_wall_skull", "minecraft:zombie_wall_head", "minecraft:player_wall_head", "minecraft:creeper_wall_head", "minecraft:dragon_wall_head"]
gen_dict(k, v, id)

# mushroom_blocks
k = ["down", "east", "north", "south", "up", "west"]
v = [BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN]
id = ["minecraft:brown_mushroom_block", "minecraft:red_mushroom_block", "minecraft:mushroom_stem"]
gen_dict(k, v, id)

# nether_wart
k = ["age"]
v = [list(range(4))]
id = ["minecraft:nether_wart"]
gen_dict(k, v, id)

# nether_portal
k = ["axis"]
v = [["x", "y"]]
id = ["minecraft:nether_portal"]
gen_dict(k, v, id)

# note_block
k = ["instrument", "note", "powered"]
v = [["banjo", "basedrum", "bass", "bell", "bit", "chime", "cow_bell", "didgeridoo", "flute", "guitar", "harp", "hat", "iron_xylophone", "pling", "snare", "xylophone"], list(range(25)), BOOLEAN]
id = ["minecraft:note_block"]
gen_dict(k, v, id)

# observer
k = ["facing", "powered"]
v = [DIT_6, BOOLEAN]
id = ["minecraft:observer"]
gen_dict(k, v, id)

# pistons
k = ["extended", "facing"]
v = [BOOLEAN, DIT_6]
id = ["minecraft:piston", "minecraft:sticky_piston"]
gen_dict(k, v, id)

# moving_piston
k = ["facing", "type"]
v = [DIT_6, ["normal", "stickey"]]
id = ["minecraft:moving_piston"]
gen_dict(k, v, id)

# piston_head
k = ["facing", "short", "type"]
v = [DIT_6, BOOLEAN, ["normal", "stickey"]]
id = ["minecraft:piston_head"]
gen_dict(k, v, id)

# potatoes
k = ["age"]
v = [list(range(8))]
id = ["minecraft:potatoes"]
gen_dict(k, v, id)

# pointed_dripstone
k = ["thickness", "vertical_direction", "waterlogged"]
v = [["tip_merge", "tip", "frustum", "middle", "base"], ["up", "down"], BOOLEAN]
id = ["minecraft:pointed_dripstone"]
gen_dict(k, v, id)

# pressure_plates
k = ["powered"]
v = [BOOLEAN]
id = set_id('wooden_pressure_plates') + set_id('stone_pressure_plates')
gen_dict(k, v, id)

# weighted_pressure_plate
k = ["power"]
v = [list(range(16))]
id = ["minecraft:light_weighted_pressure_plate", "minecraft:heavy_weighted_pressure_plate"]
gen_dict(k, v, id)

# pumpkins
k = ["facing"]
v = [DIT_4]
id = ["minecraft:pumpkin", "minecraft:carved_pumpkin"]
gen_dict(k, v, id)

# pumpkin_stem
k = ["age"]
v = [list(range(8))]
id = ["minecraft:pumpkin_stem"]
gen_dict(k, v, id)

# attached_pumpkin_stem
k = ["facing"]
v = [DIT_4]
id = ['minecraft:attached_pumpkin_stem']
gen_dict(k, v, id)

# purpur and quartz Pillar
k = ["axis"]
v = [AXIS]
id = ["purpur_pillar", "quartz_pillar"]
gen_dict(k, v, id)

# rail
k = ["shape", "waterlogged"]
v = [["east_west", "north_east", "north_south", "north_west", "south_east", "south_west", "ascending_east", "ascending_north", "ascending_south", "ascending_west"], BOOLEAN]
id = ["minecraft:rail"]
gen_dict(k, v, id)

#
k = []
v = []
id = []
gen_dict(k, v, id)

#
k = []
v = []
id = []
gen_dict(k, v, id)

#
k = []
v = []
id = []
gen_dict(k, v, id)

#
k = []
v = []
id = []
gen_dict(k, v, id)

#
k = []
v = []
id = []
gen_dict(k, v, id)

#
k = []
v = []
id = []
gen_dict(k, v, id)

#
k = []
v = []
id = []
gen_dict(k, v, id)

#
k = []
v = []
id = []
gen_dict(k, v, id)

#
k = []
v = []
id = []
gen_dict(k, v, id)

#
k = []
v = []
id = []
gen_dict(k, v, id)

#
k = []
v = []
id = []
gen_dict(k, v, id)

#
k = []
v = []
id = []
gen_dict(k, v, id)

#
k = []
v = []
id = []
gen_dict(k, v, id)

#
k = []
v = []
id = []
gen_dict(k, v, id)

#
k = []
v = []
id = []
gen_dict(k, v, id)

#
k = []
v = []
id = []
gen_dict(k, v, id)

#
k = []
v = []
id = []
gen_dict(k, v, id)

#
k = []
v = []
id = []
gen_dict(k, v, id)

#
k = []
v = []
id = []
gen_dict(k, v, id)

#
k = []
v = []
id = []
gen_dict(k, v, id)

#
k = []
v = []
id = []
gen_dict(k, v, id)

#
k = []
v = []
id = []
gen_dict(k, v, id)

#
k = []
v = []
id = []
gen_dict(k, v, id)

#
k = []
v = []
id = []
gen_dict(k, v, id)

#
k = []
v = []
id = []
gen_dict(k, v, id)

#
k = []
v = []
id = []
gen_dict(k, v, id)

#
k = []
v = []
id = []
gen_dict(k, v, id)

#
k = []
v = []
id = []
gen_dict(k, v, id)

## export
with open('debug/blockstates.json', 'w') as f:
    json.dump(Out, f, indent=4)