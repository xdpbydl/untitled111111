import tkinter as tk
from tkinter import ttk, Variable
import time


def increment(*args):
    for i in range(100):
        p1["value"] = i + 1
        root.update()
        time.sleep(0.2)
        if i == 99:  # 关闭窗口
            root.destroy()
        elif i == 50:
            text.set(r'正在生成数据……')
        # time.sleep(2)


root = tk.Tk()
root.attributes("-topmost", True)  # 最前面显示
text = Variable()
text.set(r'正在生成表格……')
root.overrideredirect(1)
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
width, height = 600, 60
size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(size)

tk.Label(root, textvariable=text).grid(row=2, column=1)

# root.geometry('320x240')
p1 = ttk.Progressbar(root, length=width, cursor='spider',
                     mode="determinate",
                     orient=tk.HORIZONTAL)
p1.grid(row=1, column=1)
# btn = ttk.Button(root, text="Start", command=increment)
# btn.grid(row=1, column=0)


increment()

root.mainloop()
