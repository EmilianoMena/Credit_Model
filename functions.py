# Libraries and dependencies
import data as d
import pandas as pd

def get_data(pillar):
    return pd.DataFrame([d.train[p] for p in pillar]).T

def score_num(ranges,values,variable):
    list_dict = [{key:value for key in list(keys)} for keys,value in zip(ranges[:-1],values[:-1])]
    dict = {key: value for dict in list_dict for key, value in dict.items()}
    score = dict.get(variable,values[-1])
    return score

def score_txt(score,values,variable):
    dict = {key: value for key, value in zip(score,values)}
    score = dict.get(variable,values)
    return score

def score(ranges,values,variable):
    if isinstance(variable,str):
        dict = {key: value for key, value in zip(score,values)}
        score = dict.get(variable,values)
        return score
    else:
        list_dict = [{key:value for key in list(keys)} for keys,value in zip(ranges[:-1],values[:-1])]
        dict = {key: value for dict in list_dict for key, value in dict.items()}
        score = dict.get(variable,values[-1])
        return score
