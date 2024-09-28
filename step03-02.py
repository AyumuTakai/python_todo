"""
STEP 03 : 条件分岐

03-01. if-else文の使いかた
"""

# 画面表示
print("============================== TODO ==============================")
print("1 日報を作成する/ 完了")
print("2 メールをチェックする")
print("3 コーヒーを買ってくる")
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
else:
    print(command, "を入力しました")

# 空の行を出力
print()
