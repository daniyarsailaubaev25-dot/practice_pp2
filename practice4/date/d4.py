from datetime import datetime

date1 = input("Enter the first date (YYYY-MM-DD HH:MM:SS): ")
date2 = input("Enter the second date (YYYY-MM-DD HH:MM:SS): ")


dt1 = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
dt2 = datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")

diff = abs((dt1-dt2).total_seconds())
print(diff)

