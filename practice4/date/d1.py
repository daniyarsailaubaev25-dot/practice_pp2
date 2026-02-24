from datetime import timedelta, date

current_date = date.today()

diff = current_date - timedelta(days=5)
print(diff)
