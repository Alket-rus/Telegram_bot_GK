import requests

def joke():
    url = 'http://rzhunemogu.ru/RandJSON.aspx?CType=1'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверяем успешность запроса
        joke_data = response.text  # Получаем текст ответа
        # Извлекаем анекдот из текста
        start_index = joke_data.find('content":"') + len('content":"')
        end_index = joke_data.find('"}', start_index)
        if start_index != -1 and end_index != -1:
            return joke_data[start_index:end_index]
        else:
            print("Анекдот не найден в ответе")
            return None
    except requests.RequestException as e:
        print(f"Ошибка при запросе: {e}")
        return None

if __name__ == '__main__':
    joke()