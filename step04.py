"""
TODOアプリ
リスト: 使用
辞書: 使用
タプル: 使用
条件分岐: 使用
繰り返し: 使用
関数: 未使用
組み込みライブラリ: 使用
f文字列: 使用
enumerate: 使用
with: 使用
"""

# JSON形式の読み込み、書き込みライブラリ
import json

# タスクリスト
with open("tasks.json", "r",encoding="utf-8") as f:
    tasks = json.load(f)

# quitまたはqを入力してbreakするまで無限ループ
while True:
    # 画面表示
    print("=" * 30, "TODO", "=" * 30)
    for i, task in enumerate(tasks):
        print(i + 1, task["task"], end="")
        if task["done"]:
            print("/ 完了", end="")
        print()
    print("=" * 66)
    print("add : タスクを追加 / quit: 終了")
    print(f"1 ~ {len(tasks)} : タスクを選択")
    print("-" * 66)

    # 操作入力
    command = input(f"コマンドまたは1 ~ {len(tasks)}の数字を入力してください : ")
    if command in ("add", "a"):
        task = input("タスクを入力してください : ")
        tasks.append({"task": task, "done": False})
        with open("tasks.json", "w", encoding="utf-8") as f:
            json.dump(tasks, f)
        print("タスクを追加しました")
    elif command in ("quit", "q"):
        print("終了しました")
        break
    else:
        try:
            no = int(command)
            if 0 <= no <= len(tasks):
                print(no, "番のタスクを選択しました")
                print("done : タスクを完了 / remove: タスクを削除")
                command = input("コマンドを入力してください : ")
                if command in ("done", "d"):
                    tasks[no - 1]["done"] = True
                    with open("tasks.json", "w", encoding="utf-8") as f:
                        json.dump(tasks, f)
                    print("タスクを完了しました")
                elif command in ("remove", "r"):
                    tasks.pop(no - 1)
                    with open("tasks.json", "w", encoding="utf-8") as f:
                        json.dump(tasks, f)
                    print("タスクを削除しました")
        except ValueError:
            print("数値またはコマンドを入力してください")
