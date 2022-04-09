import os
import pathlib
import json


PATH = pathlib.Path(os.path.dirname(os.path.abspath(__file__)))

BOOLEAN = [False, True]
_0_1 = [0, 1]
DIT_4 = ["east", "north", "south", "west"]
DIT_6 = ["east", "north", "south", "west", "up", "down"]
AXIS = ["x", "y", "z"]


# blockstates.jsonにする辞書データの項目追加
def gen_dict(keys: list, values: list, id: set):
    s_dict = dict(zip(keys, values))
    dic = {temp: s_dict for temp in id}
    Out.update(dic)

# バニラのブロックタグのjsonファイルを参照してidリストを返す
def set_id(block_tags: set, except_id: set = set()):      # (ブロックタグ名[set], idリストに入れたくないid[set])
    ids = set()

    for f_name in block_tags:
        path = PATH / 'data' / 'blocktags' / 'vanilla' / (f_name + '.json')
        dic = json.loads(path.read_text())
        ids |= set(dic["values"])
        
    return ids.difference(except_id)

##
Out = {}

# anvil
k = ["facing"]
v = [DIT_4]
id = {"minecraft:anvil"}
gen_dict(k, v, id)

# amethysts
k = ["facing", "waterlogged"]
v = [DIT_6, BOOLEAN]
id = {"minecraft:small_amethyst_bud", "minecraft:medium_amethyst_bud", "minecraft:large_amethyst_bud", "minecraft:amethyst_cluster"}
gen_dict(k, v, id)

# bamboo
k = ["age", "leaves", "stage"]
v = [_0_1, ["large", "none", "small"], _0_1]
id = {"minecraft:bamboo"}
gen_dict(k, v, id)

# banners
k = ["rotation"]
v = [list(range(16))]
id = set_id({'banners'})
gen_dict(k, v, id)

# barrel
k = ["facing", "open"]
v = [DIT_6, BOOLEAN]
id = {"minecraft:barrel"}
gen_dict(k, v, id)

# basalts
k = ["axis"]
v = [AXIS]
id = {"minecraft:basalt", "minecraft:polished_basalt"}
gen_dict(k, v, id)

# beds
k = ["facing", "occupied", "part"]
v = [DIT_4, BOOLEAN, ["foot", "head"]]
id = set_id({"beds"})
gen_dict(k, v, id)

# beehive
k = ["facing", "honey_level"]
v = [DIT_4, [list(range(6))]]
id = {"minecraft:beehive"}
gen_dict(k, v, id)

# beetroots
k = ["age"]
v = [[list(range(4))]]
id = {"minecraft:beetroots"}
gen_dict(k, v, id)

# bell
k = ["attachment", "facing", "powered"]
v = [["ceiling", "double_wall", "floor", "single_wall"], DIT_4, BOOLEAN]
id = {"minecraft:bell"}
gen_dict(k, v, id)

# big_dripleaf
k = ["facing", "tilt", "waterlogged"]
v = [DIT_4, ["full", "none"], BOOLEAN]
id = {"minecraft:big_dripleaf"}
gen_dict(k, v, id)

# big_dripleaf_stem
k = ["facing", "waterlogged"]
v = [DIT_4, BOOLEAN]
id = {"minecraft:big_dripleaf_stem"}
gen_dict(k, v, id)

# blast_furnace
k = ["facing", "lit"]
v = [DIT_4, BOOLEAN]
id = {"minecraft:blast_furnace"}
gen_dict(k, v, id)

# bone_block
k = ["axis"]
v = AXIS
id = {"minecraft:bone_block"}
gen_dict(k, v, id)

# brewing_stand
k = ["has_bottle_0", "has_bottle_1", "has_bottle_2"]
v = [BOOLEAN, BOOLEAN, BOOLEAN]
id = {"minecraft:brewing_stand"}
gen_dict(k, v, id)

# bobble_column
k = ["drag"]
v = [BOOLEAN]
id = {"minecraft:bobble_column"}
gen_dict(k, v, id)

# buttons
k = ["face", "facing", "powered"]
v = [["ceiling", "floor", "wall"], DIT_4, BOOLEAN]
id = set_id({'buttons'})
gen_dict(k, v, id)

# cactus
k = ["age"]
v = [list(range(16))]
id = {"minecraft:cactus"}
gen_dict(k, v, id)

# cake
k = ["bites"]
v = [list(range(7))]
id = {"minecraft:cake"}
gen_dict(k, v, id)

