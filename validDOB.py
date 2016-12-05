#Determines current time and validates DOB

import time

t=time.localtime(time.time())
cur_year = t[0]
cur_month = t[1]
cur_day = t[2]

def validDOB (month,day,year):
        while 1:
            if year <= 0 or month <= 0 or day <= 0:
                break
            if cur_year < year:
                break
            if month > 12:
                break
            if month in (1,3,5,7,8,10,12):
                if day > 31:
                    break
            elif month in (4,6,9,11):
                if day > 30:
                    break
            if year %4 == 0 and month == 2:
                if day >29:
                    break
            return 1
        return 0

def age(dob):
    if len(dob) != 10:
            print ("Invalid format try ... mm-dd-yyyy")
            return 0
    m = int(dob[:2])
    d = int(dob[3:5])
    y = int (dob[6:10])

    if validDOB(m,d,y) == 0:
            print ("Invalid DOB")
        
            return 0
    else:
        age = cur_year -y -1
        if m < cur_month or (m == cur_month and d < cur_day):
                age = age + 1
        return str(age)
