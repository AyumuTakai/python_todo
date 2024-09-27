"""
TODOアプリ

TkinterによるGUI版

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

import tkinter

# JSON形式の読み込み、書き込みライブラリ
import json

datafile = "tasks.json"  # タスクデータファイルパス
tasks = []  # タスクリスト

#
# コンソール/GUI 共通関数
#


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


#
# コンソール用関数
#


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


def main_command(command):
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
        sub_command(command)
    return True  # 処理を継続する場合はTrueを返す


def sub_command(command):
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


def main():
    """コンソール用メイン関数"""
    # タスクリストの読み込み
    tasks = load_tasks()

    # メインループ
    while True:
        display_tasks()
        display_commands()
        command = input(f"コマンドまたは1 ~ {len(tasks)}の数字を入力してください : ")
        main_command(command)


#
# GUI用関数
#


def done_task_handler(frame, tasks, index):
    """タスク完了イベントハンドラ

    Args:
        frame (widget): タスクリスト表示コンテナ
        index (int): タスクインデックス
    """
    done_task(tasks, index)
    reload_tasks(frame, tasks)


def add_task_handler(entry, frame, tasks):
    """タスク追加イベントハンドラ

    Args:
        entry (widget): 新規タスク入力欄
        frame (widget): タスクリスト表示コンテナ
        tasks (list, optional): タスクリスト. Defaults to tasks.
    """
    task = entry.get()
    add_task(tasks, {"task": task, "done": False})
    reload_tasks(frame, tasks)


def remove_task_handler(frame, tasks, index):
    """タスク削除イベントハンドラ

    Args:
        frame (widget): タスクリスト表示コンテナ
        index (int): タスクインデックス
        tasks (list, optional): タスクリスト. Defaults to tasks.
    """
    remove_task(tasks, index)
    reload_tasks(frame, tasks)


def task_widget(frame, index, task):
    """タスクリストアイテムウィジェットの追加

    Args:
        frame (widget): タスクリスト表示コンテナ
        index (int): タスクインデックス
        task (dict): 追加するタスク
    """
    # 背景色
    if task["done"]:
        bg = "light green"
    else:
        bg = "silver"
    row = tkinter.Frame(frame, bg=bg)
    label = tkinter.Label(row, text=task["task"], anchor=tkinter.W, bg=bg)
    label.pack(side=tkinter.LEFT, fill=tkinter.X, expand=1)
    remove_btn = tkinter.Button(
        row,
        text="🗑️",
        foreground="#f00",
        command=lambda: remove_task_handler(frame, tasks, index),
    )
    remove_btn.pack(side=tkinter.RIGHT)
    done_btn = tkinter.Button(
        row,
        text="✓",
        command=lambda: done_task_handler(frame, tasks, index),
        bg=bg,
    )
    done_btn.pack(side=tkinter.RIGHT)
    row.pack(fill=tkinter.X, padx=5, pady=2)


def reload_tasks(frame, tasks):
    """タスク一覧の表示

    Args:
        frame (widget): タスクリスト表示コンテナ
        tasks (list): タスクリスト. Defaults to tasks.
    """

    # 現在表示しているタスクウィジェットを削除
    for widget in frame.winfo_children():
        widget.destroy()

    # タスクウィジェットの追加
    for i, task in enumerate(tasks):
        task_widget(frame, i, task)


if __name__ == "__main__":
    # タスクリストの読み込み
    tasks = load_tasks()

    # ウィンドウの設定
    root = tkinter.Tk()
    root.title("TODO")
    root.geometry("600x400")

    # タスクリストのコンテナ (スクロール非対応)
    task_container = tkinter.Frame(root, bg="gray")
    task_container.pack(padx=10, pady=5, fill=tkinter.BOTH, expand=1)

    # タスク一覧表示
    reload_tasks(task_container, tasks)

    # タスク追加コンポーネント
    input_row = tkinter.Frame(root)
    # 入力欄
    entry = tkinter.Entry(input_row)
    entry.pack(side=tkinter.LEFT, fill=tkinter.X, expand=1)
    # 追加ボタン
    add_btn = tkinter.Button(
        input_row,
        text="Add",
        # Addボタンが押されたら add_task関数を呼び出す
        command=lambda: add_task_handler(entry, task_container, tasks),
    )
    add_btn.pack(side=tkinter.RIGHT)
    input_row.pack(fill=tkinter.X, side=tkinter.BOTTOM)

    # メインループの開始
    root.mainloop()