# candle_cake
k = ["lit"]
v = [BOOLEAN]
id = set_id({'candle_cakes'})
gen_dict(k, v, id)

# campfire
k = ["facing", "lit", "signal_fire", "waterlogged"]
v = [DIT_4, BOOLEAN, BOOLEAN, BOOLEAN]
id = {"minecraft:campfire"}
gen_dict(k, v, id)

# candles
k = ["candles", "lit", "waterlogged"]
v = [list(range(1, 5)), BOOLEAN, BOOLEAN]
id = set_id({'candles'})
gen_dict(k, v, id)

# carrots
k = ["age"]
v = [list(range(8))]
id = {"minecraft:carrot"}
gen_dict(k, v, id)

# cauldron
k = ["level"]
v = [list(range(4))]
id = set_id({'cauldrons'}, {"minecraft:lava_cauldron"})
gen_dict(k, v, id)

# cave_vines
k = ["berries", "age"]
v = [BOOLEAN, list(range(26))]
id = {"minecraft:cave_vines"}
gen_dict(k, v, id)

# cave_vines_plant
k = ["berries"]
v = [BOOLEAN]
id = {"minecraft:cave_vines_plant"}
gen_dict(k, v, id)

# chain
k = ["waterlogged", "axis"]
v = [BOOLEAN, AXIS]
id = {"minecraft:chain"}
gen_dict(k, v, id)

# chests
k = ["facing", "type", "waterlogged"]
v = [DIT_4, ["left", "right", "single"], BOOLEAN]
id = {"minecraft:chest", "minecraft:trapped_chest"}
gen_dict(k, v, id)

# ender_chest
k = ["facing", "waterlogged"]
v = [DIT_4, BOOLEAN]
id = {"minecraft:ender_chest"}
gen_dict(k, v, id)

# chorus_flower
k = ["age"]
v = [list(range(6))]
id = {"minecraft:chorus_flower"}
gen_dict(k, v, id)

# chorus_plant
k = ["down", "east", "north", "south", "up", "west"]
v = [BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN]
id = {"minecraft:chrous_plant"}
gen_dict(k, v, id)

# cocoa
k = ["age", "facing"]
v = [list(range(3)), DIT_4]
id = {"minecraft:cocoa"}
gen_dict(k, v, id)

# command_block
k = ["conditional", "facing"]
v = [BOOLEAN, DIT_6]
id = {"minecraft:command_block", "minecraft:chain_command_block","minecraft:repeating_command_block"}
gen_dict(k, v, id)

# composter
k = ["level"]
v = [list(range(9))]
id = {"minecraft:composter"}
gen_dict(k, v, id)

# conduit
k = ["waterlogged"]
v = [BOOLEAN]
id = {"minecraft:conduit"}
gen_dict(k, v, id)

# coral
k = ["waterlogged"]
v = [BOOLEAN]
id = set_id({'coral_plants'})
id_ = {temp.replace('minecraft:', 'minecraft:dead_') for temp in id}
id |= id_
gen_dict(k, v, id)

# coral_fan
k = ["waterlogged"]
v = [BOOLEAN]
id = set_id({'corals'}, {'#minecraft:coral_plants'})
id_ = {temp.replace('minecraft:', 'minecraft:dead_') for temp in id}
id |= id_
gen_dict(k, v, id)

# coral_wall_fan
k = ["facing", "waterlogged"]
v = [DIT_4, BOOLEAN]
id = set_id({'corals'}, {'#minecraft:coral_plants'})
id = {temp.replace('coral', 'coral_wall') for temp in id}
id_ = {temp.replace('minecraft:', 'minecraft:dead_') for temp in id}
id |= id_
gen_dict(k, v, id)

# daylight_detector
k = ["inverted", "power"]
v = [BOOLEAN, list(range(16))]
id = {"minecraft:daylight_detector"}
gen_dict(k, v, id)

# deepslate
k = ["axis"]
v = [AXIS]
id = {"minecraft:deepslate"}
gen_dict(k, v, id)

# dispenser and dropper
k = ["facing", "triggered"]
v = [DIT_6, BOOLEAN]
id = {"minecraft:dispenser", "minecraft:dropper"}
gen_dict(k, v, id)

