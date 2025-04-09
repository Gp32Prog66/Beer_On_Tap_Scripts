#Important Librarys. Use pip to install. For Arch Linux, type sudo pacman -S python-stats, then python-numpy 
import numpy
from scipy import stats
import statistics

#MySQL/Misc. Database Connection
import mysql.connector #sudo pacman -S python-mysql-connector

brewDB = mysql.connector.connect(
    host="",
    user="",
    password="",
    database=""
)

brewCursor = brewDB.cursor()

sql = "SELECT * FROM all_beer_on_tap"

results = brewCursor.fetchall()

brewCursor.execute(sql)

#Printing Introduction
print('Hello and welcome to the all tap brewery database')


#Have User Selection
userChoice = int(input(""" What brewing data would you like to see? 
1.Mean
2.Median
3.Mode
4.Standard Deviation
5.Variance
6.Percentile
"""))

#Data Arrays
abvData = [5,5,5,5]
ibuData = [10,10,10,10]

#ABV Calculations
abvMean = numpy.mean(abvData)
abvMedian = numpy.median(abvData)
abvMode = statistics.mode(abvData)
abvVariance = numpy.std(abvData)
abvPercentile = numpy.var(abvData)

#IBU Calculations
ibuMean = numpy.mean(ibuData)
ibuMedian = numpy.median(ibuData)
ibuMode = statistics.mode(ibuData)
ibuVariance = numpy.std(ibuData)
ibuPercentile = numpy.var(ibuData)

if userChoice == 1:
    print("Mean Selected")
    # data_selection()
elif userChoice == 2:
    print("Median Selected")
elif userChoice == 3:
    print("Mode Selected")
elif userChoice == 4:
    print("Standard Deviation Selected")
elif userChoice == 5:
    print("Variance Selected")
elif userChoice == 6:
    print("Percentile Selected")
else:
    print("Cheers")

def data_selection():
    print("""What data do you want to calculate?
1.ABV
2.IBU """)

dataChoice = int(input("What Data Do You Want To Select? "))

if dataChoice == 1:
    print("ABV Data Selected")
    
elif dataChoice == 2:
    print("IBU Data Selected")
else:
    print("Invalid Choice")
    
