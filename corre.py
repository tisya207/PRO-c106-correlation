import csv
import numpy as np 

def getDataSource(datapath):
    coffee_quant=[]
    sleep_hrs=[]
    with open(datapath) as dp:
        reader= csv.DictReader(dp)
        for row in reader:
            coffee_quant.append(float(row['Coffee in ml']))
            sleep_hrs.append(float(row['sleep in hours']))
    return{'x':coffee_quant, 'y':sleep_hrs}

def get_correlation(datasource):
    correlation= np.corrcoef(datasource['x'], datasource['y'])
    print('Correlation between data, quantity of coffee affecting hours of sleep is '+ str(correlation[0,1]))


def setup():
    datapath='cups of coffee vs hours of sleep.csv'
    datasource= getDataSource(datapath)
    get_correlation(datasource)

setup()

