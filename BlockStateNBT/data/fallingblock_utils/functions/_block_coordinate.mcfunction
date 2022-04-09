# 視線先のairでないブロックに0-0-0-0-0をtp
tag @s add _block_coordinate
tag 0-0-0-0-0 add _block_coordinate

execute anchored eyes run tp 0-0-0-0-0 ^ ^ ^-0.1 facing ^ ^ ^-1
execute anchored eyes positioned ^ ^ ^6.4 rotated as @e[tag=_block_coordinate,distance=..13,sort=nearest,limit=2] positioned ^ ^ ^3.2 rotated as @e[tag=_block_coordinate,distance=..13,sort=nearest,limit=2] positioned ^ ^ ^1.6 rotated as @e[tag=_block_coordinate,distance=..13,sort=nearest,limit=2] positioned ^ ^ ^0.8 rotated as @e[tag=_block_coordinate,distance=..13,sort=nearest,limit=2] positioned ^ ^ ^0.4 rotated as @e[tag=_block_coordinate,distance=..13,sort=nearest,limit=2] positioned ^ ^ ^0.2 rotated as @e[tag=_block_coordinate,distance=..13,sort=nearest,limit=2] positioned ^ ^ ^0.1 rotated as @e[tag=_block_coordinate,distance=..13,sort=nearest,limit=2] positioned ^ ^ ^0.05 unless block ~ ~ ~ air align xyz run tp 0-0-0-0-0 ~ ~ ~

tag @e[tag=_block_coordinate,distance=..13,limit=2] remove _block_coordinate

execute positioned as 0-0-0-0-0 run function fallingblock_utils:get

# 後始末
execute in overworld run tp 0-0-0-0-0 0.0 0.0 0.0
advancement revoke @s only parkour:debug/_block_coordinate
scoreboard players reset @s Carrot