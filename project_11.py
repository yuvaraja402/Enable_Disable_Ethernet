import tkinter as tk
import subprocess as sub
import os

WINDOW_SIZE = "350x100"

root = tk.Tk()
root.title("Windows Adapter Toggler")
root.geometry(WINDOW_SIZE)

tk.Button(root, text="DISABLE Internet", command=lambda: sub.call('netsh interface set interface name="Ethernet" admin=DISABLED')).pack()
tk.Button(root, text="ENABLE Internet", command=lambda: sub.call('netsh interface set interface name="Ethernet" admin=ENABLED')).pack()
os.system(bashCommand)
