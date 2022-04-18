# BlockStatesNBT
マイクラ内のブロックのidやblockstateをNBTとして取得できるデータパック  
## リポジトリ内容
### BlockStatesNBTディレクトリ
データパック本体
### gen_loot_tablesディレクトリ
データパックのloottable生成用のスクリプトおよびjsonファイル
## 概要
マイクラのブロックのid(`minecraft:stone` etc..)やblockstates(`powered=false` etc..)をNBTとして取得できる。  
ストレージを介してアイテム説明文やtellraw等に組み込んだり、  
アイテムのidとNBT比較を行いたいときなどに有用