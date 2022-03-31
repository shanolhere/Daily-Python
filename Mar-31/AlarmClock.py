#Alarm Clock with Python
from datetime import datetime
#from playsound import playsound
alarm_time = input("Enter the time in HH:MM:SS :")
alarm_hour = alarm_time[:2]
alarm_min = alarm_time[3:5]
alarm_sec = alarm_time[6:8]
alarm_period = alarm_time[9:].upper()

while True:
    now = datetime.now()
    current_hr = now.strftime("%H")
    current_min = now.strftime("%M")
    current_sec = now.strftime("%S")
    current_period = now.strftime("%p")
    if current_period == alarm_period:
        if current_hr == alarm_hour:
            if current_min == alarm_min:
                if current_sec == alarm_sec:
                    print("WakeUp bud")
                    #playsound(audio.mp3)
                    break