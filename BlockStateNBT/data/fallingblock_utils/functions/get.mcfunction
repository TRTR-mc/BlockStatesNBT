loot spawn ~ 500 ~ loot fallingblock_utils:all
data modify storage temp: _ set from entity @e[type=item,y=500,distance=..3,limit=1] Item.tag._
kill @e[type=item,y=500,distance=..3,limit=1]

execute if data storage temp: {_:{id:"minecraft:air"}} run data remove storage temp: _

title @s times 0 20 0
title @s title ""
title @s subtitle {"nbt":"_","storage": "temp:","color": "gold"}