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
                system('pyinstaller -w -F -i "{0}" {1}'.format(icoPath, pyFilePath))
            else:
                system('pyinstaller -F -i "{0}" {1}'.format(icoPath, pyFilePath))
        else:
            system('pyinstaller -F ' + pyFilePath)
        temp = name.split(".")
        nameOfFile = name
        name = temp[0] + ".spec"

        removeTempFiles(nameOfFile, name, batPath)
        isLoading = False
        label_loading.place_forget()
        messagebox.showinfo("success", "Конвертация завершена")
        print('Convert success!')
        resetEntries()
    else:
        messagebox.showerror("Ошибка ввода", "Ну ты как бы заполни поля")


def multiThreading():
    t = threading.Thread(target=createFile, name='Theard1')
    t.start()


def removeTempFiles(nameOfFile, name, batPath):
    shutil.rmtree("build")
    shutil.rmtree(pyFilePath[:-len(nameOfFile)] + "__pycache__")
    os.remove(name)
    shutil.move('dist/' + name[:-4] + 'exe', batPath)
    shutil.rmtree('dist')


def resetEntries():
    try:
        fillPath(entry_py, '')
        fillPath(entry_path, '')
        fillPath(entry_ico, '')
    except Exception as e:
        print(e)


def fillPath(entry, content):
    try:
        entry.configure(state="normal")
        entry.delete(0, tk.END)
        entry.insert(0, str(content))
        entry.configure(state="disabled")
        content = entry.get()
        content = content.replace('\\', '/')
        return content
    except Exception as e:
        print(e)


def pyPath():
    try:
        global pyFilePath
        pyFilePath = filedialog.askopenfilename(filetypes=(("Python File", "*.py"), ("All files", "*.*")))
        pyFilePath = fillPath(entry_py, pyFilePath)
        print('Путь к .py файлу: ' + pyFilePath)
    except Exception as e:
        print(e)


def path():
    try:
        global batPath
        batPath = filedialog.askdirectory()
        batPath = fillPath(entry_path, batPath)
        print('Путь для создания файла: ' + batPath)
    except Exception as e:
        print(e)


def ico_Path():
    try:
        global icoPath
        icoPath = filedialog.askopenfilename(filetypes=(("ярлык", "*.ico"), ("All files", "*.*")))
        icoPath = fillPath(entry_ico, icoPath)
        print(icoPath)
    except Exception as e:
        print(e)


check_frame = LabelFrame(root, width=990, height=50, relief=FLAT)
check_frame.pack()

ico = Checkbutton(check_frame, font=12, text="Установить иконку", fg='black', variable=var4)
ico.pack(side=RIGHT, padx=5)

exe = Checkbutton(check_frame, font=12, text="Скрывать консоль", fg='black', variable=var2)
exe.pack(side=LEFT, padx=5)

lib = Checkbutton(check_frame, font=12, text="Библиотеки установлены", fg='black', variable=var3)
lib.pack(side=LEFT, padx=5)

l_frame = LabelFrame(root, width=990, height=150, relief=FLAT)
l_frame.pack()

l1_frame = LabelFrame(l_frame, width=925, height=50, relief=FLAT)
l1_frame.pack(pady=5)

label_py = tk.Label(l1_frame, font=12, text="Путь к .py файлу:     ", fg='black', width=15)
label_py.pack(side=LEFT, padx=5)

button_py = tk.Button(l1_frame, text="Обзор", bg='#2E8B57', width=20, command=lambda: pyPath())
button_py.pack(side=RIGHT, padx=5)

entry_py = tk.Entry(l1_frame, font=12, width=75, state="disabled")
entry_py.pack(side=RIGHT, padx=5)

l2_frame = LabelFrame(l_frame, width=925, height=50, relief=FLAT)
l2_frame.pack(pady=5)

label_python = tk.Label(l2_frame, font=12, text="Путь для создания:", fg='black', width=15)
label_python.pack(side=LEFT, padx=5)

button_python = tk.Button(l2_frame, text="Обзор", bg='#2E8B57', width=20, command=lambda: path())
button_python.pack(side=RIGHT, padx=5)

entry_path = tk.Entry(l2_frame, font=12, width=75, state="disabled")
entry_path.pack(side=RIGHT, padx=5)

l3_frame = LabelFrame(l_frame, width=925, height=50, relief=FLAT)
l3_frame.pack(pady=5)

label_ico = tk.Label(l3_frame, font=12, text="Путь к иконке:         ", fg='black', width=15)
label_ico.pack(side=LEFT, padx=5)

button_ico = Button(l3_frame, text="Обзор", bg='#2E8B57', width=20, command=lambda: ico_Path())
button_ico.pack(side=RIGHT, padx=5)

entry_ico = tk.Entry(l3_frame, font=12, width=75, state="disabled")
entry_ico.pack(side=RIGHT, padx=5)

PS_frame = LabelFrame(root, width=990, height=50, relief=FLAT)
PS_frame.pack()

convert = tk.Button(PS_frame, text="конвертировать", bg='#2E8B57', width=110, command=lambda: multiThreading())
convert.pack()

label_1 = tk.Label(PS_frame, font=5, text="Если что-то не получается, то я не виноват, что ты даунич ))))0))",
                   fg='black')
label_1.pack()


label_loading = tk.Label(root, text="Конвертация", bg='white', fg='black', font=18)
label_loading.place(relwidth=0.2, relheight=0.2, anchor=CENTER)
label_loading.place_forget()

w = root.winfo_screenwidth() // 2 - 500
h = root.winfo_screenheight() // 2 - 150

if __name__ == "__main__":
    root.title("BanO4ka v666.228.1337")
    root.geometry("1050x220+{}+{}".format(w, h))
    root.resizable(False, False)
    root.mainloop()
