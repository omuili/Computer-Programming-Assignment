class Date(object):
    def __init__(self, month, day, year):
        self._month = month
        self._day = day
        self._year = year

    def leap_year(self):
        if self._year%4 == 0:
            if self._year%100 == 0:
                if self._year%400 == 0:
                    return True # divisible by 4 and century and also divisible by 400
                else:
                    return False # divisible by 4 and century and also not divisible by 400
            else:
                return True # divisible by 4 and not a century
        else:
            return False # not divisible by 4
            
    def tomorrow(self):
        if self._month in [1,3,5,7,8,10]:
            if self._day < 31:
                return Date(self._month,self._day+1,self._year)
            else:
                return Date(self._month+1,1,self._year)
        elif self._month in [4,6,9,11]:
            if self._day < 30:
                return Date(self._month,self._day+1,self._year)
            else:
                return Date(self._month+1,1,self._year)
        elif self._month == 12:
            if self._day == 31:
                return Date(1,1,self._year+1)
            else:
                return Date(self._month,self._day+1,self._year)
        elif self._month == 2:
            if self.leap_year():
                if self._day == 29:
                    return Date(self._month+1,1,self._year)
                else:
                    return Date(self._month,self._day+1,self._year)
            else:
                if self._day == 28:
                    return Date(self._month+1,1,self._year)
                else:
                    return Date(self._month,self._day+1,self._year)
        else:
            return None
        
    def yesterday(self):
        if self._month in [1,3,5,7,8,10]:
            if self._day < 31:
                return Date(self._month,self._day-1,self._year)
            else:
                return Date(self._month-1,1,self._year)
        elif self._month in [4,6,9,11]:
            if self._day < 30:
                return Date(self._month,self._day-1,self._year)
            else:
                return Date(self._month-1,1,self._year)
        elif self._month == 12:
            if self._day == 31:
                return Date(1,1,self._year-1)
            else:
                return Date(self._month,self._day-1,self._year)
        elif self._month == 2:
            if self.leap_year():
                if self._day == 29:
                    return Date(self._month-1,1,self._year)
                else:
                    return Date(self._month,self._day-1,self._year)
            else:
                if self._day == 28:
                    return Date(self._month-1,1,self._year)
                else:
                    return Date(self._month,self._day-1,self._year)
        else:
            return None

    def add(self,ndays):
        d = Date(self._month,self._day,self._year)
        for i in range(ndays):
            d = d.tomorrow()
        return d

    def sub(self,ndays):
        d = Date(self._month,self._day,self._year)
        for i in range(ndays):
            d = d.yesterday()
        return d
        
    def first_of_next_month(self):
        pass

    def first_of_previous_month(self):
        pass

    def after(self, d):
        #returns True if the calling object represents a calendar date that occurs after the calendar
        #date that is represented by other. 
        if self == d:
            return False
        elif not self.is_before(d):
            return True
        else:
            return False

    def equals(self,d):
        #returns True if the called object (self) and the argument (other) represent the same calendar date
        if self.day == d.day and self.month == d.month and self.year == d.year:
            return True
        else:
            return False

    def before(self, d):
        #returns True if the called object represents a calendar date that occurs
        #before the calendar date that is represented by other.
        if self == d:
            return False
        if self.year < d.year:
            return True
        elif self.year < d.year and self.month < d.month:
            return True
        elif self.year < d.year and self.month < d.month and self.day < d.day:
            return True
        else:
            return False

    def days_between(self,d):
    #returns an integer that represents the number of days between self and other
        num_days = 0
        self_copy = self.copy()
        d_copy = d.copy()
        if self == d:
            return num_days
        if self_copy.is_before(d_copy):
            while self_copy != d_copy:
                self_copy.tomorrow()
                num_days += 1

    def __str__(self):
        sMonths = "01January:02February:03March:04April:05May:06June:" + \
                  "07July:08August:09September:10October:11November:12December:"
        m = "0"+str(self._month) if (self._month<10) else ""+str(self._month)
        i = sMonths.find(m)
        j = sMonths.find(":",i)
        sMonth = sMonths[i+2:j]
        return str(self._day) + " " + sMonth + ", " + str(self._year)