# doors
k = ["facing", "half", "hinge", "open", "powered"]
v = [DIT_4, ["lower", "upper"], ["left", "right"], BOOLEAN, BOOLEAN]
id = set_id({'doors' ,'wooden_doors'}, {'#minecraft:wooden_doors'})
gen_dict(k, v, id)

# end_portal_frame
k = ["eye", "facing"]
v = [BOOLEAN, DIT_4]
id = {"minecraft:end_portal_frame"}
gen_dict(k, v, id)

# end_rod
k = ["facing"]
v = [DIT_6]
id = {"minecraft:end_rod"}
gen_dict(k, v, id)

# farmland
k = ["moisture"]
v = [list(range(8))]
id = {"minecraft:farmland"}
gen_dict(k, v, id)

# fences
k = ["east", "north", "south", "waterlogged", "west"]
v = [BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN]
id = set_id({'fences' ,'wooden_fences'}, {"#minecraft:wooden_fences"})
gen_dict(k, v, id)

# fence gates
k = ["facing", "in_wall", "open", "powered"]
v = [DIT_4, BOOLEAN, BOOLEAN, BOOLEAN]
id = set_id({'fence_gates'})
gen_dict(k, v, id)

# fire
k = ["age", "east", "north", "south", "up", "wast"]
v = [list(range(16)), BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN]
id = {"minecraft:fire"}
gen_dict(k, v, id)

# flowers
k = ["half"]
v = [["lower", "upper"]]
id = set_id({'tall_flowers'})
gen_dict(k, v, id)

# frosted ice
k = ["age"]
v = [list(range(4))]
id = {"minecraft:frosted_ice"}
gen_dict(k, v, id)

# furnace
k = ["facing", "lit"]
v = [DIT_4, BOOLEAN]
id = {"minecraft:furnace"}
gen_dict(k, v, id)

# glass_panes
k = ["east", "north", "south", "waterlogged", "west"]
v = [BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN]
id = set_id({'impermeable'})
gen_dict(k, v, id)

# glazed_terracotta
k = ["facing"]
v = [DIT_4]
id = set_id({'terracotta'})
id = {temp.replace('terracotta', 'glazed_terracotta') for temp in id}
gen_dict(k, v, id)

# glow_lichen
k = ["down", "east", "north", "south", "up", "waterlogged", "west"]
v = [BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN]
id = {"minecraft:glow_lichen"}
gen_dict(k, v, id)

# grass_block mycelium podzol
k = ["snowy"]
v = [BOOLEAN]
id = {"minecraft:grass_block", "minecraft:mycelium", "minecraft:podzol"}
gen_dict(k, v, id)

# grindstone
k = ["face", "facing"]
v = [["ceiling", "floor", "wall"], DIT_4]
id = {"minecraft:grindstone"}
gen_dict(k, v, id)

# hay_block
k = ["axis"]
v = [AXIS]
id = {"minecraft:hay_block"}
gen_dict(k, v, id)

# hopper
k = ["enabled", "facing"]
v = [BOOLEAN, ["east", "north", "south", "west", "down"]]
id = {"minecraft:hopper"}
gen_dict(k, v, id)

# iron_bars
k = ["east", "north", "south", "waterlogged", "west"]
v = [BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN]
id = {"minecraft:iron_bars"}
gen_dict(k, v, id)

# jigsaw_block
k = ["orientation"]
v = [["down_east", "down_north", "down_south", "down_west", "east_up", "north_up", "south_up", "up_east", "up_north", "up_south", "up_west", "west_up"]]
id = {"minecraft:jigsaw"}
gen_dict(k, v, id)

# jack_o_lantern
k = ["facing"]
v = [DIT_4]
id = {"minecraft:jack_o_lantern"}
gen_dict(k, v, id)

# jukebox
k = ["has_record"]
v = [BOOLEAN]
id = {"minecraft:jukebox"}
gen_dict(k, v, id)

# kelp
k = ["age"]
v = [list(range(26))]
id = {"minecraft:kelp"}
gen_dict(k, v, id)

# ladder
k = ["facing", "waterlogged"]
v = [DIT_4, BOOLEAN]
id = {"minecraft:ladder"}
gen_dict(k, v, id)

# lanterns
k = ["hanging", "waterlogged"]
v = [BOOLEAN, BOOLEAN]
id = {"minecraft:lantern", "minecraft:soul_lantern"}
gen_dict(k, v, id)

# lava
k = ["level"]
v = [list(range(16))]
id = {"minecraft:lava"}
gen_dict(k, v, id)

