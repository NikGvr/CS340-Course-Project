# Gavriilidis Nikolaos
# 20220427@student.act.edu
# Part A for Pyhton project

# imports that will be needed ( suposedly )

import matplotlib.pyplot as plot

# Debug boolean because It is more efficient for me and many other people.

Debug =  True

# A running boolean because it will be needed.

Running = True

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

# A dictionary that will be used for option 5 and it will have the driver names and the average lap time (x-axis: driver names. y-axis: average lap time in minutes)

F1AverageLapTimes = {}

#option selected value

OptionSelected = 0

# creating the classes that will be used in the lists, mostly date, time, race, Driver.

# Date class

class Date:
    # variables used by the class

    DayNum = 0
    DayStr = ""
    MonNum = 0
    MonStr = ""
    YearNum = 0
    YearStr = ""

    # list of months that will be used to calculate the variable MonNum

    MonthsList = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    # constructor for the class

    def __init__(self, day, month, year):

        # puttin the day as a number and as a string

        self.DayNum = int(day)

        # making the day into a string

        if (int(day) <= 9):

            self.DayStr = ("0" + str(int(day)))

        else:
            self.DayStr = str(day)

        # making the month string

        self.MonStr = str(month)

        # making the month number based on the list.

        for i in range(len(self.MonthsList)):

            if (self.MonthsList[i] == str(month)):
                MonthIndex = i

        self.MonNum = MonthIndex

        # making the year num and str

        self.YearNum = int(year)

        self.YearStr = str(year)

        # a function to return date in the format that is in te file.

        def ReturnDate(self):

            ReturnString = f"{self.DayStr}-{self.MonStr}-{self.YearStr}"

            return ReturnString

        # found out that I could compare touples for the sorting ( option 4 )

        def ToTuple(self):
            return (self.YearNum, self.MonNum, self.DayNum)


# the time class

class Time:
    # variables that will be used in the time class.

    MinNum = 0
    MinStr = ""
    SecNum = 0
    SecStr = ""
    MillisecNum = 0
    MillisecStr = ""
    OnlyMillisecs = 0

    # constructor for the class

    def __init__(self, minutes, seconds, milliseconds):

        # creating the minutes number and string

        self.MinNum = int(minutes)

        if (int(minutes) <= 9):

            self.MinStr = ("0", str(int(minutes)))

        else:

            self.MinStr = str(int(minutes))

        # creating the seconds number and string

        self.SecNum = int(seconds)

        if (int(seconds) <= 0):

            self.SecStr = ("0", str(int(seconds)))

        else:

            self.SecStr = str(int(seconds))

        # creating the milliseconds number and string

        self.MillisecNum = int(milliseconds)

        self.MillisecStr = str(milliseconds)

        self.OnlyMillisec = int(self.ConvertToMilisecs())

    # function to convert time in Milliseconds.

    def ConvertToMilisecs(self):

        ReturnNumber = int((self.MinNum * 60 * 1000) + (self.SecNum * 1000) + self.MillisecNum)

        return ReturnNumber

    # function to return the time in the format of the file

    def ReturnTime(self):

        ReturnString = f"{self.MinStr}:{self.SecStr}.{self.MillisecStr}"

        return ReturnString


# race class to save the races.

class Race:
    # variables used by the race class.

    GrandPrix = ""  # name of the race

    Date = Date  # the date of the race

    Winner = ""  # the name of the winner

    Car = ""  # the name of the car ( the team name )

    Laps = 0  # the number of laps

    Time = Time  # the time it took

    AverageLapTime = 0.0  # the average lap time ( needed for option 3 )

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

        # creating the average lap time per race.

        self.AverageLapTime = float(int(Time.ConvertToMilisecs()) / int(Laps)) / 60000.0

    # function to return race as a string.

    def ReturnRace(self):
        StringToReturn = (
            f"{self.GrandPrix:<15} {self.Date.ReturnDate():<15} {self.Winner:<20} {self.Car:<20} {self.Laps:<5} {self.Time.ReturnTime():<15}")

        return StringToReturn

    # function to output data to the output file in option 3

    def ReturnRaceOutput(self):
        StringToReturn = (
            f"{self.GrandPrix:<15} {self.Date.ReturnDate():<15} {self.Winner:<20} {self.Car:<20} {self.Laps:<5} {self.Time.ReturnTime():<15}")

        return StringToReturn


