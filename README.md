# PythonによるTODOアプリ開発

開発実習の資料としてのTODOアプリ

## STEP 01 出力

### トピック

* print関数
* 空行の出力
* コメント

## STEP 02 入力と変数

### トピック

* input関数
* 変数
* print関数の可変長引数

## STEP 03 条件分岐

### トピック

* if文
* if-else文
* if-elif-else文
* 比較演算子

## STEP 04 リストと繰り返し

### トピック

* リストの作成
* リストの要素の取得
* in演算子
* for文
* appendメソッド
* len関数
* f文字列
* while文
* 無限ループ
* break

## STEP 05 データ型と型変換

### トピック

* int関数
* min < x < max
* if文のネスト
* popメソッド

## STEP 06 辞書

### トピック

* 辞書型
* 辞書のリスト

## STEP 07 ファイル入出力

### トピック

* with文
* open関数
* import文
* JSON形式
* jsonパッケージ
    * json.load
    * json.dump

## STEP 08 関数

### トピック

* def文
* return文
* __name__変数

## STEP 09 例外処理

### トピック

* try-catch文
* Exception

## STEP 10 Tkinter

### トピック

* tkinterパッケージ
* 関数のインポート

# 完成品サンプル

## コンソール版

```
cd sample
python todo.py
```

## GUI版
```
cd sample
python gtodo.py
```


# 検討事項

## step04-08.py

enumerate関数を使った
```python
for i, task in enumerate(tasks):
    print(i, task)
```

の代わりに

```python
for i in range(len(tasks)):
    print(i, tasks[i])
```
にするかどうか

### pros

* enumerate関数のような特殊な関数をおぼえる必要がない
* javascriptなどでも見かける書き方

### cons

* pythonicな書き方ではない

## step07-01.py,step07-02.py

jsonパッケージの代わりに自前の書式を使用する

### pros

* split関数などの使用例になる

### cons

* 記述量が増える
