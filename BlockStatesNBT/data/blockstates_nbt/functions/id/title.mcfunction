#> blockstates_nbt:id/title
#
# title表示
#
# @within function blockstates_nbt:id/set_position

# id取得
loot spawn ~ 500 ~ loot blockstates_nbt:id
data modify storage blockstates_nbt: ID set from entity @e[type=item,distance=..1,y=500,limit=1] Item.tag.data.id_
kill @e[type=item,distance=..1,y=500,limit=1]

# title
title @s times 0 10 0
title @s title ""
title @s subtitle {"nbt": "ID","storage": "blockstates_nbt:","color": "gold"}