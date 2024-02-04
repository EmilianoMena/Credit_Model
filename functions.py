# Libraries and dependencies
import data as d
import pandas as pd

def score(ranges,values,variable):
    if isinstance(variable,(int,float))==True:
        list_dict = [{key:value for key in list(keys)} for keys,value in zip(ranges,values[:-1])]
        dict = {key: value for dict in list_dict for key, value in dict.items()}
        score = dict.get(variable,values[-1])
        return score
    else:
        dict = {key: value for key, value in zip(ranges,values)}
        score = dict.get(variable,0)
        return score
    
f1 = lambda x: 200 if x <= 3 else 150 if x <= 10 else 100 if x <= 30 else 75 if x <= 60 else 50 if x <=90 else 25
f2 = lambda x: 150 if x <= 1 else 100 if x <= 5 else 50 if x <= 10 else 25
f3 = lambda x: 300 if x <= 500 else 275 if x <= 1000 else 250 if x <= 1500 else 150 if x <= 2000 else 75 if x <=2500 else 50
f4 = lambda x: 15 if x <= 24 else 30 if x <= 48 else 45 if x <= 72 else 60 if x <= 96 else 85 if x <=120 else 100
f5 = lambda x: 150 if x == 'Good' else 100 if x == 'Standard' else 50
f6 = lambda x: 100 if x <= 3 else 75 if x <= 6 else 50 if x <= 9 else 25 
f7 = lambda x: 'Poor' if x<600 else 'Standard' if x<800 else 'Good'