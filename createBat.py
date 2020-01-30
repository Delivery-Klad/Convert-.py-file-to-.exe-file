import os
import time
import shutil
import threading
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
pythonPath = ""
batPath = ""
icoPath = ""
isLoading = False


def loading():
    while True:
        label_loading.config(text='loading.  ')
        time.sleep(0.5)
        label_loading.config(text='loading.. ')
        time.sleep(0.5)
        label_loading.config(text='loading...')
        time.sleep(0.5)


def createFile():
    global batPath
    global isLoading
    if len(entry_py.get()) != 0 and len(entry_path.get()) != 0 and len(entry_python.get()) != 0 and var2.get() == 0:
        if batPath[len(batPath) - 1] != '\\':
            batPath += '\\'
        if var1.get() == 0 and var2.get() == 0:
            label_loading.place(relx=0.4, rely=0.35, relwidth=0.2, relheight=0.2)
            file = open(batPath + "start.bat", "w")
            if var.get():
                file.write("echo off\n")
            file.write('"' + pythonPath + '" "' + pyFilePath + '"\n@pause')  # заполнение файла
            print("bat файл успешно создан")
            label_loading.place_forget()
            messagebox.showinfo("success", "Конвертация завершена")
            file.close()
        elif var1.get() == 1:
            batPath1 = batPath + "BanO4ka\\"
            try:
                label_loading.place(relx=0.4, rely=0.35, relwidth=0.2, relheight=0.2)
                os.mkdir(batPath1)
                file = open(batPath1 + "start.bat", "w")
                if var.get():
                    file.write("echo off\n")
                file.write('"' + pythonPath + '" "' + pyFilePath + '"\n@pause')
                file.close()
                file1 = open(batPath1 + "start.vbs", "w")
                file1.write(
                    'Set shell = WScript.CreateObject("WScript.Shell")\nshell.Run("' + batPath + 'start.bat"), 0 , True')
                file1.close()
                label_loading.place_forget()
                messagebox.showinfo("success", "Конвертация завершена")
                print('convert success')
            except Exception as e:
                print(e)
    elif var2.get() and len(entry_py.get()) != 0 and len(entry_path.get()) != 0:
        temp = pyFilePath.split("/")
        name = temp[len(temp) - 1]
        label_loading.place(relx=0.4, rely=0.35, relwidth=0.2, relheight=0.2)
        if var3.get() == 0:
            file2 = open(batPath + "install.bat", "w")  # установщик pyinstaller'a
            file2.write('pip install pyinstaller')
            file2.close()
            os.startfile(batPath + 'install.bat')
            print('sleep')
            time.sleep(50)  # ожидание установки
            print('install success')
            os.remove(batPath + "install.bat")
        file3 = open(batPath + "convert.bat", "w")  # конвертация
        file3.write('cd ' + batPath + '\npyinstaller -F ' + name)
        file3.close()
        os.startfile(batPath + 'convert.bat')
        print('sleep')
        time.sleep(15)  # ожидание конвертации
        os.remove(batPath + "convert.bat")
        shutil.rmtree(batPath + "/build")
        shutil.rmtree(batPath + "/__pycache__")
        temp = name.split(".")
        name = "/" + temp[0] + ".spec"
        os.remove(batPath + name)
        label_loading.place_forget()
        messagebox.showinfo("success", "Конвертация завершена")
        print('convert success')
    else:
        messagebox.showerror("Ошибка ввода", "Ну ты как бы заполни поля")


def multiThreading():
    t = threading.Thread(target=createFile, name='Theard1')
    t.start()
    load = threading.Thread(target=loading, name='Thread2')
    load.start()


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
    print(pyFilePath)


def pytPath():
    global pythonPath
    pythonPath = filedialog.askopenfilename(filetypes=(("Приложение", "*.exe"), ("All files", "*.*")))
    pythonPath = fillPath(entry_python, pythonPath)
    print(pythonPath)


def path():
    global batPath
    batPath = filedialog.askdirectory()
    batPath = fillPath(entry_path, batPath)
    print(batPath)


def ico_Path():
    global icoPath
    icoPath = filedialog.askopenfilename(filetypes=(("ярлык", "*.ico"), ("All files", "*.*")))
    icoPath = fillPath(entry_ico, icoPath)
    print(icoPath)


