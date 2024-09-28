"""
STEP 04 : リストと繰り返し

04-04. リストへの要素の追加 appendメソッドの使いかた
"""

tasks = ["1 日報を作成する / 完了", "2 メールをチェックする", "3 コーヒーを買ってくる"]

# 画面表示
print("============================== TODO ==============================")
for task in tasks:
    print(task)
print("==================================================================")
print("1 ~ 3 : タスクを選択")
print("add : タスクを追加")
print("quit : 終了")
print("------------------------------------------------------------------")

# コマンド入力
command = input("コマンド(頭文字でも可)または1 ~ 3の数字を入力してください : ")

# コマンド処理
if command in ["quit", "q"]:
    print("終了しました")
elif command in ["add", "a"]:
    task = input("追加するタスクを入力してください : ")
    tasks.append(task)
    print("タスクを追加しました")
else:
    print(command, "を入力しました")

# 空の行を出力
print()
