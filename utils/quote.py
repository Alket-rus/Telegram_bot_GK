import requests

def quote():
    url = 'http://rzhunemogu.ru/RandJSON.aspx?CType=5'
    try:
        response = requests.get(url)
        response.raise_for_status()
        quote_data = response.text 
        start_index = quote_data.find('content":"') + len('content":"')
        end_index = quote_data.find('"}', start_index)
        if start_index != -1 and end_index != -1:
            return quote_data[start_index:end_index]
        else:
            print("Цитата не найден в ответе")
            return None
    except requests.RequestException as e:
        print(f"Ошибка при запросе: {e}")
        return None

if __name__ == '__main__':
    quote()