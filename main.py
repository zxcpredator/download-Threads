# Задача сделать так, чтобы ты вводил в инпут "download"
# И начиналось скачивание того файла, что я прикрепил ( либо любого другого ) без блокировки потока input
#
# - Всё в бесконечных циклах зациклить
# Сейчас:
#
# "download" -> 30сек ждем -> print("download")
#
# Надо:
#
# "download" ввел
# -> print("download")
# "download" опять ввел
# -> print("download")
#
# В это время грузится файл
# Если он уже начал грузиться - сделай отправку сообщения "Файл уже загружается" и НЕ начинай загрузку еще раз
#
# Когда файл загрузится - "Файл загружен" в поток вывода. И убери флаг запрета на повторную загрузку


import wget
import pythread as pt
import time

url = 'https://catalog.lenta.com/uploads/action_rules_3f66d26598.docx'


def download_file(url):
    print('Начало загрузки')
    time.sleep(10)
    wget.download(url)
    print('Файл загружен')


isDownloading = False

while True:
    i = input()

    if (len(pt.getThreads()) == 1) and isDownloading:
        isDownloading = False

    if i == 'download':
        if not isDownloading:
            thread = pt.createThread('Downloading', download_file, 0, url)
            thread.start()
            thread.do_run = False
            isDownloading = True
        else:
            print('Файл уже загружается')

    print(pt.getThreads())

    print(i)
