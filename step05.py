"""
TODOアプリ

関数に分割

リスト: 使用
辞書: 使用
タプル: 使用
条件分岐: 使用
繰り返し: 使用
関数: 使用
組み込みライブラリ: 使用
f文字列: 使用
enumerate: 使用
with: 使用
__main__: 使用
"""

# JSON形式の読み込み、書き込みライブラリ
import json

def load_tasks():
    """ タスクリストをファイルから読み込む """
    try:
        with open("tasks.json", "r",encoding="utf-8") as f:
            tasks = json.load(f)
    except Exception:
        return [] # エラーが発生したら空のタスクリストを返す
    return tasks

def save_tasks():
    """ タスクリストにファイルを保存 """
    with open("tasks.json", "w", encoding="utf-8") as f:
        json.dump(tasks, f)

def display_tasks():
    """ 画面表示 """
    print("=" * 30, "TODO", "=" * 30) # 上罫線
    for i, task in enumerate(tasks):
        print(i + 1, task["task"], end="")
        if task["done"]:
            print("/ 完了", end="")
        print() # 改行だけおこなう
    print("=" * 66) # 下罫線

def display_commands():
    """ コマンド一覧を表示 """
    print("add : タスクを追加 / quit: 終了")
    print(f"1 ~ {len(tasks)} : タスクを選択")
    print("-" * 66)

def main_command():
    """ メインコマンド処理 """
    command = input(f"コマンドまたは1 ~ {len(tasks)}の数字を入力してください : ")
    if command in ("add", "a"):
        task = input("タスクを入力してください : ")
        tasks.append({"task": task, "done": False})
        save_tasks()
        print("タスクを追加しました")
    elif command in ("quit", "q"):
        print("終了しました")
        return False # アプリ終了する場合はFalseを返す
    else:
        sub_command(command)
    return True # 処理を継続する場合はTrueを返す

def sub_command(command):
    """ タスクを選択してからのコマンド処理 """
    try:
        no = int(command)
        if 0 <= no <= len(tasks):
            print(no, "番のタスクを選択しました")
            print("done : タスクを完了 / remove: タスクを削除")
            command = input("コマンドを入力してください : ")
            if command in ("done", "d"):
                tasks[no - 1]["done"] = True
                save_tasks()
                print("タスクを完了しました")
            elif command in ("remove", "r"):
                tasks.pop(no - 1)
                save_tasks()
                print("タスクを削除しました")
    except ValueError:
        print("数値またはコマンドを入力してください")

if __name__ == "__main__":

    tasks = load_tasks()

    # メインループ (quitまたはqを入力してbreakするまで無限ループ)
    while True:
        # 画面表示
        display_tasks()
        display_commands()

        # 操作入力
        if not main_command():
            break