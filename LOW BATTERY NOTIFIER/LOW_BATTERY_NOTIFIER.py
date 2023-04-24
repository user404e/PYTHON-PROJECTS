from time import sleep
from plyer import notification,battery

while True:
    
    battery_data = battery.get_state()
    
    if(battery_data['isCharging']==False):
        
    
        if(battery_data['percentage']==50):
            
            notification.notify(
                message='BATTERY IS LESS THAN 50 % PLEASE CONNECT YOUR CHARGER',
                app_icon='BATTERY_ICON.ico',
                timeout=20
            )
            
        elif(battery_data['percentage']==40):
            
            notification.notify(
                message='BATTERY IS LESS THAN 40 % PLEASE CONNECT YOUR CHARGER',
                app_icon='BATTERY_ICON.ico',
                timeout=20
            )
        
        elif(battery_data['percentage']==30):
            
            notification.notify(
                message='BATTERY IS LESS THAN 30 % PLEASE CONNECT YOUR CHARGER',
                app_icon='BATTERY_ICON.ico',
                timeout=20
            )
        
        elif(battery_data['percentage']==25):
            
            notification.notify(
                message='BATTERY IS LESS THAN 25 % PLEASE CONNECT YOUR CHARGER IMMEDIATELY',
                app_icon='BATTERY_ICON.ico',
                timeout=20
            )
        
        elif(battery_data['percentage']==20):
            
            notification.notify(
                message='BATTERY IS LESS THAN 20 % PLEASE CONNECT YOUR CHARGER IMMEDIATELY',
                app_icon='BATTERY_ICON.ico',
                timeout=20
            )
        
        elif(battery_data['percentage']==15):
            
            notification.notify(
                message='BATTERY IS LESS THAN 15 % PLEASE CONNECT YOUR CHARGER IMMEDIATELY',
                app_icon='BATTERY_ICON.ico',
                timeout=20
            )
            
        elif(battery_data['percentage']==10):
            
            notification.notify(
                message='BATTERY IS LESS THAN 10 % PLEASE CONNECT YOUR CHARGER IMMEDIATELY',
                app_icon='BATTERY_ICON.ico',
                timeout=20
            )
        
        elif(battery_data['percentage']==5):
            
            notification.notify(
                message='BATTERY IS LESS THAN 5 % PLEASE CONNECT YOUR CHARGER IMMEDIATELY',
                app_icon='BATTERY_ICON.ico',
                timeout=20
            )
        
        elif(battery_data['percentage']==3):
            
            notification.notify(
                title='BATTERY NOTIFIER',
                message='BATTERY IS LESS THAN 3 % PLEASE CONNECT YOUR CHARGER IMMEDIATELY',
                app_icon='BATTERY_ICON.ico',
                timeout=20
            )
        
        elif(battery_data['percentage']==1):
            
            notification.notify(
                message='BATTERY IS 1 % PLEASE CONNECT YOUR CHARGER IMMEDIATELY',
                app_icon='BATTERY_ICON.ico',
                timeout=20
            )
    sleep(60)
