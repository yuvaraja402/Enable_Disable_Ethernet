import tkinter as tk
import subprocess as sub
import os

WINDOW_SIZE = "350x100"

root = tk.Tk()
root.title("Windows Adapter Toggler")
root.geometry(WINDOW_SIZE)

#to call a "disable bash file" from outside
#tk.Button(root, text="DISABLE Internet", command=lambda: sub.call("C:/Users/DYUTRON/Desktop/disable_net.bat")).pack()
#to call a "enable bash file" from outside
#tk.Button(root, text="ENABLE Internet", command=lambda: sub.call("C:/Users/DYUTRON/Desktop/enable_net.bat")).pack()

#to execute bash command right from python script
# use "bashCommand=--cmd" for example to execute without buttons/tkinter
tk.Button(root, text="DISABLE Internet", command=lambda: sub.call('netsh interface set interface name="Ethernet" admin=DISABLED')).pack()
tk.Button(root, text="ENABLE Internet", command=lambda: sub.call('netsh interface set interface name="Ethernet" admin=ENABLED')).pack()
os.system(bashCommand)
