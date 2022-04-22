# BlockStatesNBT
マイクラ内のブロックのidやblockstateをNBTとして取得できるloottable  
## リポジトリ内容
- BlockStatesNBTディレクトリ 
  - loottableを含むデータパック本体
- gen_loot_tablesディレクトリ
  - loottable生成用のスクリプトおよびjsonファイル
## 概要
loottableを利用して、マイクラのブロックのid(`minecraft:stone etc..`)や  
ブロックステイト(`powered=false etc..`)をNBTとして取得できます。
## 対応バージョン
Minecraft ver1.18.2
## DL方法
[右のReleases](https://github.com/TRTR-mc/BlockStatesNBT/releases)からダウンロードしてください。
## 使用方法
1. 取得したいブロックの場所でloottableを呼び出す。
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
3つのloottableがあり、それぞれアイテムのタグから取得できる項目が異なります。
- `all.json` idとstate両方
- `id.json` idのみ
- `state.json` stateを持つブロックのidとstate

`all.json`よりも、`id.json`や`state.json`のほうがアイテムのエントリー数が少ないです。

**使用例**
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
#> foo:bar_
# (50,50,50)のブロックの"minecraft:"を省略したIDを取得
execute positioned 50 50 50 run function foo:get


#> foo:get_
loot spawn ~ 500.0 ~ loot blockstates_nbt:id
data get entity @e[type=item,y=500,distance=..1,limit=1] Item.tag.data.id_
    # "magma_block"
kill @e[type=item,y=500,distance=..1,limit=1]
```

また、データパックの中にも例があります。詳しくはfunctionファイル内のコメントを参照してください。