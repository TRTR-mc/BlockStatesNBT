#> blockstates_nbt:id/set_position
#
# 視線先のブロックの位置で実行
#
# @within function
#   blockstates_nbt:id/_
#   blockstates_nbt:id/set_position

execute unless block ^ ^ ^ air run function blockstates_nbt:id/title
execute if data storage blockstates_nbt: {ID:"$init"} positioned ^ ^ ^0.1 unless block ~ ~ ~ air run function blockstates_nbt:id/title
execute if data storage blockstates_nbt: {ID:"$init"} positioned ^ ^ ^0.2 unless block ~ ~ ~ air run function blockstates_nbt:id/title
execute if data storage blockstates_nbt: {ID:"$init"} positioned ^ ^ ^0.3 unless block ~ ~ ~ air run function blockstates_nbt:id/title
execute if data storage blockstates_nbt: {ID:"$init"} positioned ^ ^ ^0.4 unless block ~ ~ ~ air run function blockstates_nbt:id/title
execute if data storage blockstates_nbt: {ID:"$init"} positioned ^ ^ ^0.5 unless block ~ ~ ~ air run function blockstates_nbt:id/title
execute if data storage blockstates_nbt: {ID:"$init"} positioned ^ ^ ^0.6 unless block ~ ~ ~ air run function blockstates_nbt:id/title
execute if data storage blockstates_nbt: {ID:"$init"} positioned ^ ^ ^0.7 unless block ~ ~ ~ air run function blockstates_nbt:id/title
execute if data storage blockstates_nbt: {ID:"$init"} positioned ^ ^ ^0.8 unless block ~ ~ ~ air run function blockstates_nbt:id/title
execute if data storage blockstates_nbt: {ID:"$init"} positioned ^ ^ ^0.9 unless block ~ ~ ~ air run function blockstates_nbt:id/title
execute if data storage blockstates_nbt: {ID:"$init"} if entity @s[distance=..20] positioned ^ ^ ^1.0 run function blockstates_nbt:id/set_position