"""
STEP 10 : GUI

10-01. TkinterによるGUIアプリ開発
"""

# 組込みGUIライブラリのインポート
import tkinter

# コンソール版の関数をインポート
from sample.todo import load_tasks, add_task, done_task, remove_task

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
    task = entry.get()  # 入力値を取得する
    entry.delete(0, tkinter.END)  # 入力欄を空にする
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