# leaves
k = ["distance", "persistant", "waterlogged"]
v = [list(range(1, 8)), BOOLEAN, BOOLEAN]
id = set_id({'leaves'})
gen_dict(k, v, id)

# lectern
k = ["facing", "has_book", "powered"]
v = [DIT_4, BOOLEAN, BOOLEAN]
id = {"minecraft:lectern"}
gen_dict(k, v, id)

# lever
k = ["face", "facing", "powered"]
v = [["ceiling", "floor", "wall"], DIT_4, BOOLEAN]
id = {"minecraft:lever"}
gen_dict(k, v, id)

# light_block
k = ["waterlogged", "level"]
v = [BOOLEAN, list(range(16))]
id = {"minecraft:light"}
gen_dict(k, v, id)

# lightning_rod
k = ["facing", "powered"]
v = [DIT_6, BOOLEAN]
id = {"minecraft:lightning_rod"}
gen_dict(k, v, id)

# logs
k = ["axis"]
v = [AXIS]
id = set_id({'dark_oak_logs', 'oak_logs', 'acacia_logs', 'birch_logs', 'jungle_logs', 'spruce_logs', 'crimson_stems', 'warped_stems'})
gen_dict(k, v, id)

# loom
k = ["facing"]
v = [DIT_4]
id = {"minecraft:loom"}
gen_dict(k, v, id)

# melon_stem
k = ["age"]
v = [list(range(8))]
id = {"minecraft:melon_stem"}
gen_dict(k, v, id)

# attached_melon_stem
k = ["facing"]
v = [DIT_4]
id = {"minecraft:attached_melon_stem"}
gen_dict(k, v, id)

# mob_heads
k = ["rotation"]
v = [list(range(16))]
id = {"minecraft:skelton_skull", "minecraft:wither_skelton_skull", "minecraft:zombie_head", "minecraft:player_head", "minecraft:creeper_head", "minecraft:dragon_head"}
gen_dict(k, v, id)

# mob_wall_heads
k = ["facing"]
v = [DIT_4]
id = {"minecraft:skelton_wall_skull", "minecraft:wither_skelton_wall_skull", "minecraft:zombie_wall_head", "minecraft:player_wall_head", "minecraft:creeper_wall_head", "minecraft:dragon_wall_head"}
gen_dict(k, v, id)

# mushroom_blocks
k = ["down", "east", "north", "south", "up", "west"]
v = [BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN]
id = {"minecraft:brown_mushroom_block", "minecraft:red_mushroom_block", "minecraft:mushroom_stem"}
gen_dict(k, v, id)

# nether_wart
k = ["age"]
v = [list(range(4))]
id = {"minecraft:nether_wart"}
gen_dict(k, v, id)

# nether_portal
k = ["axis"]
v = [["x", "y"]]
id = {"minecraft:nether_portal"}
gen_dict(k, v, id)

# note_block
k = ["instrument", "note", "powered"]
v = [["banjo", "basedrum", "bass", "bell", "bit", "chime", "cow_bell", "didgeridoo", "flute", "guitar", "harp", "hat", "iron_xylophone", "pling", "snare", "xylophone"], list(range(25)), BOOLEAN]
id = {"minecraft:note_block"}
gen_dict(k, v, id)

# observer
k = ["facing", "powered"]
v = [DIT_6, BOOLEAN]
id = {"minecraft:observer"}
gen_dict(k, v, id)

# pistons
k = ["extended", "facing"]
v = [BOOLEAN, DIT_6]
id = {"minecraft:piston", "minecraft:sticky_piston"}
gen_dict(k, v, id)

# moving_piston
k = ["facing", "type"]
v = [DIT_6, ["normal", "stickey"]]
id = {"minecraft:moving_piston"}
gen_dict(k, v, id)

# piston_head
k = ["facing", "short", "type"]
v = [DIT_6, BOOLEAN, ["normal", "stickey"]]
id = {"minecraft:piston_head"}
gen_dict(k, v, id)

# potatoes
k = ["age"]
v = [list(range(8))]
id = {"minecraft:potatoes"}
gen_dict(k, v, id)

# pointed_dripstone
k = ["thickness", "vertical_direction", "waterlogged"]
v = [["tip_merge", "tip", "frustum", "middle", "base"], ["up", "down"], BOOLEAN]
id = {"minecraft:pointed_dripstone"}
gen_dict(k, v, id)

