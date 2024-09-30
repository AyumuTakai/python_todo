# PythonによるTODOアプリ開発

開発実習の例題としてのTODOアプリ。

Pythonの文法を学ぶだけではなく、大掛かりな要件定義などをおこなわないカジュアルな開発の手順を例示する。

STEP09までは1日で行けるのでは。STEP10は実行を確認するだけ。

最初に完成例を実行してアプリのイメージを掴んでから実習を開始すること。

# 完成品サンプル

データファイルのパスがカレントディレクトリ基準になっているため、以下のようにカレントディレクトリを変更してから実行すること。

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


# 作成するテキストのコンセプト

実習の各ステップの前にトピックを簡単な例題で練習、動作を確認すること。

1. TODOアプリに実装するべき機能の確認
2. 必要な処理や手順へのドリルダウン
3. Pythonでの記述方法と短かいサンプルで動作確認
4. 章末でTODOアプリに学んだことを反映する

各章ごとに上記1〜4を繰り返す。

いきなりプロダクトに新しく学んだ技術を投入するのではなく、検証したうえで使用することを習慣づける。

# 環境構築

Python.code-profileをインポートすることで、開発に有用な拡張機能をまとめてインストールする。

プロファイルを分けることで別用途で作業するときに機能の競合を防ぐ。

# 進行手順

## STEP 01 出力 #############################################################################

### コンセプト

完成をイメージして仮の画面を表示する。

完成形を具体化することでこの後の作業を明確にするのと、モチベーションを上げる。

### トピック

* print関数
* 空行の出力
* コメント

## STEP 02 入力と変数 ########################################################################

### コンセプト

入力の仕方を学ぶことで、プログラムを記述している段階では確定しない値を扱うことを提示する。

そのような値をプログラムに記述するためには変数という仕組みが必要であることを理解する。

    * 未定の値を扱う
    * プログラムを読みやすくするために値に名前をつける
    * プログラムを読みやすくするために計算結果を一時保存する

早いうちから入力→処理→出力 という構成を意識し基本的な設計能力を身につける。

### トピック

* input関数
* 変数
* print関数の可変長引数

## STEP 03 条件分岐 ########################################################################

### コンセプト

入力した値によってプログラムの結果を変える方法を学ぶ。

### トピック

* if文
* if-else文
* if-elif-else文
* 比較演算子

## STEP 04 リストと繰り返し ########################################################################

### コンセプト

複数かつ可変個のデータを効率的に扱う方法を学ぶ。
効率的なプログラミングに必要な仕組みもこの段階で扱う。

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

## STEP 05 データ型と型変換 ######################################################################

### コンセプト

データ型の違い、文字列から整数への型変換を学ぶ。

### トピック

* int関数
* min < x < max
* if文のネスト
* popメソッド

## STEP 06 辞書 ################################################################################

複雑なデータ構造を辞書形式で扱うことを学ぶ。

辞書のリストとして複数個のデータをまとめて管理することを学ぶ。

### トピック

* 辞書型
* 辞書のリスト

## STEP 07 ファイル入出力 ########################################################################


### コンセプト

ファイルの入出力によってデータを永続化する方法を学ぶ。

tasks-sample.jsonをtasks.jsonとして複製して使用する。

プログラムの動作確認によってtasks.jsonの内容が変更されたり、場合によっては破壊されるため、
サンプルデータを残しておくこと重要性も学ぶ。

### トピック

* with文
* open関数
* import文
* JSON形式
* jsonパッケージ
    * json.load
    * json.dump

## STEP 08 関数 ##############################################################################

### コンセプト

複雑化したプログラムを関数という形で切り分けて、わかりやすく整理する方法を学ぶ。

### トピック

* def文
* return文
* __name__変数

## STEP 09 例外処理 ###########################################################################


### コンセプト

エラーが発生した場合に適切な例外処理をおこなうことで、プログラムが使いやすくなることを学ぶ。

### トピック

* try-catch文
* Exception

## STEP 10 Tkinter ##########################################################################

関数化することでコンソールとGUIで同じ処理を共有できることを学ぶ。

フロントエンドとビジネスロジックを分離するメリットを学ぶ。

### トピック

* tkinterパッケージ
* 関数のインポート



# 応用例

* 完了したタスクの順番を変更する
    * sortメソッド

* TODの追加、完了をしたときにファイルに日時を保存する
    * writeメソッド
    * datetimeパッケージ

* タスクの編集機能

# 検討事項

## 関数化のタイミング

もっと早い段階で関数を扱い、関数の定義をアップデートする例を追加して
関数のシグネチャを変更せずに処理内容を変えられることのメリットを紹介する

## Docstring

書き方を含めるべきか

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

jsonパッケージの代わりに自前の入出力を実装する。

入力関数、出力関数の宣言をしておけば、内部実装が変っても呼び出し側は変更する必要はないということを提示するのも良いか。

### pros

* split関数などの使用例になる

### cons

* 記述量が増える

