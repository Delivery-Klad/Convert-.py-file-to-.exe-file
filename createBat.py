import sys  # для завершения работы программы


def createBatFile():
    programName = "start"  # название bat-файла
    print("\nДля выхода из программы в любой момент напишите q")
    pythonPath = input("Путь к python.exe: ")
    if pythonPath == 'q':
        sys.exit()  # завершение работы программы

    pyFilePath = input("Путь к .py файлу: ")
    if pyFilePath == 'q':
        sys.exit()  # завершение работы программы

    batPath = input("Путь для созданного bat файла или введите 0 для создания в папке проекта: ")
    if batPath == 'q':
        sys.exit()  # завершение работы программы

    if batPath == '0':  # если требуется создание bat-файла в папке проекта
        programName = ""
        batPath = ""
        temp = pyFilePath.split("\\")  # удаление названия .py файла
        str1 = temp[len(temp) - 1]  # название .py файла
        for i in range(len(pyFilePath) - len(str1)):
            batPath += pyFilePath[i]  # формирование пути
        for j in range(len(str1)-3):
            programName += str1[j]  # формирование названия bat-файла
    else:
        programName = ""
        if batPath[len(batPath)-1] != '\\':  # если в конце не стоит "\"
            batPath += '\\'  # добавить "\"
        temp = pyFilePath.split("\\")  # удаление названия .py файла
        str1 = temp[len(temp) - 1]  # название .py файла
        for j in range(len(str1) - 3):
            programName += str1[j]  # формирование названия bat-файла

    file = open(batPath + programName + ".bat", "w")  # создание bat-файла
    file.write('"' + pythonPath + '" "' + pyFilePath + '"\n@pause')  # заполнение файла
    print("bat файл успешно создан")
    file.close()  # закрытие файла


while True:
    createBatFile()
