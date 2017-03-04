days =0

# for i in range(1900,2001):
#     days +=365
#     if ((i%4==0 and (i%100>0)) or (i%4==0 and i%400==0)):
#         days +=1
#         print "%d is a leap year" % i

days = ["Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday","Monday"]
months = ["Jan","Feb","March","April","May","June","July","August","September","October","November","December"]
monthdays = [31,28,31,30,31,30,31,31,30,31,30,31]
day=0
sundayonfirst =0
for year in range(1901,2001):
    for month in range(0,12):
        days_in_month = monthdays[month]
        if ((month ==1) and ((year%4==0 and (year%100>0)) or (year%4==0 and year%400==0))):
            days_in_month = 29
            print "%d was a leap year so February had 29 days" % year
        day_offset = day%7
        # print "day offset: ", day_offset
        first_of_month_day = days[day_offset]
        print "The 1st day of %s in %d was a %s"%(months[month],year,first_of_month_day)
        day += days_in_month

        if first_of_month_day=="Sunday":
            sundayonfirst+=1
            print "Sunday on first in %s of %d" % (months[month],year)
print "_"*10
print "Number of Sundays on first of the month: ", sundayonfirst
