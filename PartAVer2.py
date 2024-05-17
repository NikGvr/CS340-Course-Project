#Gavriilidis Nikolaos
#20220427@student.act.edu
#Part A for Pyhton project

# imports that will be needed ( suposedly )

import sys
import os
from typing import List, Any

# Classes, filenames and lists that will be needed for the project based on project desciption.

# setting the filenames for the functions using them

inputfile = "partA_input_data.txt"
outputfile = "partA_output_data.txt"

# creating the lists that will be used with the files.

# the list that contains the original data from the file.

F1File = []

# the list that will contain the sorted data for the file.

F1FileSorted = []

# the list that will contain the data for option 3 ( with the average lap time per race)

F1OutputFile = []

# the list that will be used for option 4, it is basically the previous one but sorted.

F1OutputFileSorted = []

#A list that will be used for option 5 and it will have the driver names and the average lap time (x-axis: driver names. y-axis: average lap time in minutes)

F1AverageLapTimes = []

# creating the classes that will be used in the lists, mostly date, time, race, Driver. 

# Date class

class Date:

    # variables used by the class

    self.DayNum = 0 
    self.DayStr = ""
    self.MonNum = 0
    self.MonStr = ""
    self.YearNum = 0
    self.YearStr = ""

    # list of months that will be used to calculate the variable MonNum

    self.MonthsList = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    # constructor for the class

    def __init__(self, day, month, year):
        
        # puttin the day as a number and as a string

        self.DayNum = int(day)

        # making the day into a string

        if(int(day) <= 9):

            self.DayStr = ("0" + str(int(day)))
        
        else:
            self.DayStr = str(day)

        # making the month string

        self.MonStr = str(month)

        #making the month number based on the list.

        for i in range(len(self.MonthsList)):

            if(MonthsList[i] == str(month)):

                index = i

        self.MonNum = index

        # making the year num and str

        self.YearNum = int(year)

        self.YearStr = str(year)

        # a function to return date in the format that is in te file.

        def ReturnDate(self):
        
            ReturnString = f"{self.DayStr}-{self.MonStr}-{self.YearStr}"
        
            return ReturnString
        

# the time class

class Time:

    # variables that will be used in the time class.

    self.MinNum = 0
    self.MinStr = ""
    self.SecNum = 0
    self.SecStr = ""
    self.MillisecNum = 0
    self.MillisecStr = ""

    # constructor for the class

    def __init__(self, minutes, seconds, milliseconds):

        # creating the minutes number and string

        self.MinNum = int(minutes)

        if(int(minutes) <= 9):

            self.MinStr = ("0", str(int(minutes)))

        else:

            self.MinStr = str(int(minutes))

        # creating the seconds number and string

        self.SecNum = int(seconds)

        if(int(seconds) <= 0):

            self.SecStr = ("0", str(int(seconds)))

        else:

            self.SecStr = str(int(seconds))

        # creating the milliseconds number and string

        self.MillisecNum = int(milliseconds)

        self.MillisecStr = str(milliseconds)

        # function to return the time in the format of the file

        def ReturnTime(self):

            ReturnString = f"{self.MinStr}:{self.SecStr}.{self.MillisecStr}"

            return ReturnString


# race class to save the races.

class Race:

    # variables used by the race class.

    self.GrandPrix = "" # name of the race 

    self.Date = Date # the date of the race

    self.Winner = "" # the name of the winner

    self.Car = "" # the name of the car ( the team name )

    self.Laps = 0 # the number of laps

    self.Time = Time # the time it took

    self.AverageLapTime = 0 # the average lap time ( needed for option 3 )

    # a constructor for the Race class

    def __init__(self, GrandPrix, Date, Winner, Car, Laps, Time):

        # GrandPrix name

        self.GrandPrix = str(GrandPrix)

        # date of the race

        self.Date = Date

        # name of the winner

        self.Winner = str(Winner)

        # name of the car ( team name)

        self.Car = str(Car)

        # number of laps

        self.Laps = int(Laps)

        # time that the race took

        self.Time = Time

    # function to return race as a string.

    def ReturnRace(self):

        StringToReturn = (f"{self.GrandPrix:<15} {self.Date.ReturnDate():<15} {self.Winner:<20} {self.Car:<20} {self.Laps:<5} {self.Time.ReturnTime():<15}")

        return StringToReturn
    
# a class for the driver data ( needed for option 5)

class Driver:

    # variables used by the driver class.

    self.DriverName = ""
    self.TotalLaps = 0
    self.TotalTime = 0

    def __init__(self, name, laps, time):

        self.DriverName = str(name)

        self.TotalLaps = int(laps)

        
        



