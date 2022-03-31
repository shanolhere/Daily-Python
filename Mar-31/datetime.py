from datetime import datetime
now = datetime.now()
current_period = now.strftime("%p")
print(current_period)
print(now)