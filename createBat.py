import os
import time
import shutil
import psutil
import threading
from os import system
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

root = tk.Tk()
var = IntVar()
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
pyFilePath = ""
batPath = ""
icoPath = ""
isLoading = False
contain = False
var2.set(1)
var3.set(1)


def createFile():
    global batPath
    global contain
    global isLoading

    if len(entry_py.get()) != 0 and len(entry_path.get()) != 0:
        temp = pyFilePath.split("/")
        name = temp[len(temp) - 1]
        isLoading = True
        label_loading.place(relx=0.4, rely=0.35, relwidth=0.2, relheight=0.2)
        if var3.get() == 0:
            system("pip install pyinstaller")
            print('Install success')
        if var4.get() == 1 and len(entry_ico.get()) != 0:
            if var2.get() == 1:
                system('pyinstaller -w -F -i "{0}" {1}'.format(icoPath, name))
            else:
                system('pyinstaller -F -i "{0}" {1}'.format(icoPath, name))
        else:
            system('pyinstaller -F ' + name)
        temp = name.split(".")
        nameOfFile = len(name)

        shutil.rmtree("build")
        shutil.rmtree("__pycache__")
        name = temp[0] + ".spec"
        os.remove(name)
        shutil.move('dist/' + name[:-4] + 'exe', batPath)
        shutil.rmtree('dist')
        isLoading = False
        label_loading.place_forget()
        messagebox.showinfo("success", "Конвертация завершена")
        print('Convert success!')
    else:
        messagebox.showerror("Ошибка ввода", "Ну ты как бы заполни поля")


def multiThreading():
    t = threading.Thread(target=createFile, name='Theard1')
    t.start()


def fillPath(entry, content):
    entry.configure(state="normal")
    entry.delete(0, tk.END)
    entry.insert(0, str(content))
    entry.configure(state="disabled")
    content = entry.get()
    content = content.replace('\\', '/')
    return content


def pyPath():
    global pyFilePath
    pyFilePath = filedialog.askopenfilename(filetypes=(("Python File", "*.py"), ("All files", "*.*")))
    pyFilePath = fillPath(entry_py, pyFilePath)
    print('Путь к .py файлу: ' + pyFilePath)


def path():
    global batPath
    batPath = filedialog.askdirectory()
    batPath = fillPath(entry_path, batPath)
    print('Путь для создания файла: ' + batPath)


def ico_Path():
    global icoPath
    icoPath = filedialog.askopenfilename(filetypes=(("ярлык", "*.ico"), ("All files", "*.*")))
    icoPath = fillPath(entry_ico, icoPath)
    print(icoPath)


exe = Checkbutton(root, font=12, text="скрывать консоль", fg='black', variable=var2)
exe.place(relx=0.1, rely=0.03, relwidth=0.19, relheight=0.15)

lib = Checkbutton(root, font=12, text="библиотеки установлены", fg='black', variable=var3)
lib.place(relx=0.4, rely=0.03, relwidth=0.25, relheight=0.15)

ico = Checkbutton(root, font=12, text="установить иконку", fg='black', variable=var4)
ico.place(relx=0.75, rely=0.03, relwidth=0.18, relheight=0.15)

label_py = tk.Label(root, font=12, text="Путь к .py файлу:", fg='black')
label_py.place(relx=0.011, rely=0.2, relwidth=0.20, relheight=0.12)

label_python = tk.Label(root, font=12, text="Путь для создания:", fg='black')
label_python.place(relx=0.02, rely=0.35, relwidth=0.20, relheight=0.12)

label_ico = tk.Label(root, font=12, text="Путь к иконке:", fg='black')
label_ico.place(relx=0.001, rely=0.5, relwidth=0.20, relheight=0.12)

button_py = tk.Button(root, text="Обзор", bg='#2E8B57', command=lambda: pyPath())
button_py.place(relx=0.8, rely=0.20, relwidth=0.15, relheight=0.12)

button_python = tk.Button(root, text="Обзор", bg='#2E8B57', command=lambda: path())
button_python.place(relx=0.8, rely=0.35, relwidth=0.15, relheight=0.12)

button_ico = tk.Button(root, text="Обзор", bg='#2E8B57', command=lambda: ico_Path())
button_ico.place(relx=0.8, rely=0.5, relwidth=0.15, relheight=0.12)

entry_py = tk.Entry(root, font=12, state="disabled")
entry_py.place(relx=0.19, rely=0.20, relwidth=0.60, relheight=0.12)

entry_path = tk.Entry(root, font=12, state="disabled")
entry_path.place(relx=0.19, rely=0.35, relwidth=0.60, relheight=0.12)

entry_ico = tk.Entry(root, font=12, state="disabled")
entry_ico.place(relx=0.19, rely=0.5, relwidth=0.60, relheight=0.12)
entry_ico.configure(state="normal")
entry_ico.delete(0, tk.END)
entry_ico.insert(0, "опционально")
entry_ico.configure(state="disabled")

convert = tk.Button(root, text="конвертировать", bg='#2E8B57', command=lambda: multiThreading())
convert.place(relx=0.1, rely=0.65, relwidth=0.80, relheight=0.12)

label_1 = tk.Label(root, font=12, text="Если что-то не получается, то я не виноват, что ты даунич ))))0))",
                   fg='black')
label_1.place(relx=0.1, rely=0.82, relwidth=0.80, relheight=0.1)

label_loading = tk.Label(root, text="Конвертация", bg='white', fg='black', font=18)
label_loading.place(relx=0.4, rely=0.35, relwidth=0.2, relheight=0.2)
label_loading.place_forget()


if __name__ == "__main__":
    root.title("BanO4ka v666.228.1337")
    root.geometry("1000x250")
    root.resizable(False, False)
    root.mainloop()
