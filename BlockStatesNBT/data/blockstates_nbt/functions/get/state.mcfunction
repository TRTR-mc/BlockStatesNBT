#> blockstates_nbt:get/state
#
# state
#
# @public

# storage初期化
data remove storage blockstates_nbt: data

# 取得
loot spawn ~ 500 ~ loot blockstates_nbt:state
data modify storage blockstates_nbt: data.state set from entity @e[type=item,y=500,distance=..3,limit=1] Item.tag.data.state
kill @e[type=item,y=500,distance=..3,limit=1]