import csv
import datetime
import holidays
import os

start_date = datetime.date(1990, 1, 1)
end_date = datetime.date(2030, 12, 31)

filename = 'data/dates.csv'
file_count = 0
while os.path.isfile(filename):
    file_count += 1
    filename = f'data/dates({file_count}).csv'

os.makedirs(os.path.dirname(filename), exist_ok=True)  # create subfolder if it doesn't exist


date_format = "%Y-%m-%d"
header = ['Day', 'Year', 'Month', 'MonthName', 'Weekday', 'WeekdayName', 'IsWeekend', 'IsHoliday', 'Holiday']
with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    us_holidays = holidays.UnitedStates()
    for delta in range((end_date - start_date).days + 1):
        date = start_date + datetime.timedelta(delta)
        year = date.year
        month = date.month
        month_name = date.strftime('%B')
        weekday = date.weekday()
        weekday_name = date.strftime('%A')
        is_weekend = weekday >= 5
        is_holiday = date in us_holidays
        holiday_name = us_holidays.get(date, '')
        row = [date.strftime(date_format), year, month, month_name, weekday, weekday_name, is_weekend, is_holiday, holiday_name]
        writer.writerow(row)

print(f'{filename} generated successfully!')
