import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

# Create a ToastNotifier object
notifier = ToastNotifier()

# Function to fetch weather data
def fetch_weather_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Ensure the request was successful
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# URL for weather data
weather_url = "https://weather.com/en-IN/weather/today/l/92c8b30fd5f57445331a69e4ee32737135a913923516a20cd1409e63fa74ddd1"

# Fetch and parse the data
html_data = fetch_weather_data(weather_url)
if html_data:
    tmp= BeautifulSoup(html_data, 'html.parser')

    # Extract temperature
    temp_element = tmp.find("span", {
        "data-testid": "TemperatureValue",
        "class": "CurrentConditions--tempValue--zUBSz"
    })
    temperature = temp_element.text if temp_element else "N/A"

   

   
    weather_info = f"Temperature currently is {temperature} in Ponda, Goa."

    # Show notification
    notifier.show_toast("Live Weather Update", weather_info, duration=15)
else:
    print("Failed to fetch weather data.")
