"""
STEP 01 : 辞書

06-02. 状態表示
"""

tasks = [
    {"task": "日報を作成する", "done": True},
    {"task": "メールをチェックする", "done": False},
    {"task": "コーヒーを買ってくる", "done": False},
]

while True:
    # 画面表示
    print("============================== TODO ==============================")
    for i, task in enumerate(tasks):
        if task["done"]:
            status = "/ 完了"
        else:
            status = ""
        print(i + 1, task["task"], status)
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
        tasks.append({"task": task, "done": False})
        print("タスクを追加しました")
    else:
        index = int(command) - 1
        if 0 <= index < len(tasks):
            print(index + 1, tasks[index]["task"], "を選択しました")
            print()
            print("done: タスクの完了")
            print("remove: タスクの削除")
            print("cancel: 選択のキャンセル")
            print("------------------------------------------------------------------")

            # サブコマンドの入力
            subcommand = input("コマンド(頭文字でも可)を入力してください : ")

            # サブコマンド処理
            if subcommand in ["done", "d"]:
                tasks[index]["done"] = True
            elif subcommand in ["remove", "r"]:
                tasks.pop(index)
                print("タスクを削除しました")
            # doneとremove以外は何もしないで次のループへ

        else:
            print(command, "を入力しました")

    # 空の行を出力
    print()
