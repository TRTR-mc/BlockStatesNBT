#> blockstates_nbt:get/id
#
# id
#
# @public

# storage初期化
data remove storage blockstates_nbt: data

# 取得
loot spawn ~ 500 ~ loot blockstates_nbt:id
data modify storage blockstates_nbt: data.id set from entity @e[type=item,y=500,distance=..3,limit=1] Item.tag.data.id
kill @e[type=item,y=500,distance=..3,limit=1]