"""
STEP 04 : リストと繰り返し

04-01. リストの使いかた
"""

tasks = ["1 日報を作成する / 完了", "2 メールをチェックする", "3 コーヒーを買ってくる"]

# 画面表示
print("============================== TODO ==============================")
print(tasks[0])
print(tasks[1])
print(tasks[2])
print("==================================================================")
print("1 ~ 3 : タスクを選択")
print("add : タスクを追加")
print("quit : 終了")
print("------------------------------------------------------------------")

# コマンド入力
command = input("コマンドまたは1 ~ 3の数字を入力してください : ")

# コマンド処理
if command == "quit":
    print("終了しました")
elif command == "add":
    print("タスクを追加します")
else:
    print(command, "を入力しました")

# 空の行を出力
print()
