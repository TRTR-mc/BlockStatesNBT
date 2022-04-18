#> blockstates_nbt:get/all
#
# id and state
#
# @public

# storage初期化
data remove storage blockstates_nbt: data

# 取得
loot spawn ~ 500 ~ loot blockstates_nbt:all
data modify storage blockstates_nbt: data set from entity @e[type=item,y=500,distance=..3,limit=1] Item.tag.data
kill @e[type=item,y=500,distance=..3,limit=1]