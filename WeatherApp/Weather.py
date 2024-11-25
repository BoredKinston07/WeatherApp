from bs4 import BeautifulSoup as BS4
import requests
import eel

# Ініціалізація Eel
eel.init('web')

# Створимо функцію, яка буде передавати результат в JavaScript
@eel.expose
def get_weather(country, city):
    # Форматуємо введені країну і місто для URL
    city_formatted = city.lower().replace(" ", "-")
    country_formatted = country.lower()
    url = f"https://www.timeanddate.com/weather/{country_formatted}/{city_formatted}"

    response = requests.get(url)

    soup = BS4(response.text, 'html.parser')

    try:
        # Знайдемо температуру і відправимо результат назад у JS
        temperature = soup.find("div", class_="h2").get_text(strip=True)
        return temperature
    except AttributeError:
        return "City or country not found, or there was an issue with the request."

# Запуск програми Eel
eel.start('main.html', size=(700, 700))
