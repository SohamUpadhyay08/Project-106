import csv
import plotly.express as px
import numpy as np

def plotFigure(data_path):
    with open(data_path) as f:
        df = csv.DictReader(f)
        graph = px.scatter(df,y="Days Present",x="Marks In Percentage",color="Roll No")
        graph.show()

def getDataSource(data_path):
    DaysPresent = []
    Marks = []
    with open(data_path) as f:
        reader = csv.DictReader(f)
        for row in reader :
            DaysPresent.append(float(row["Days Present"]))
            Marks.append(float(row["Marks In Percentage"])) 
    return {"y":DaysPresent,"x":Marks}

def findCorellation(data_source):
    corellation = np.corrcoef(data_source["x"],data_source["y"])
    print(corellation[0,1])

def main():
    data_path= "studentPercentage.csv"
    data_source = getDataSource(data_path)
    findCorellation(data_source)
    plotFigure(data_path)

main()