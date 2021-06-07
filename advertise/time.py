from datetime import datetime

data = datetime.now()
year = data.year
month = data.month
day = data.day
hours = data.hour
minute = data.minute
second = data.second

times = int(f"{year}{month}{day}{hours}{minute}{second}")
print(type(times))