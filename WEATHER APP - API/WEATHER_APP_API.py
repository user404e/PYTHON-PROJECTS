from requests import get
print("\n----- WEATHER APP -----\n")
try:
    
    city = input("ENTER CITY NAME : ")
    
    d1 = get('http://api.weatherapi.com/v1/current.json?key=971e0288ffde4535bdb60747220912&q=' + city)
   
    data = d1.json()
    
    print("\nNAME : " + data['location']['name'])
    print("REGION : " + data['location']['region'])
    print("TIME-ZONE : " + data['location']['tz_id'])
    print("LOCAL TIME : " + data['location']['localtime'])

    print("\nTEMPERATURE : ",data['current']['temp_c'],"C 'OR'",data['current']['temp_f'],"F")
    print("WIND : ",data['current']['wind_kph'],"KPH")
    print("HUMIDITY : ",data['current']['humidity'],"%")
    print("CLOUD : ",data['current']['cloud'],"%")

except:
    
    print("\nNO INTERNET CONNECTION - ")


