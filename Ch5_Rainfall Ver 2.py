# Michael King -  RAINFALL CALCULATIONS - PYTHON 3
# Use Nested Loops to calculate average rainfall over a period of years.



def totalYears():
    while True:
        try:
            years = int(input("\nPlease enter the number of years to calculate rainfall:\n"))
            while years > 0:
                return years
            else:
                print("Please Enter a number greater than 0.")
        except ValueError:
            print("Please enter a number")

def getRainFall(month):
     #pass number to add the month to input string, to help user.
     months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

     while True:
          try:
               rain = int(input(f"How many inches of rain in {months[month]} ?\n"))
               while rain >= 0:
                    return rain
               else:
                    print("Please Enter a Positive Number")
          except ValueError:
               print("Please enter a number")


def calcAvgRain(number_of_years):
    #calculate and return average monthly rainfall over period of years.

     #loop to collect rainfall for x years

     totalMonths = number_of_years * 12
     totalRain = 0
     
     #Loop iterates once for each year

     for year in range(number_of_years):
          print(f"Enter Values for Year {year+1}\n")
               
               #Inner Loop iterates 12 times, once per each month
          for month in range(12):

               #Inner loop Calls Function: getRainFall() to get rainfall of the month
               rain = getRainFall(month)

               # that rainfall gets added (accumulated) to the total_rainfall
               totalRain = totalRain + rain
          #except:
           #    print("ERROR")

     #After ALL Iterations: Display number of months, total Inches of Rainfall,           
     print(f"Total months: {totalMonths} | Total Inches: {totalRain} | Average Monthly Rainfall {totalRain / totalMonths:.2f}")


#Main Module calls the above functions in proper order.      
calcAvgRain(totalYears())

       
