from datetime import datetime, date

# 1 Get the current day, month, year, hour, minute and timestamp from datetime module
now = datetime.now()
day = now.day
month = now.month
year = now.year
minute = now.minute
timestamp = now.timestamp()
print('Day: {} \n Month: {} \n Year: {} \n Minute: {} \n Timestamp: {}' .format(day, month, year, minute, timestamp))
# 2 Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
format_s = now.strftime("%m/%d/%Y, %H:%M:%S")
#format_t = now.strftime("%H:%M:%S")
print(format_s)
# 3 Today is 5 December, 2019. Change this time string to time.
str_to_time = date(year=2019, month=12, day=5)
print(str_to_time)

date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)
# 4 Calculate the time difference between now and new year.
day_today = date.today()
new_year = date(2027, 1, 1)
time_to_newyear =  new_year - day_today
print(time_to_newyear)
# 5 Calculate the time difference between 1 January 1970 and now.
gone_day = date(1970, 1, 1)
print(day_today - gone_day, ' days difference!')