# a class for the driver data ( needed for option 5)

class Driver:
    # variables used by the driver class.

    DriverName = ""
    TotalLaps = 0
    TotalTime = 0
    AverageLapTime = 0

    def __init__(self, name, laps, time):
        self.DriverName = str(name)

        self.TotalLaps = int(laps)

        self.TotalTime = time.ConvertToMilisecs()

        self.AverageLapTime = float(self.TotalLaps / self.TotalTime)

    def AddTimeAndLaps(self, laps, time):
        self.TotalLaps = int(self.TotalLaps) + int(laps)

        self.TotalTime = self.TotalTime + time.ConvertToMillisecs()

        # updating the average lap time after the addition

        self.AverageLapTime = float(self.TotalLaps / self.TotalTime) / 60000.0

    def ReturnAverageLapTime(self):
        ReturnNumber = float(self.TotalLaps / self.TotalTime) / 60000.0

        return ReturnNumber

    def GetDetails(self):
        ReturnString = (
            f"Name: {self.DriverName} \nLaps: {self.TotalLaps} \nTotalTimeInMilliseconds: {self.TotalTime} \n")


# Creating a function that creates the file regardless if it exists or not.

def CreateInputFile():  # Creationg of the time (it will overwrite if existent.) Based on C++ project comments.

    file = open(inputfile, "w")

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


# creating a function that reads the data from the file and puts it into the F1File.

def FileToList():  # Taking the F1File list and appending the data from the PartA file.

    file = open(inputfile, "r")

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

        F1File.append(RaceToAppend)

    file.close()


# making a function that reads the data from the file, puts it into the F1FileSorted and sorts it for the option 2 usage.

def F1FileSortedCreation(F1FileSorted):
    file = open(inputfile, "r")

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

        F1FileSorted.append(RaceToAppend)

    file.close()

    # sorting the data based on the name of the drand prix.

    F1FileSorted = sorted(F1FileSorted, key=lambda x: x.GrandPrix)


# Creation of the list for option 3

# list needed: F1OutputFile = []

def F1OutputFileCreation():
    for i in range(len(F1File)):
        F1OutputFile[i] = F1File[i]

    file = open(outputfile, 'w')

    file.write("GRAND PRIX,DATE,WINNER,CAR,LAPS,TIME,AVGLAPTIME\n")

    for i in range(len(F1OutputFile)):
        StringToWrite = (
            f"{F1OutputFile[i].GrandPrix},{F1OutputFile[i].Date.ReturnDate()},{F1OutputFile[i].Winner},{F1OutputFile[i].Car},{F1OutputFile[i].Laps},{F1OutputFile[i].Time.ReturnTime()},{F1OutputFile[i].AverageLapTime}\n")

        file.write(StringToWrite)

    file.close()


# a function that will take each driver from the starting file and add the needed data into the dictionary

# First make a function that reads the list F1File and adds the needed data

# dict needed: F1AverageLapTimes

def DriverDictCreationOrUpdate():
    for i in range(len(F1File)):

        # we need a variable that will work as a string with witch we will check if a key ( diver's name ) exists inside the dictionary or not.

        FindDriver = ""

        FindDriver = str(F1File[i].Winner)

        if FindDriver in F1AverageLapTimes:

            if Debug == True:
                print(
                    "Debug: Yes the driver exists and we will add the time and laps, and create the average lap time for the driver.")
                print("Showing key and value before the update.")
                print("Key:" + FindDriver)
                print("value: " + F1AverageLapTimes[FindDriver].GetDetails())
                print("updating now")

            # updating the values

            KeyOfValueToUpdate = FindDriver

            ValueToUpdate = F1AverageLapTimes[FindDriver].AddTimeAndLaps(F1File[i].Laps, F1File[i].Time)

            if Debug == True:
                print("values updated. SHowing them now,")
                print("Key:" + FindDriver)
                print("value: " + F1AverageLapTimes[FindDriver].GetDetails())


        else:

            if Debug == True:
                print(
                    "Debug: The driver does not exist to we will create the driver and add the time and laps into the driver object.")

            # String that will be used as the key in the dict.

            DriverKey = str(F1File[i].Winner)

            # Driver Object that will be used inside the dict.

            DriverObj = Driver(F1File[i].Winner, F1File[i].Laps, F1File[i].Time)

            # creating the key value pair inside the dict

            F1AverageLapTimes.update(DriverKey, DriverObj)

            if Debug == True:
                print("Debug: The driver key pair is made and it will be shown now.")
                print("key: " + DriverKey)
                print("value: " + F1AverageLapTimes[DriverKey])


