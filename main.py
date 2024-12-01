import requests
import time

# Куда отправлять запрос?
url = "https://api-gw.geagle.online/tap" 

# Заголовки
headers = {
    "Authorization": "" # Ваш код авторизации
}

# Цикл
while True:
    try:
        # Данные
        data = {
            "available_taps": 0,
            "count": 1000,
            "timestamp": int(time.time() * 1000)  # Текущая временная метка в миллисекундах
        }

        # POST запрос
        response = requests.post(url, json=data, headers=headers)
        
        # Статус
        print(f"Запрос отправлен. Код ответа: {response.status_code}, Тело ответа: {response.text}")
    except Exception as e:
        print(f"Ошибка при отправке запроса: {e}")

    # Ожидание
    time.sleep(1000)