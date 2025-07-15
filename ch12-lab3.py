# Joe Melia EET-107
import requests 

def main():
    print("Weather App\n")
    zipc = input("What is your zipcode? ").strip()
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?zip={zipc},us&appid=6f897a600039febcb8d251d9a33da0d1&units=imperial")
    if response:
       response_dict = response.json()
       city = response_dict["name"]
       conditions = response_dict["weather"][0]["description"]
       temp = response_dict["main"]["temp"]
       ftemp = response_dict["main"]["feels_like"]
       humid = response_dict["main"]["humidity"]
       windsp = response_dict["wind"]["speed"]
       deg = response_dict["wind"]["deg"]
       print(f"The Current Weather for {city}:")
       print(f"Conditions: {conditions}")
       print(f"Temperature: {temp} Degrees")
       print(f"Feels like: {ftemp} Degrees")
       print(f"Humidity: {humid}")
       print(f"Wind: {windsp} knots @ {deg} degrees")

main()