# makign the sorting algorithm for option 4

# making the sorted verion for option 4

# list needed: F1OutputFileSorted = []

def F1OutputFileSorting(F1OutputFileSorted):
    # copy the data

    for i in range(len(F1OutputFile)):
        F1OutputFileSorted.append(F1OutputFile[i])

    # now ask the used witch field does the user want to sort.

    Pass = False

    while Pass == False:

        print("Please enter a number cooresponding to the field that you want to sort the list by.")

        option = int(input(
            "1) Sort by Grand Prix Name\n2) Sort by Date\n3) Sort by Winner\n4) Sort by Car\n5) Sort by laps\n6) Sort by time\n7) Sort by Average Lap Time."))

        if option in range(1, 8):

            Pass = True

            print("Accepted option, sorting now.")

        else:

            print("incorect option please try again")

    FieldNum = option

    Pass2 = False

    AscOrDesc = ""

    while Pass2 == False:

        print("Please select whitch way you want the list to be sorted.")

        option2 = str(input("select 1 for ascending or 2 for descending."))

        if (option2 == '1'):

            Pass2 = True
            AscOrDesc = "Ascending"

        elif (option2 == '2'):

            Pass2 = True
            AscOrDesc = "Descending"
        else:

            print("invalid option please try again.")

    # now doing the sorting based on the field number

    if FieldNum == 1:

        # that means the Grand Prix value

        if AscOrDesc == "Ascending":

            # the reverse value is the one choosing which way to sort True = Desc

            F1OutputFileSorted = sorted(F1OutputFileSorted, key=lambda x: x.GrandPrix, reverse=False)

        elif AscOrDesc == "Descending":

            F1OutputFileSorted = sorted(F1OutputFileSorted, key=lambda x: x.GrandPrix, reverse=True)

    elif FieldNum == 2:

        # that is the Date Value

        if AscOrDesc == "Ascending":

            # the reverse value is the one choosing which way to sort True = Desc

            F1OutputFileSorted = sorted(F1OutputFileSorted, key=lambda x: x.Date.ToTuple(), reverse=False)

        elif AscOrDesc == "Descending":

            F1OutputFileSorted = sorted(F1OutputFileSorted, key=lambda x: x.Date.ToTuple(), reverse=True)

    elif FieldNum == 3:

        # that is the Winner value

        if AscOrDesc == "Ascending":

            # the reverse value is the one choosing which way to sort True = Desc

            F1OutputFileSorted = sorted(F1OutputFileSorted, key=lambda x: x.Winner, reverse=False)

        elif AscOrDesc == "Descending":

            F1OutputFileSorted = sorted(F1OutputFileSorted, key=lambda x: x.Winner, reverse=True)

    elif FieldNum == 4:

        # that is the Car value

        if AscOrDesc == "Ascending":

            # the reverse value is the one choosing which way to sort True = Desc

            F1OutputFileSorted = sorted(F1OutputFileSorted, key=lambda x: x.Car, reverse=False)

        elif AscOrDesc == "Descending":

            F1OutputFileSorted = sorted(F1OutputFileSorted, key=lambda x: x.Car, reverse=True)

    elif FieldNum == 5:

        # that is the Laps Value

        if AscOrDesc == "Ascending":

            # the reverse value is the one choosing which way to sort True = Desc

            F1OutputFileSorted = sorted(F1OutputFileSorted, key=lambda x: x.Laps, reverse=False)

        elif AscOrDesc == "Descending":

            F1OutputFileSorted = sorted(F1OutputFileSorted, key=lambda x: x.Laps, reverse=True)

    elif FieldNum == 6:

        # that is the time value ( OnlyMillisec will be used)

        if AscOrDesc == "Ascending":

            # the reverse value is the one choosing which way to sort True = Desc

            F1OutputFileSorted = sorted(F1OutputFileSorted, key=lambda x: x.Time.OnlyMillisecs, reverse=False)

        elif AscOrDesc == "Descending":

            F1OutputFileSorted = sorted(F1OutputFileSorted, key=lambda x: x.Time.OnlyMillisecs, reverse=True)

    elif FieldNum == 7:

        # that is the Average Lap time value.

        if AscOrDesc == "Ascending":

            # the reverse value is the one choosing which way to sort True = Desc

            F1OutputFileSorted = sorted(F1OutputFileSorted, key=lambda x: x.AverageLapTime, reverse=False)

        elif AscOrDesc == "Descending":

            F1OutputFileSorted = sorted(F1OutputFileSorted, key=lambda x: x.AverageLapTime, reverse=True)

    # now showing the data inside the F1OutputFileSorted list as asked by the instructions

    print(f"{"Grand Prix":<15}{"Date":<10}{"Winner":<20}{"Car":<10}{"Laps":<10}{"Time":<10}{"Average Lap Time":<15}")

    for i in range(len(F1OutputFileSorted)):
        StringToPrint = (
            f"{F1OutputFileSorted[i].GrandPrix:<15}{F1OutputFileSorted[i].Date.ReturnDate():<15}{F1OutputFileSorted[i].Winner:<15}{F1OutputFileSorted[i].Car:<15}{F1OutputFileSorted[i].Laps:<15}{F1OutputFileSorted[i].Time.ReturnTIme():<15}{F1OutputFileSorted[i].AverageLapTime:<15}")


