# CS340 Course Project
# Gavriilidis Nikolaos
# 20220427@student.act.edu

# part A

#import statements

import sys
import os
from typing import List, Any

# Date and Time classes that will be needed for the list because doing that with Libraries right now is a Pain in the head.


class Date:
    def __init__(self, day, month, Year):
        self.DayNum = int(day)

        if day <= 9:
            self.DayStr = "0" + str(day)
        else:
            self.DayStr = str(day)

        
        self.MonthStr = str(month)
        self.MonthList = ["Jan", 'Feb', "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        self.MonthNum = 0
        for i in range(len(self.MonthList)):
            if self.MonthStr == self.MonthList[i]:
                self.MonthNum = i + 1
        
        self.YearStr = str(Year)
        self.YearNum = int(Year)



    def ShowDate(self):
        print(self.DayStr, "-", self.month, "-", self.year)

    def ReturnDate(self):
        ReturnString = f"{self.DayStr}-{self.MonthStr}-{self.YearStr}"
        return ReturnString


class Time:
    def __init__(self, min, sec, millisec):

        self.MinNum = int(min)

        if int(min) <= 9:
            self.MinStr = "0" + str(min)
        else:
            self.MinStr = str(min)

        
        self.SecNum = int(sec)

        if(int(sec) <= 9):
            self.SecStr = "0" + str(sec)
        else:
            self.SecStr = str(sec)

        self.MillisecNum = int(millisec)
        self.MillisecStr = str(millisec)


        self.TotalMilliseconds = 0

        self.TotalMilliseconds = self.MillisecNum + (self.SecNum*1000) + (self.MinNum*60*1000)

    def ShowTime(self):
        print(self.MinString, "-", self.Seconds, "-", self.Millisec)

    def ReturnTime(self):
        ReturnString = f"{self.MinStr}-{self.SecStr}-{self.MillisecStr}"
        return ReturnString


class Race:

    def __init__(self, GrandPrix, Date, Winner, Car, Laps, Time):
        self.GrandPrix = str(GrandPrix)
        self.Date = Date
        self.Winner = str(Winner)
        self.Car = str(Car)
        self.Laps = int(Laps)
        self.Time = Time

    def ReturnRace(self):
        StringToReturn = (f"{self.GrandPrix:<15} {self.Date.ReturnDate():<15} {self.Winner:<20} {self.Car:<20} {self.Laps:<5} {self.Time.ReturnTime():<15}")
        return StringToReturn



F1List = []

def CreatePartAFile():
    file = open(filename, "w")
    file.write("GRAND PRIX,DATE,WINNER,CAR,LAPS,TIME\n")
    file.write("Bahrain,05-Mar-23,Max Verstappen,RED BULL RACING,57,33:56.7\n")
    file.write("Saudi Arabia,19-Mar-23,Sergio Perez,RED BULL RACING,50,21:14.9\n")
    file.write("Australia,02-Apr-23,Max Verstappen,RED BULL RACING,58,32:38.4\n")
    file.write("Azerbaijan,30-Apr-23,Sergio Perez,RED BULL RACING,51,32:42.4\n")
    file.write("Miami,07-May-23,Max Verstappen,RED BULL RACING,57,27:38.2\n")
    file.write("Monaco,28-May-23,Max Verstappen,RED BULL RACING,78,48:52.0\n")
    file.write("Spain,04-Jun-23,Max Verstappen,RED BULL RACING,66,27:57.9\n")
    file.write("Canada,18-Jun-23,Max Verstappen,RED BULL RACING,70,33:58.3\n")
    file.write("Austria,02-Jul-23,Max Verstappen,RED BULL RACING,71,25:33.6\n")
    file.write("Great Britain,09-Jul-23,Max Verstappen,RED BULL RACING,52,25:16.9\n")
    file.write("Hungary,23-Jul-23,Max Verstappen,RED BULL RACING,70,38:08.6\n")
    file.write("Belgium,30-Jul-23,Max Verstappen,RED BULL RACING,44,22:30.4\n")
    file.write("Netherlands,27-Aug-23,Max Verstappen,RED BULL RACING,72,24:04.4\n")
    file.write("Italy,03-Sep-23,Max Verstappen,RED BULL RACING,51,13:41.1\n")
    file.write("Singapore,17-Sep-23,Carlos Sainz,FERRARI,62,46:37.4\n")
    file.write("Japan,24-Sep-23,Max Verstappen,RED BULL RACING,53,30:58.4\n")
    file.write("Qatar,08-Oct-23,Max Verstappen,RED BULL RACING,57,27:39.2\n")
    file.write("United States,22-Oct-23,Max Verstappen,RED BULL RACING,56,35:21.4\n")
    file.write("Mexico,29-Oct-23,Max Verstappen,RED BULL RACING,71,02:30.8\n")
    file.write("Brazil,05-Nov-23,Max Verstappen,RED BULL RACING,71,56:48.9\n")
    file.write("Las Vegas,18-Nov-23,Max Verstappen,RED BULL RACING,50,29:08.3\n")
    file.write("Abu Dhabi,26-Nov-23,Max Verstappen,RED BULL RACING,58,27:02.6\n")
    file.close()


def Show5Options():
    print("======================================================================")
    print("  F1 GRAND PRIX RACING DATA & STATISTICS FOR THE 2023 RACING SEASON.  ")
    print("======================================================================")
    print("1. Read and display the F1 Grand Prix data for the 2023 racing season.")
    print("2. Filter and sort race data based on a minimum threshold of laps.")
    print("3. Calculate average lap time per race, save, retrieve, display.")
    print("4. Sort and display the data based on user parameters.")
    print("5. Calculate and graph total lap time per driver.")
    print("6. Exit the program.")



def CheckIfValidOption(option):
    if(option <= 6 and option >= 1):
        print("Valid option, continuing.")
        return True
    else:
        print("Invalid option, please try again.")
        return False

def FileToList():
    file = open(filename, "r")
    lines = file.readlines()
    for line in lines[1:]:
        tokens = line.strip().split(',')

        race_token = str(tokens[0])

        date_token = tokens[1].split('-')
        day_token = int(date_token[0])
        month_token = str(date_token[1])
        year_token = int(date_token[2])

        date_token = Date(day_token, month_token, year_token)


        winner_token = str(tokens[2])

        car_token = str(tokens[3])

        laps_token = int(tokens[4])

        time_token = tokens[5]
        time_values = time_token.split(":")
        minutes, seconds_millisec = time_values[0], time_values[1]
        seconds, millisec = seconds_millisec.split(".")

        time_token = Time(minutes, seconds, millisec)


        RaceToAppend = Race(race_token, date_token, winner_token, car_token, laps_token, time_token)

        F1List.append(RaceToAppend)

    file.close()





def option1():
    fout = open(filename, "r")
    for line in fout:
        fields = line.strip().split(',')
        print(f"{fields[0]:<15} {fields[1]:<15} {fields[2]:<20} {fields[3]:<20} {fields[4]:<5} {fields[5]:<15}")


    fout.close()

#Menu option 2: Asks the user for a limit of laps to search by, then displays only the race results
#which involve that number of home laps or greater, sorted alphabetically by Grand Prix name.

def option2():

    LapsLimit = 0
    LapsLimit = int(input("Plase input a limit of laps to show races that have more laps that than and Alphabetically sorted."))

    # Creating the F1ListSorted that will be used for that option

    F1ListSorted = []

    #inserting data

    for i in range(len(F1List)):
        if F1List[i].Laps >= LapsLimit:
            F1ListSorted.append(F1List[i])
        
    #Testing the values of F1ListSorted

    for i in range(len(F1ListSorted)):
        print(F1ListSorted[i].ReturnRace())

    #sorting the lines alphabetically using the Grand Prix name

    F1ListSorted = sorted(F1ListSorted, key=lambda x: x.GrandPrix)




    #Checking if the list was sorted proeprly
    print("SortTest")
    for i in range(len(F1ListSorted)):
        print(F1ListSorted[i].ReturnRace())


    #final Answer for option 2

    print("Here is a List of the races that have more laps than the value you gave us and they are sorted alphabetically.")
    for i in range(len(F1ListSorted)):
        print(F1ListSorted[i].ReturnRace())



#   Menu option 3 : Calculates the average lap time per race then saves this new information as a
#   7th column in file partA_output_data.tx t . After saving into the file, it should also read back
#   and display all 7 columns of data on the screen (the 6 original columns + the new one based
#   on the calculations).

#def option3():



#   Menu option 4: Asks the user for a field to sort by, then whether the order should be ascending
#   or descending. Displays on screen all data contained in the file sorted according to the user's
#   instructions. This option refers to the 7-column file generated in option 3 and assumes it exists,
#   otherwise the program should inform the user to execute option 3 first and then get back to
#   option 4.

#def option4():


#   Menu option 5 : Calculates the total average lap time per driver -across all Grand Prix races- and
#   presents it as a GUI column graph in a pop-up window (x-axis: driver names. y-axis: average
#   lap time in minutes).

#def option5():



def option6():
    print("You chose to exit. See you next time")
    sys.exit()


def main():
    CreatePartAFile()
    print("option 1 Test")
    option1()
    print("FileToList Test")
    FileToList()
    for i in range(len(F1List)):
        print(F1List[i].ReturnRace())
    option2()

filename = "partA_input_data.txt"



if __name__ == "__main__":
    main()