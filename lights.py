from phue import Bridge
import requests
import json
# Get information from wheather api
# requests help us to get information from website
#to hide variables is os environment variables

#Credentials
api_key = "..........."
url = "http://api.openweathermap.org/data/2.5/weather?q=Austin&appid="+api_key

#hit the web url
r = requests.get(url)
readable_data = r.json()
#make the data more readable through json
pretty_data = json.dumps(readable_data, indent=4, sort_keys=True)
#dumps just basically tells how its gonna look

weather_today = readable_data["weather"][0]["main"]

if(weather_today == "Clouds"):
    # use the bridge to connect to
    print("True");