# pressure_plates
k = ["powered"]
v = [BOOLEAN]
id = set_id({'wooden_pressure_plates', 'stone_pressure_plates'})
gen_dict(k, v, id)

# weighted_pressure_plate
k = ["power"]
v = [list(range(16))]
id = {"minecraft:light_weighted_pressure_plate", "minecraft:heavy_weighted_pressure_plate"}
gen_dict(k, v, id)

# pumpkins
k = ["facing"]
v = [DIT_4]
id = {"minecraft:pumpkin", "minecraft:carved_pumpkin"}
gen_dict(k, v, id)

# pumpkin_stem
k = ["age"]
v = [list(range(8))]
id = {"minecraft:pumpkin_stem"}
gen_dict(k, v, id)

# attached_pumpkin_stem
k = ["facing"]
v = [DIT_4]
id = {'minecraft:attached_pumpkin_stem'}
gen_dict(k, v, id)

# purpur and quartz Pillar
k = ["axis"]
v = [AXIS]
id = {"purpur_pillar", "quartz_pillar"}
gen_dict(k, v, id)

# rail
k = ["shape", "waterlogged"]
v = [["east_west", "north_east", "north_south", "north_west", "south_east", "south_west", "ascending_east", "ascending_north", "ascending_south", "ascending_west"], BOOLEAN]
id = {"minecraft:rail"}
gen_dict(k, v, id)

# - rail
k = ["powered", "shape", "waterlogged"]
v = [BOOLEAN, ["east_west", "north_south", "ascending_east", "ascending_north", "ascending_south", "ascending_west"], BOOLEAN]
id = {"minecraft:activator_rail", "minecraft:detector_rail", "minecraft:powered_rail"}
gen_dict(k, v, id)

# redstone_comparator
k = ["facing", "mode", "powered"]
v = [DIT_4, ["compare", "subtract"], BOOLEAN]
id = {"minecraft:redstone_comparator"}
gen_dict(k, v, id)

# RS_dust
k = ["east", "north", "power", "south", "west"]
v = [["none", "side", "up"], ["none", "side", "up"], list(range(16)), ["none", "side", "up"], ["none", "side", "up"]]
id = {"minecraft:redstone_dust"}
gen_dict(k, v, id)

# RS_lamp
k = ["lit"]
v = [BOOLEAN]
id = {"minecraft:redstone_lamp"}
gen_dict(k, v, id)

# RS_ore
k = ["lit"]
v = [BOOLEAN]
id = {"minecraft:redstone_ore"}
gen_dict(k, v, id)

# RS_repeater
k = ["delay", "facing", "locked", "powered"]
v = [list(range(1, 5)), DIT_4, BOOLEAN, BOOLEAN]
id = {"minecraft:redstone_repeater"}
gen_dict(k, v, id)

# RS_torch
k = ["lit"]
v = [BOOLEAN]
id = {"minecraft:redstone_torch"}
gen_dict(k, v, id)

# RS_wall_torch
k = ["facing", "lit"]
v = [DIT_4, BOOLEAN]
id = {"minecraft:redstone_wall_torch"}
gen_dict(k, v, id)

# respawn_anchor
k = ["charges"]
v = [list(range(5))]
id = {"minecraft:respawn_anchor"}
gen_dict(k, v, id)

# saplings
k = ["stage"]
v = [list(range(2))]
id = set_id({"saplings"}, {"minecraft:azalea", "minecraft:flowering_azalea"})
gen_dict(k, v, id)

# scaffolding
k = ["bottom", "distance", "waterlogged"]
v = [BOOLEAN, list(range(8)), BOOLEAN]
id = {"minecraft:scaffolding"}
gen_dict(k, v, id)

# sea_pickle
k = ["pickles", "waterlogged"]
v = [list(range(1, 5)), BOOLEAN]
id = {"minecraft:sea_pickle"}
gen_dict(k, v, id)

# shulker_boxes
k = ["facing"]
v = [DIT_6]
id = set_id({"shulker_boxes"})
gen_dict(k, v, id)

# sign
k = ["rotation", "lit", "waterlogged"]
v = [list(range(16)), BOOLEAN, BOOLEAN]
id = set_id({"wall_signs"})
gen_dict(k, v, id)

# wall_sign
k = ["facing", "lit", "waterlogged"]
v = [DIT_4, BOOLEAN, BOOLEAN]
id = set_id({"standing_signs"})
gen_dict(k, v, id)

