import time

local_time = time.localtime()
year_guess = int(input("what do you think is the year?\n"))
month_guess = int(input("what do you think is the month? (1-12)\n"))
day_guess = int(input("what do you think is the day? (1-31)\n"))
time_guess = input("what do you think is the time? (hh:mm am/pm)\n")
print('guess: ' + str(year_guess), month_guess, day_guess, time_guess)
print('actual: ' + str(local_time.tm_year), local_time.tm_mon, local_time.tm_mday, str(local_time.tm_hour) + ':' + str(local_time.tm_min))
