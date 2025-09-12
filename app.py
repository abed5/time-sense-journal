import time

local_time = time.localtime()
year_guess = int(input("what do you think is the year?\n"))
month_guess = int(input("what do you think is the month? (1-12)\n"))
date_guess = int(input("what do you think is the date? (1-31)\n"))
day_guess = int(input("what do you think the day of week is? (0-6, Monday is 0)\n"))
time_guess = input("what do you think is the time? (hh:mm am/pm)\n")
print('guess: ' + str(year_guess), month_guess, date_guess, day_guess, time_guess)
print('actual: ' + str(local_time.tm_year), local_time.tm_mon, local_time.tm_mday, local_time.tm_wday, str(local_time.tm_hour) + ':' + str(local_time.tm_min))

year_diff = year_guess-local_time.tm_year
month_diff = month_guess-local_time.tm_mon
date_diff = date_guess-local_time.tm_mday
day_correct = 0
if day_guess == local_time.tm_wday:
    day_guess = 1
time_diff = str(int(time_guess.split(':')[0])-local_time.tm_hour) + ':' + str(int(time_guess.split(':')[1])-local_time.tm_min)
print(year_diff, month_diff, date_diff, day_correct, time_diff)