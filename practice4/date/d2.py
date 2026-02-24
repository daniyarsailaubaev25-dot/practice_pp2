from datetime import date, timedelta

current_date = date.today()
yesterday_date = current_date - timedelta(days=1)
tomorrow_date = current_date + timedelta(days=1)

print(yesterday_date)
print(current_date)
print(tomorrow_date)