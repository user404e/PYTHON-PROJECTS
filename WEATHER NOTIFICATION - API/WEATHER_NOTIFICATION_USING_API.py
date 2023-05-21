from requests import get
from time import sleep
from plyer import notification

while True:
    try:
        resposne = get('http://api.weatherapi.com/v1/current.json?key=971e0288ffde4535bdb60747220912&q=' + 'rajkot')
        data = resposne.json()
        
        city_name = data['location']['name']
        temeprature_celsius = str(data['current']['temp_c']) + '\u00b0' + '   CELSIUS'
        temeprature_fahrenheit = str(data['current']['temp_f']) + '\u00b0' + '   FAHRENHEIT'
        
        final = city_name.upper() + '\n\n' + temeprature_celsius + '\n' + temeprature_fahrenheit
        
        notification.notify(message=final,app_icon='WEATHER_ICON.ico',timeout=20)
    except:
        pass
    sleep(7200)