# slabs
k = ["type", "waterlogged"]
v = [["bottom", "top", "double"], BOOLEAN]
id = set_id({"slabs" ,"wooden_slabs"}, {"#minecraft:wooden_slabs"})
gen_dict(k, v, id)

# small_dripleaf
k = ["facing", "half", "waterloggeed"]
v = [DIT_4, ["lower", "upper"], BOOLEAN]
id = {"minecraft:small_dripleaf"}
gen_dict(k, v, id)

# smoker
k = ["facing", "lit"]
v = [DIT_4, BOOLEAN]
id = {"minecraft:smooker"}
gen_dict(k, v, id)

# snow
k = ["layers"]
v = [list(range(1, 9))]
id = {"minecraft:snow"}
gen_dict(k, v, id)

# stairs
k = ["facing", "half", "shape", "waterlogged"]
v = [DIT_4, ["bottom", "top"], ["inner_left", "inner_right", "outer_left", "outer_right", "straight"], BOOLEAN]
id = set_id({"wooden_stairs", "stairs"}, {"#wooden_stairs"})
gen_dict(k, v, id)

# stonecutter
k = ["facing"]
v = [DIT_4]
id = {"minecraft:stonecutter"}
gen_dict(k, v, id)

# structure_block
k = ["mode"]
v = [["corner", "data", "load", "save"]]
id = {"minecraft:structure_block"}
gen_dict(k, v, id)

# suger_cane
k = ["age"]
v = [list(range(16))]
id = {"minecraft:suger_cane"}
gen_dict(k, v, id)

# sweet_berry_bush
k = ["age"]
v = [list(range(4))]
id = {"minecraft:sweet_berry_bush"}
gen_dict(k, v, id)

# tall_glass and large_fern
k = ["half"]
v = [["lower", "upper"]]
id = {"minecraft:tall_glass", "minecraft:large_fern"}
gen_dict(k, v, id)

# tall_seagrass
k = ["half"]
v = [["lower", "upper"]]
id = {"minecraft:tall_seagrass"}
gen_dict(k, v, id)

# target
k = ["power"]
v = [list(range(16))]
id = {"minecraft:target"}
gen_dict(k, v, id)

# tnt
k = ["unstable"]
v = [BOOLEAN]
id = {"minecraft:tnt"}
gen_dict(k, v, id)

# torch and S_torch
k = ["facing"]
v = [DIT_4]
id = {"minecraft:torch", "minecraft:soul_torch"}
gen_dict(k, v, id)

# trapdoors
k = ["facing", "half", "open", "powered", "waterlogged"]
v = [DIT_4, ["bottom", "top"], BOOLEAN, BOOLEAN, BOOLEAN]
id = set_id({"wooden_trapdoors", "trapdoors"}, {"#minecraft:wooden_trapdoors"})
gen_dict(k, v, id)

# tripwire
k = ["attached", "disarmed", "east", "north", "powered", "south", "west"]
v = [BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN]
id = {"minecraft:tripwire"}
gen_dict(k, v, id)

# tripwire_hook
k = ["attached", "facing", "powered"]
v = [BOOLEAN, DIT_4, BOOLEAN]
id = {"minecraft:tripwire_hook"}
gen_dict(k, v, id)

# turtle_egg
k = ["eggs", "hatch"]
v = [list(range(1, 5)), list(range(3))]
id = {"minecraft:turtle_egg"}
gen_dict(k, v, id)

# twisting_vines
k = ["age"]
v = [list(range(26))]
id = {"minecraft:twisting_vines"}
gen_dict(k, v, id)

# vines
k = ["east", "north", "south", "up", "west"]
v = [BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN]
id = {"minecraft:vines"}
gen_dict(k, v, id)

# walls
k = ["east", "north", "south", "up", "waterlogged", "west"]
v = [BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN, BOOLEAN]
id = set_id({"walls"})
gen_dict(k, v, id)

# water
k = ["level"]
v = [list(range(16))]
id = {"minecraft:water"}
gen_dict(k, v, id)

# weeping_vines
k = ["age"]
v = [list(range(26))]
id = {"minecraft:weeping_vines"}
gen_dict(k, v, id)

# wheat
k = ["age"]
v = [list(range(8))]
id = {"minecraft:wheat"}
gen_dict(k, v, id)

## export
export_path = PATH / 'data' / 'blockstates.json'
export_path.write_text(json.dumps(Out, indent=4))