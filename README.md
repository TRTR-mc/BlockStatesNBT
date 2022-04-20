# BlockStatesNBT
マイクラ内のブロックのidやblockstateをNBTとして取得できるloottable  
## リポジトリ内容
- BlockStatesNBTディレクトリ 
  - loottableを含むデータパック本体
- gen_loot_tablesディレクトリ
  - loottable生成用のスクリプトおよびjsonファイル
## 概要
マイクラのブロックのid(`minecraft:stone etc..`)やblockstates(`powered=false etc..`)をNBTとして取得できる。  
ストレージを介してアイテム説明文やtellraw等に組み込んだり、アイテムのidとNBT比較を行いたいとき等に有用
## 対応バージョン
JavaEdition ver1.18.2
## 使用方法
1. 取得したいブロックの場所でこのデータパックの名前空間`blockstates_nbt`内にあるloottableを呼び出す。
2. 抽選されたアイテムのタグ`data`以下にNBTがあるので、取り出して使用する。  

アイテムタグのNBTのデータ構造は以下の通り
|項目名|      |          |  型                    |  説明 |
| ---- | ---- | ----     | ----                   | ---- |
|data  |      |          |compound                |      |
|      |id    |          |string                  |ブロックのid|
|      |id_   |          |string                  |名前空間(`minecraft:`)を省略したブロックのid|
|      |state |          |compound                |ブロックステイト|
|      |      |(name)    |string<br>int<br>boolean||

### loottable一覧
6つのloottableがあり、それぞれアイテムのタグから取得できる項目が異なる。
- `all.json` idとstate両方
- `id.json` idのみ
- `state.json` stateを持つブロックのidとstate

`all.json`よりも、`id.json`や`state.json`のほうがアイテムのエントリー数が少ない。気になる場合は使い分けるとよい。

**例**
```mcfunction
#> foo:bar
# 取得したいブロックの場所で実行する
# 実行場所のチャンクが読み込まれていること
# (100,100,100)のブロックIDおよびブロックステイトを取得
execute positioned 100 100 100 run function foo:get


#> foo:get
loot spawn ~ 500.0 ~ loot blockstates_nbt:all
data get entity @e[type=item,y=500,distance=..1,limit=1] Item.tag.data
    # {id:"minecraft:acacia_slab",id_:"acacia_slab",state:{type:"top",waterlogged:false}}
kill @e[type=item,y=500,distance=..1,limit=1]
```
```mcfunction
#> foo:bar
# (50,50,50)のブロックの"minecraft:"を省略したIDを取得
execute positioned 50 50 50 run function foo:get


#> foo:get
loot spawn ~ 500.0 ~ loot blockstates_nbt:id
data get entity @e[type=item,y=500,distance=..1,limit=1] Item.tag.data.id_
    # "magma_block"
kill @e[type=item,y=500,distance=..1,limit=1]
```