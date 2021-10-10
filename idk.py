import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    hours_of_sleep = []
    cups_of_coffee = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            cups_of_coffee.append(float(row["Coffee in ml"]))
            hours_of_sleep.append(float(row["sleep in hours"]))
    return {"x": cups_of_coffee, "y": hours_of_sleep}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation between Cups of Coffee vs Hours of Sleep: \n--->", correlation[0,1])

def plotFigure(data_path):
   with open(data_path) as csv_file:
       df = csv.DictReader(csv_file)
       fig = px.scatter(df, x = "Cups of Coffee", y = "Hours of Sleep") 
       fig.show()

def setup():
    data_path = "cups of coffee vs hours of sleep.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
    plotFigure(data_path)
setup()