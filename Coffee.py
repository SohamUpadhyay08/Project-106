import csv
import plotly.express as px
import numpy as np

def plotFigure(data_path):
    with open(data_path) as f:
        df = csv.DictReader(f)
        graph = px.scatter(df,x="Coffee in ml",y="sleep in hours",color="week")
        graph.show()

def getDataSource(data_path):
    CoffeeConsumption = []
    sleepingHours = []
    with open(data_path) as f:
        reader = csv.DictReader(f)
        for row in reader :
            CoffeeConsumption.append(float(row["Coffee in ml"]))
            sleepingHours.append(float(row["sleep in hours"])) 
    return {"x":CoffeeConsumption,"y":sleepingHours}

def findCorellation(data_source):
    corellation = np.corrcoef(data_source["x"],data_source["y"])
    print(corellation[0,1])

def main():
    data_path= "Coffee.csv"
    data_source = getDataSource(data_path)
    findCorellation(data_source)
    plotFigure(data_path)

main()
