import requests

def city_choice_KO_weather(user_city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={user_city}&lang=ru&units=metric&appid=2265bd82256457d68acf98993681e796&exclude=minutely,hourly,daily,alerts'
    
    try:
        response = requests.get(url)
        data = response.json()
        
        cur_temp = data["main"]["temp"]
        
        user_city_modified = user_city.title()

        return (f"Текущая температура в городе {user_city_modified}: {cur_temp}°C\n"
                f"Хорошего дня!")
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")



if __name__ == '__main__':
    city_choice_KO_weather()
