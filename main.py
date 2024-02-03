# Libraries and dependencies
import data as d
import functions as f
import pandas as pd

# Define the pillars
pillar1 = 'Delay_from_due_date'
pillar2 = 'Num_of_Delayed_Payment'
pillar3 = 'Outstanding_Debt'
pillar4 = 'Credit_History_Age'
pillar5 = 'Credit_Mix'
pillar6 = 'Num_Credit_Inquiries'
pillars = [pillar1,pillar2,pillar3,pillar4,pillar5,pillar6]
# Define the ranges of every pillar
range1 = [range(0,1),range(1,4),range(4,16),range(16,31),range(31,61),range(61,91)]
range2 = [range(0,1),range(1,2),range(2,6),range(6,11)]
range3 = [range(0,281),range(281,1156),range(1156,1431),range(1431,2586),range(2586,3781)]
range4 = [range(0,13),range(13,25),range(25,37),range(37,73),range(73,109),range(109,121)]
range5 = ['Bad','Standard','Good']
range6 = [range(0,1),range(1,3),range(3,6),range(6,11),range(11,14)]
ranges = [range1,range2,range3,range4,range5,range6]
# Define the score of every different range 
values1 = [200,150,100,75,50,25,10]
values2 = [150,125,100,50,25]
values3 = [300,250,200,150,100,50]
values4 = [40,50,60,70,80,90,100]
values5 = [50,100,150]
values6 = [75,100,75,50,25,10]
values = [values1,values2,values3,values4,values5,values6]
# Get the numerical scores of every person
data = [d.train[p] for p in pillars]
num_score = [[f.score(r,v,x) for x in xi] for r,v,xi in zip(ranges,values,data)]
final_scores = [sum(x) for x in zip(*num_score)]
# Asign the Final Score 
range7 = [range(0,601),range(601,800)]
values7 = ['Poor','Standard','Good']
original_score = d.train['Credit_Score'].values
model_score = [f.score(range7,values7,x) for x in final_scores]
# Load the original score and the score the model gives on a dataframe
df = pd.DataFrame({'Original Score':original_score,
                   'Model Score':model_score})
# Find the accuracy of the model
accuracy = sum([1 if x==y else 0 for x,y in zip(original_score,model_score)])/len(original_score)