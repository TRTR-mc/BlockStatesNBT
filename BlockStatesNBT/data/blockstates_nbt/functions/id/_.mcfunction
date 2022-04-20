#> blockstates_nbt:id/_
#
# 20ブロック以内の視線先のブロックidを実行者のタイトルに表示します
#
# @input as player
# @api

# storage初期化
data modify storage blockstates_nbt: ID set value 0

# 実行場所を設定して実行
execute if entity @s[type=player] at @s anchored eyes run function blockstates_nbt:id/set_position