# doing the bar graph for option 5

def MakeGraph():
    # getting the dirver names

    driver_names = list(F1AverageLapTimes.keys())

    # getting the average lap times

    average_lap_times = [Driver.ReturnAverageLapTime() for Driver in F1AverageLapTimes.values()]

    # Create the bar graph

    plot.figure(figsize=(10, 6))

    # setting the values used in the plot

    plot.bar(driver_names, average_lap_times, color='blue')

    # Add titles and labels

    plot.title('Average Lap Time for Each Driver')  # setting title

    plot.xlabel('Driver Name')  # setting the x-axis label

    plot.ylabel('Average Lap Time (ms)')  # setting the y-axis label

    plot.show()  # show graph


# making the option showing for the user.

def ShowOptions():
    print("======================================================================")
    print("  F1 GRAND PRIX RACING DATA & STATISTICS FOR THE 2023 RACING SEASON.  ")
    print("======================================================================")
    print("1. Read and display the F1 Grand Prix data for the 2023 racing season.")
    print("2. Filter and sort race data based on a minimum threshold of laps.")
    print("3. Calculate average lap time per race, save, retrieve, display.")
    print("4. Sort and display the data based on user parameters.")
    print("5. Calculate and graph total lap time per driver.")
    print("6. Exit the program.")


# making the OptionSelectionFunction

# making the option selection value

OptionSelected = ''

valid_options = {1, 2, 3, 4, 5, 6}


def OptionSelection(OptionSelected):
    ShowOptions()

    Pass = False

    while Pass == False:

        OptionSelected = int(input("Please input the number of the option that you want to select and run."))

        if OptionSelected in valid_options:
            print("Valid option selected. Continuing.")
            print("the value of OptionSelected is ", OptionSelected)

            Pass = True


# making the functions that correspond to the options

def Option1():
    FileToList()


def Option2():
    F1FileSortedCreation(F1FileSorted)


def Option3():
    F1OutputFileCreation()


def Option4():
    if F1OutputFile != []:

        F1OutputFileSorting(F1OutputFileSorted)

    else:

        print('Please run option 3 before running option 4')


def Option5():
    DriverDictCreationOrUpdate()

    MakeGraph()


def Option6():
    print('ByeBye, see you another time.')
    Running = False


def OptionRun(OptionSelected):

    print("the value of option selected is : ", OptionSelected)
    if OptionSelected == 1:

        print('option 1 selected')
        Option1()

    elif OptionSelected == 2:

        print("option 2 selected")
        Option2()

    elif OptionSelected == 3:

        print("option 3 selected")
        Option3()

    elif OptionSelected == 4:

        print('option 4 selected')
        Option4()

    elif OptionSelected == 5:

        print('option 5 selected')
        Option5()

    elif OptionSelected == 6:

        print('option 6 selected')
        Option6()

    else:

        print("no option selected")


# making the BootSequence before running in the main function

def BootSequence():
    CreateInputFile()


def Main():
    # running the boot sequence

    BootSequence()

    while Running == True:
        OptionSelection(OptionSelected)

        OptionRun(OptionSelected)


if __name__ == '__main__':
    Main()