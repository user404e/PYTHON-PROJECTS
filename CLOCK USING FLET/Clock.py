import flet as ft
from datetime import datetime
import time
def main(page:ft.Page):
    txt1 = ft.Text(value="Date - ")
    t1 = ft.Text()
    txt2 = ft.Text(value="Time - ")
    t2 = ft.Text()
    
    page.add(txt1,t1,txt2,t2) # it's a shortcut for page.controls.append(t) and then page.update()

    for i in range(10):
        page.title = 'Clock'
        cdt = datetime.now()
        cdate = str(cdt.day) + " - " + str(cdt.month) + " - " + str(cdt.year)
        ctime = str(cdt.hour) + " - " + str(cdt.minute) + " - " + str(cdt.second)
        t1.value = cdate
        t2.value = ctime
        page.update()
        time.sleep(1)
        
ft.app(target=main)