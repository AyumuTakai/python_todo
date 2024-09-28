"""
TODOアプリ

コンソール版完成

リスト: 使用
辞書: 使用
タプル: 使用
条件分岐: 使用
繰り返し: 使用
組み込みライブラリ: 使用
f文字列: 使用
enumerate: 使用
with: 使用
__main__: 使用
関数: 使用
デフォルト引数: 使用
"""

# JSON形式の読み込み、書き込みライブラリ
import json

datafile = "tasks.json"  # タスクデータファイルパス
tasks = []  # タスクリスト


def load_tasks(datafile=datafile):
    """タスクリストをファイルから読み込む

    Args:
        datafile (str, optional): ファイルパス. Defaults to datafile.

    Returns:
        list: タスクリスト
    """
    try:
        with open(datafile, "r", encoding="utf-8") as f:
            tasks = json.load(f)
    except Exception:
        return []  # エラーが発生したら空のタスクリストを返す
    return tasks


def save_tasks(tasks, datafile=datafile):
    """タスクリストをファイルに保存
    Args:
        tasks (list): タスクリスト. Defaults to tasks.
        datafile (str, optional): ファイルパス. Defaults to datafile.
    """
    with open(datafile, "w", encoding="utf-8") as f:
        json.dump(tasks, f)


def add_task(tasks, task):
    """タスクの追加と保存

    Args:
        tasks (list): タスクリスト. Defaults to tasks.
        task (dict): 追加するタスク
    """
    tasks.append(task)
    save_tasks(tasks)


def done_task(tasks, index):
    """タスク完了処理と保存

    Args:
        tasks (list): タスクリスト. Defaults to tasks.
        index (int): タスクインデックス
    """
    tasks[index]["done"] = True
    save_tasks(tasks)


def remove_task(tasks, index):
    """タスク削除と保存

    Args:
        tasks (list): タスクリスト. Defaults to tasks.
        index (int): タスクインデックス
    """
    tasks.pop(index)
    save_tasks(tasks)


def display_tasks(tasks):
    """タスク一覧をコンソールに表示

    Args:
        tasks (list, optional): タスクリスト. Defaults to tasks.
    """
    print("=" * 30, "TODO", "=" * 30)  # 上罫線
    for i, task in enumerate(tasks):
        print(i + 1, task["task"], end="")
        if task["done"]:
            print("/ 完了", end="")
        print()  # 改行だけおこなう
    print("=" * 66)  # 下罫線


def display_commands(tasks):
    """コマンド一覧をコンソールに表示

    Args:
        tasks (list, optional): タスクリスト. Defaults to tasks.
    """
    print("add : タスクを追加 / quit: 終了")
    print(f"1 ~ {len(tasks)} : タスクを選択")
    print("-" * 66)


def main_command(tasks, command):
    """メインコマンド処理
    Args:
        command (str): 入力されたコマンド文字列 "add","a","quit","q"

    Returns:
        bool: 処理を継続するならTrue, 終了するならFalse
    """
    if command in ("add", "a"):
        task = input("タスクを入力してください : ")
        add_task(tasks, {"task": task, "done": False})
        print("タスクを追加しました")
    elif command in ("quit", "q"):
        print("終了しました")
        return False  # プログラムを終了する場合はFalseを返す
    else:
        sub_command(tasks, command)
    return True  # 処理を継続する場合はTrueを返す


def sub_command(tasks, command):
    """タスクを選択してからのコマンド処理

    Args:
        command (str): 入力されたコマンド文字列
    """
    try:
        no = int(command)
        if 0 <= no <= len(tasks):
            print(no, "番のタスクを選択しました")
            print("done : タスクを完了 / remove: タスクを削除")
            command = input("コマンドを入力してください : ")
            if command in ("done", "d"):
                done_task(tasks, no - 1)
                print("タスクを完了しました")
            elif command in ("remove", "r"):
                remove_task(tasks, no - 1)
                print("タスクを削除しました")
    except ValueError:
        print("数値またはコマンドを入力してください")


if __name__ == "__main__":
    # タスクリストの読み込み
    tasks = load_tasks()

    # メインループ
    while True:
        display_tasks(tasks)
        display_commands(tasks)
        command = input(f"コマンドまたは1 ~ {len(tasks)}の数字を入力してください : ")
        if not main_command(tasks, command):
            break
