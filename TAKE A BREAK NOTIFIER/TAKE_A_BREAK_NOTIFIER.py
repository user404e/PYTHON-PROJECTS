from time import sleep
from plyer import  notification

while True:
    sleep(7200)
    notification.notify(message='YOU   HAVE   BEEN   USING   PC   FOR   2   HOURS,   PLEASE   TAKE   A   BREAK',
                        app_icon="TAKE_BREAK_ICON.ico",
                        timeout=20
                        )
    
