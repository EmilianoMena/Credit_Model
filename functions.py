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