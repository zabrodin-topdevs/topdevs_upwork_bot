from bottoken import bottoken
from bottoken import chatid
import requests
import json
from datetime import datetime
from variables import VariableFile

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Started at ", current_time)

forecastUrl = "https://api.open-meteo.com/v1/forecast?latitude=48.46&longitude=35.04&current_weather=true"
last_temperature_file = VariableFile("variable.txt")
last_temperature = last_temperature_file.read()
print(last_temperature)

try:
    forecastResponse = requests.get(forecastUrl, timeout=10.0)
    forecastJson = json.loads(forecastResponse.content)
    current_weather = forecastJson["current_weather"]
    print(current_weather)

    temperature = str(current_weather["temperature"])
    windspeed = str(current_weather["windspeed"])

#    last_temperature = float(os.environ.get('LAST_TEMPERATURE', '-99'))

    if temperature == last_temperature:
        print("Temperature isn't changed")
        exit()

    last_temperature_file.write(str(temperature))


#    os.environ['LAST_TEMPERATURE'] = str(temperature)
#    print(os.environ.get('LAST_TEMPERATURE', '-99'))

    message = "temperature: " + temperature + " windspeed: " + windspeed
    print(message)

    res = requests.get(
        url=f"https://api.telegram.org/{bottoken}/sendMessage?chat_id={chatid}&text=" +
            message)
    print(res.text)

except:
  print("Something went wrong")