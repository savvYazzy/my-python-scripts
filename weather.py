import requests

api_key = "4016fdbdcf3d690de7a132307dbfb707" # replace with your own API key
city = input("Enter the name of a city: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(url)

if response.ok:
    data = response.json()
    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]
    print(f"The current temperature in {city} is {temperature}°C with {description}.")
else:
    print("Error: Unable to retrieve weather information.")
