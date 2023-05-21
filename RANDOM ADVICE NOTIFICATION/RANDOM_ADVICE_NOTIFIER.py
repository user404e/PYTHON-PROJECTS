from plyer import notification
from time import sleep
from requests import get

while True:
    try:
        req = get('https://api.adviceslip.com/advice')
        data = req.json()
        
        notification.notify(title='ADVICE : ',message=data['slip']['advice'],app_icon='ADVICE_ICON.ico',timeout=10)

        req.close()

    except:
        pass
    sleep(7200)
   