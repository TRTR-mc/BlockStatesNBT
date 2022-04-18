# BlockStatesNBT
マイクラ内のブロックのidやblockstateをNBTとして取得できるデータパック  
## リポジトリ内容
### BlockStatesNBTディレクトリ
データパック本体
### gen_loot_tablesディレクトリ
データパックのloottable生成用のスクリプトおよびjsonファイル
## 概要
マイクラのブロックのid(`minecraft:stone etc..`)やblockstates(`powered=false etc..`)をNBTとして取得できる。  
ストレージを介してアイテム説明文やtellraw等に組み込んだり、アイテムのidとNBT比較を行いたいとき等に有用
## 対応バージョン
JavaEdition ver1.18.2
## 使用方法
### loottableを用いて取得
1. 取得したいブロックの場所でloottableを呼び出す。
2. 抽選されたアイテムのタグ`data`以下にNBTがあるので、取り出して使用する。  

取得されるNBTのデータ構造は以下の通り
|項目名|      |          |  型                    |  説明 |
| ---- | ---- | ----     | ----                   | ---- |
|data  |      |          |compound                |      |
|      |id    |          |string                  |ブロックのid|
|      |state |          |compound                |ブロックステイト|
|      |      |(key_name)|string<br>int<br>boolean||

#### loottable一覧
6つのloottableがあり、それぞれitemのタグから取得できる項目が異なる
- `all.json` idとstate両方
- `id.json` idのみ
- `state.json` stateを持つブロックのidとstate
- `all_.json` idとstate両方、ただしidからデフォルトの名前空間(`minecraft:`)が省略されている
- `id_.json` idのみ、ただしidからデフォルトの名前空間(`minecraft:`)が省略されている
- `state_.json` stateを持つブロックのidとstate、ただしidからデフォルトの名前空間(`minecraft:`)が省略されている

**例**
```mcfunction
# 取得したいブロックの場所で実行する
# 実行場所のチャンクが読み込まれていること
# (100,100,100)のブロックIDおよびブロックステイトを取得
execute positioned 100 100 100 run loot spawn ~ 500 ~ loot blockstates_nbt:all
data get entity @e[type=item,y=500,distance=..3,limit=1] Item.tag.data
    # {id:"minecraft:acacia_slab",state:{type:"top",waterlogged:false}}
kill @e[type=item,y=500,distance=..3,limit=1]
```
```mcfunction
# (50,50,50)のブロックの"minecraft:"を省略したIDを取得
execute positioned 50 50 50 run loot spawn ~ 500 ~ loot blockstates_nbt:id_
data get entity @e[type=item,y=500,distance=..3,limit=1] Item.tag.data
    # {id:"magma_block"}
kill @e[type=item,y=500,distance=..3,limit=1]
```
**補足**  
`all.json`または`all_.json`を使用すればidもstateも取得できるが、id.jsonやstate.jsonのほうがloottable内の`location_check`数が少ない。気になる場合は、idのみ、stateのみを取得したい時に使い分けるとよい。
### データパックのfunctionを利用して取得
`./BlockStatesNBT/data/blockstates_nbt/functions/get/`内にあるmcfunctionファイルを呼び出すことで、  
ストレージにNBTを取得できる。  
#### function一覧と取得可能要素
- `all.mcfunction` idとstate両方
- `id.mcfunction` idのみ
- `state.mcfunction` stateのみ
- `all_.mcfunction` idとstate両方、ただしidからデフォルトの名前空間(`minecraft:`)が省略されている
- `id_.mcfunction` idのみ、ただしidからデフォルトの名前空間(`minecraft:`)が省略されている
- `state_.mcfunction` stateのみ、ただしidからデフォルトの名前空間(`minecraft:`)が省略されている


**例**
```mcfunction
# (100,100,100)のブロックIDおよびブロックステイトを取得
execute positioned 100 100 100 run function blockstates_nbt:get/all

# blockstate_nbt: 内に取得される
data get storage blockstates_nbt: data
    # {id:"minecraft:acacia_slab",state:{type:"top",waterlogged:false}}
```