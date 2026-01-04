from datetime import datetime

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
# 4 Calculate the time difference between now and new year.
# 5 Calculate the time difference between 1 January 1970 and now.