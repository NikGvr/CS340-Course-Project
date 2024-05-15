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
    def __init__(self, day, month, year):
        self.DayNum = day
        if day <= 9:
            self.DayStr = "0" + str(day)
        else:
            self.DayStr = str(day)
        self.month = month
        self.year = year

    def ShowDate(self):
        print(self.DayStr, "-", self.month, "-", self.year)

    def ReturnDate(self):
        ReturnString = (self.DayStr, "-", self.month, "-", self.year)
        return ReturnString


class Time:
    def __init__(self, min, sec, millisec):
        self.MinNum = min
        if min <= 9:
            self.MinString = "0" + str(min)
        else:
            self.MinString = str(min)
        self.Seconds = sec
        self.Millisec = millisec

    def ShowTime(self):
        print(self.MinString, "-", self.Seconds, "-", self.Millisec)

    def ReturnTime(self):
        ReturnString = (self.MinString, ":", self.Seconds, ".", self.Millisec)
        return ReturnString


class Race:

    def __init__(self, GrandPrix, Date, Winner, Car, Laps, Time):
        self.GrandPrix = str(GrandPrix)
        self.Date = Date
        self.Winner = str(Winner)
        self.Car = str(Car)
        self.Laps = int(Laps)
        self.Time = Time



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
    F1List = []
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
        print(f"{fields[0]:<15} {fields[1]:<15} {fields[2]:<20} {fields[3]:<20} {fields[4]:<15} {fields[5]:<15}")


    fout.close()

#Menu option 2: Asks the user for a limit of laps to search by, then displays only the race results
#which involve that number of home laps or greater, sorted alphabetically by Grand Prix name.

#def option2():



#def option3():



#def option4():



#def option5():



def option6():
    print("You chose to exit. See you next time")
    sys.exit()


def main():
    CreatePartAFile()
    print("option 1 Test")
    option1()
    print("FileToList Test")
    print(F1List)

filename = "partA_input_data.txt"



if __name__ == "__main__":
    main()