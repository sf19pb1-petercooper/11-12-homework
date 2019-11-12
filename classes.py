"""
classDate.py

Create a class named Date and call one of its class methods (monthsInYear).
Then create an object named d of class Date and call its instance methods.
"""

import sys

class Date(object):
    """
    Class Date demonstrates class and instance attributes, class and instance methods.
    It is a simple date class, containing year, month, and day integers.
    """

# The variable length in lengths in global scope is shared among all objects is called
# a "class attribute". See how lengths is under the class Date(object). Class attributes
# can be any size and any type of data.

    lengths = [
        None,
        31, #January
        28, #February (assume the year is not leap)
        31, #March
        30, #April
        31, #May
        30, #June
        31, #July
        31, #August
        30, #September
        31, #October
        30, #November
        31  #December
    ]

    january = 1
    february = 2
    march = 3
    april = 4
    may = 5
    june = 6
    july = 7
    august = 8
    september = 9
    october = 10
    november = 11
    december = 12

# The instance attributes (or members) are year, month and day. They are the little variables
# inside the __init__ method.


    def __init__(self, month, day, year): #attributes are loaded into the object via the __init__ method
        assert isinstance(year, int)
        assert isinstance(month, int) and 1 <= month <= Date.monthsInYear()
        self.year = year
        self.month = month
        self.day = day

    #These three methods are getters.
    @classmethod
    def newYearsDay(cls, year):
        print(f"cls = {cls}")
        print(f"type(cls) = {type(cls)}")
        return cls(1, 1, year)    #calls Date(1, 1, year) 

    def getYear(self):
        "Return my year."
        return self.year

    def getMonth(self):
        "Return the number of my month (1 to 12 inclusive)."
        return self.month

    def getDay(self):
        "Return the number of my day (1 to the length of my month, inclusive)."
        return self.day

    def __str__(self):
        "Return a string that looks like the contents of myself."
        return f"{self.month:02}/{self.day:02}/{self.year:04}"

    def dayOfYear(self): #this uses the class attribute Date.lengths and the instance attributes
        # self.month and self.day
        "Return my day of the year, a number in the range 1 to 365 inclusive."
        return sum(Date.lengths[1:self.month]) + self.day

    def nextDay(self):
        "Move myself one day into the future."
        if self.day < Date.lengths[self.month]:
            self.day += 1
        else:
            self.day = 1       #Go to the first day of the next month.
            if self.month < Date.monthsInYear():
                self.month += 1
            else:
                self.month = 1 #Go to the first month of the next year.
                self.year += 1

    def nextDays(self, n):
        "Move myself n days into the future."
        assert isinstance(n, int) and n >= 0
        for _ in range(n):
            self.nextDay()     #Call the instance method in line 62.

    def prevDay(self):
        "Move myself one day into the past."
        if self.day == 0:  # Go to the previous month.
            try:
                self.month -= 1
                print(self.month)
            except:
                pass
        elif self.day < Date.lengths[self.month]:
            self.day -= 1
        
    def prevDays(self, n):
        "Move myself n days into the past."
        assert isinstance(n, int) and n >= 0
        for _ in range(n):
            self.prevDay()     #Call the instance method in line 62.
                
    @staticmethod
    def monthsInYear():   #selfless
        "Return the number of months in a year.  This function is selfless."
        return len(Date.lengths) - 1

    #The definition of class Date ends here.

    @staticmethod
    def daysInYear():
        "Return the number of days in a year."
        return(sum(Date.lengths[1:]))
        

print(f"months in year = {Date.monthsInYear()}")
print(f"Days in year = {Date.daysInYear()}")
d = Date(Date.december, 31, 2019)         #Call the instance method in line 32.
newYearsDay = Date.newYearsDay(2019)   #ultimately calls Date(1, 1, 2019)
print(f"newYearsDay = {newYearsDay}")

print(f"type(d) = {type(d)}")
#print(f"{type(d) = }")
print()

#These three statements do the same thing:
#print(f"{d= }")
print(f"d = {d}")
print(f"d = {str(d)}")
print(f"d = {d.__str__()}")    # Call the instance method in line 54. Called
print()                        # whenever you call line 94 which in turn calls line 95.

print(f"month = {d.getMonth()}") #Call the instance method in line 46.
print(f"day = {d.getDay()}")     #Call the instance method in line 50.
print(f"year = {d.getYear()}")   #Call the instance method in line 42.
print()

print(f"{d} is day number {d.dayOfYear()} of the year {d.getYear()}.")
d.nextDay()                    # Call the instance method in line 62. The nextDay() method
                               # changes the Date object d.
print(f"{d} is the next day.")
d.nextDays(7)                  #Call the instance method in line 74.
print(f"{d} is a week after that.")
d.prevDay()
d.prevDay()
print(f"{d} is two days before that")
d.prevDay()
print(f"{d} is a day before that")
d.prevDay()
print(f"{d} is a day before that")
d.prevDay()
print(f"{d} is a day before that")
d.prevDay()
print(f"{d} is a day before that")
d.prevDay()
print(f"{d} is a day before that")
d.prevDay()
print(f"{d} is a day before that")
d.prevDay()
print(f"{d} is a day before that")
d.prevDay()
print(f"{d} is a day before that")
d.prevDay()
#sys.exit(0)
