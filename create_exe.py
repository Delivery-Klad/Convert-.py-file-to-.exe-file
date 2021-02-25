import tkinter as tk
import re
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from os import system
from itertools import groupby

root = tk.Tk()
pyFilePath = ""
builder = "builder.py"
libraries = []


def build():
    global pyFilePath, libraries
    libraries = entry_lib.get()
    print(libraries)
    with open(builder, "w") as file:
        file.write('import sys\nfrom cx_Freeze import setup, Executable\nbase = None\n' 
                   'if sys.platform == "win32":\n\tbase = "Win32GUI"\n' 
                   'elif sys.platform == "win64":\n\tbase = "Win64GUI"\n' 
                   f'executables = [Executable("{pyFilePath}", base=base)]\n' 
                   f'packages = {libraries}\n' 
                   'options = {"build_exe": {"packages": packages, }, }\n' 
                   'setup(name="main", options=options, version="1.0", executables=executables)')
    system("python builder.py build")
    messagebox.showinfo("Success", "Build successed")


def create_exe():
    global pyFilePath, libraries
    libraries = []
    with open(pyFilePath, "r") as file:
        code = file.read()
        result = re.findall(r'((^|\n)import\s\S+)', code)
        result += re.findall(r'((^|\n)from\s\S+)', code)
        for i in result:
            temp = i[0].replace("\n", "").split(" ", 1)[1].split(".", 1)[0]
            libraries.append(temp)
        entry_lib.delete(0, tk.END)
        libraries = [el for el, _ in groupby(libraries)]
        entry_lib.insert(0, str(libraries))
        button_b.configure(state="normal")


def py_path():
    try:
        global pyFilePath
        pyFilePath = filedialog.askopenfilename(filetypes=(("Python File", "*.py"), ("All files", "*.*")))
        pyFilePath = pyFilePath.replace('\\', '/')
        print('Путь к .py файлу: ' + pyFilePath)
        create_exe()
    except Exception as e:
        print(e)


entry_lib = tk.Entry(root, width=160)
entry_lib.pack(side=TOP, pady=5)
button_py = tk.Button(root, text="Обзор", bg='#2E8B57', width=20, command=lambda: py_path())
button_py.pack(side=BOTTOM, pady=5)
button_b = tk.Button(root, text="Build", bg='#2E8B57', width=20, command=lambda: build(), state="disabled")
button_b.pack(side=BOTTOM, pady=5)
w = root.winfo_screenwidth() // 2 - 500
h = root.winfo_screenheight() // 2 - 150

if __name__ == "__main__":
    root.title("BanO4ka v666.228.1337")
    root.geometry("1000x100+{}+{}".format(w, h))
    root.resizable(False, False)
    root.mainloop()
