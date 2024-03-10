import requests

def poem():
    url = 'http://rzhunemogu.ru/RandJSON.aspx?CType=3'
    try:
        response = requests.get(url)
        response.raise_for_status()
        poem_data = response.text 
        start_index = poem_data.find('content":"') + len('content":"')
        end_index = poem_data.find('"}', start_index)
        if start_index != -1 and end_index != -1:
            return poem_data[start_index:end_index]
        else:
            print("Стих не найден в ответе")
            return None
    except requests.RequestException as e:
        print(f"Ошибка при запросе: {e}")
        return None

if __name__ == '__main__':
    poem()