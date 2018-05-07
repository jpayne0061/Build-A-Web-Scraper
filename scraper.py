import requests
from bs4 import BeautifulSoup
import re
import json

def strip_word_and_space(text, word_to_replace):
    stripped = text.replace(word_to_replace, "")
    stripped = stripped.replace(" ", "")
    return stripped

def strip_location(loc):
    location_strip = loc.replace("Location:", "")
    space_stripped = location_strip.replace(" ", "")
    city = space_stripped.split(",")[0]
    state = space_stripped.split(",")[1]    
    return [city, state]

url = "https://evan-payne.000webhostapp.com/scrape/cars.html"
source_code = requests.get(url)
soup = BeautifulSoup(source_code.text)

list_car_info = soup.findAll('div', {'class': 'vehicle-card'})

for car_info in list_car_info:
    car_data = {}
    
    details = car_info.find('div', {'data-qa': 'VehicleCardDetails'})
    make = details.find('a').get("data-analytics-make")
    model = details.find('a').get("data-analytics-model")
    year = details.find('a').get("data-analytics-year")
    
    price = re.sub("\D", "", car_info.find('p', {'class': 'price'}).text)
    
    car_data["make"] = make
    car_data["model"] = model
    car_data["year"] = year
    car_data["price"] = price
    
    ul_contents = details.find('ul').contents
    
    for content in ul_contents:
        if "VIN:" in content.text:
            car_data["vin"] = strip_word_and_space(content.text, "VIN:")
        if "Mileage:" in content.text:
            car_data["mileage"] = re.sub("\D", "", content.text)
        if "Location:" in content.text:
            car_data["city"] = strip_location(content.text)[0]
            car_data["state"] = strip_location(content.text)[1]

    json_data = json.dumps(car_data)
    with open("data.json", 'a') as f:
	     f.write(json_data + "\n") 
            
            
            
            
            
            
    

