import wget
import threading
import time


url = 'https://catalog.lenta.com/uploads/action_rules_3f66d26598.docx'


def download_file(url):
        print('Начало загрузки файла')
        time.sleep(5)
        wget.download(url)
        print('Файл загружен')


isDownloading = False

while True:
    i = input()

    if (len(threading.enumerate()) == 1) and isDownloading:
        isDownloading = False

    if i == 'download':
        if not isDownloading:
            thread = threading.Thread(target=download_file, args=(url,))
            thread.start()
            isDownloading = True
        else:
            print('Файл уже загружается')

    print(threading.enumerate())

    print(i)