check = Checkbutton(root, font=12, text="echo off", fg='black', variable=var)
check.place(relx=0.04, rely=0.03, relwidth=0.10, relheight=0.15)

vbs = Checkbutton(root, font=12, text=".bat для запуска в фоне", fg='black', variable=var1)
vbs.place(relx=0.142, rely=0.03, relwidth=0.20, relheight=0.15)

exe = Checkbutton(root, font=12, text="конвертировать в .exe", fg='black', variable=var2)
exe.place(relx=0.362, rely=0.03, relwidth=0.19, relheight=0.15)

lib = Checkbutton(root, font=12, text="библиотеки установлены", fg='black', variable=var3)
lib.place(relx=0.552, rely=0.03, relwidth=0.25, relheight=0.15)

ico = Checkbutton(root, font=12, text="установить иконку", fg='black', variable=var4)
ico.place(relx=0.78, rely=0.03, relwidth=0.18, relheight=0.15)

label_py = tk.Label(root, font=12, text="Путь к .py файлу:", fg='black')
label_py.place(relx=0.011, rely=0.20, relwidth=0.20, relheight=0.08)

button_py = tk.Button(root, text="выбрать", bg='#2E8B57', command=lambda: pyPath())
button_py.place(relx=0.8, rely=0.20, relwidth=0.15, relheight=0.08)

entry_py = tk.Entry(root, font=12, state="disabled")
entry_py.place(relx=0.19, rely=0.20, relwidth=0.60, relheight=0.08)

label_python = tk.Label(root, font=12, text="Путь к python.exe:", fg='black')
label_python.place(relx=0.014, rely=0.3, relwidth=0.20, relheight=0.08)

button_python = tk.Button(root, text="выбрать", bg='#2E8B57', command=lambda: pytPath())
button_python.place(relx=0.8, rely=0.3, relwidth=0.15, relheight=0.08)

entry_python = tk.Entry(root, font=12, state="disabled")
entry_python.place(relx=0.19, rely=0.3, relwidth=0.60, relheight=0.08)
entry_python.configure(state="normal")
entry_python.delete(0, tk.END)
entry_python.insert(0, "опционально")
entry_python.configure(state="disabled")

label_python = tk.Label(root, font=12, text="Путь для создания:", fg='black')
label_python.place(relx=0.02, rely=0.4, relwidth=0.20, relheight=0.08)

button_python = tk.Button(root, text="выбрать", bg='#2E8B57', command=lambda: path())
button_python.place(relx=0.8, rely=0.4, relwidth=0.15, relheight=0.08)

entry_path = tk.Entry(root, font=12, state="disabled")
entry_path.place(relx=0.19, rely=0.4, relwidth=0.60, relheight=0.08)

label_ico = tk.Label(root, font=12, text="Путь к иконке:", fg='black')
label_ico.place(relx=0.001, rely=0.5, relwidth=0.20, relheight=0.08)

button_ico = tk.Button(root, text="выбрать", bg='#2E8B57', command=lambda: ico_Path())
button_ico.place(relx=0.8, rely=0.5, relwidth=0.15, relheight=0.08)

entry_ico = tk.Entry(root, font=12, state="disabled")
entry_ico.place(relx=0.19, rely=0.5, relwidth=0.60, relheight=0.08)
entry_ico.configure(state="normal")
entry_ico.delete(0, tk.END)
entry_ico.insert(0, "опционально(пока не работает)")
entry_ico.configure(state="disabled")

convert = tk.Button(root, text="конвертировать", bg='#2E8B57', command=lambda: multiThreading())
convert.place(relx=0.1, rely=0.65, relwidth=0.80, relheight=0.08)

label_1 = tk.Label(root, font=12, text="Если что-то не получается, то я не виноват, что ты даунич ))))0))",
                   fg='black')
label_1.place(relx=0.1, rely=0.82, relwidth=0.80, relheight=0.1)

label_loading = tk.Label(root, text="", bg='white', fg='black', font=18)
label_loading.place(relx=0.4, rely=0.35, relwidth=0.2, relheight=0.2)
label_loading.place_forget()

if __name__ == "__main__":
    root.title("BanO4ka v228.666.1337")
    root.geometry("1000x350")
    root.resizable(False, False)
    root.mainloop()
