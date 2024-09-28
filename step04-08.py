"""
STEP 04 : リストと繰り返し

04-08. enumerate関数の使いかた
"""

tasks = ["日報を作成する / 完了", "メールをチェックする", "コーヒーを買ってくる"]

while True:
    # 画面表示
    print("============================== TODO ==============================")
    for i, task in enumerate(tasks):
        print(i + 1, task)
    print("==================================================================")
    # タスクの個数を得る
    n = len(tasks)
    if n > 0:
        print(f"1 ~ {n} : タスクを選択")
    print("add : タスクを追加")
    print("quit : 終了")
    print("------------------------------------------------------------------")

    # コマンド入力
    if n > 0:
        message = f"コマンド(頭文字でも可)または1 ~ {n}の数字を入力してください : "
    else:
        message = "コマンド(頭文字でも可)を入力してください : "

    command = input(message)

    # コマンド処理
    if command in ["quit", "q"]:
        print("終了しました")
        break
    elif command in ["add", "a"]:
        task = input("追加するタスクを入力してください : ")
        tasks.append(task)
        print("タスクを追加しました")
    else:
        print(command, "を入力しました")

    # 空の行を出力
    print()
