from googleapiclient.discovery import build          # импортируем функцию build для создания объектов службы api
import re                       # модуль re, для работы со строками и регулярными выражениями для нахождения совпадений

api_key = 'AIzaSyA7nB1coFcBh9YmMfHGmNpiLtu1SIhCSws'   # ключ api

youtube = build('youtube', 'v3', developerKey=api_key)     # Создается объект youtube api

def get_video_type(video_url):       # функция get_video_type, которая принимает в качестве аргумента URL видео
    # используем регулярное выражение для поиска и извлечения идентификатора youtube видео из url. Он ищет последовательность символов длиной 11, которая может содержать цифры, заглавные и строчные латинские буквы, а также символы "_-" после подстрок 'v=' или '/'
    video_id = re.findall(r'(?:v=|/)([0-9A-Za-z_-]{11}).*', video_url) 

    if not video_id:                    # успешно ли найден идентификатор видео в url                 
        return 'URL видео некорректен'
    else:
        video_id = video_id[0]  # обращаемся к первому элементу списка с помощью индекса [0] и присваиваем его новой переменной video_id

    # Получите информацию о видео
    video_response = youtube.videos().list(   # обращаемся к методу list для работы с ресурсом videos
        part='snippet,contentDetails',    # запрашиваем данные из разделов snippet (основные детали видео, такие как заголовок, описание) и contentDetails
        id=video_id           #  используем ранее извлеченный video_id, чтобы запросить информацию о конкретном видео
    ).execute()        #  отправляет запрос к youtube api для выполнения операции, заданной в предыдущих шагах
    
    # Проверьте тип видео
    video_type = 'Неизвестно'      # изначальное значение 
    if 'shorts' in video_url:
        video_type = 'Shorts'
        # проверка на наличие элементов в items (если список пуст, то информация не была получена от youtube api), and проверка на наличие информации о трансляции в первом элементе списка items, если liveBroadcastContent не равно 'none', это означает, что видео является трансляцией 
    elif video_response['items'] and video_response['items'][0]['snippet']['liveBroadcastContent'] != 'none':
        video_type = 'Translation'
    else:
        video_type = 'Standart'
    
    return video_type     # возвращаем video_type

# Пример использования функции
video_url = input("Введите URL видео: ")   # просим пользователя ввести URL
print(get_video_type(video_url))         # вызываем функцию get_video_type
