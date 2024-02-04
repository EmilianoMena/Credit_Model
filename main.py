# Libraries and dependencies
import data as d
import functions as f
import pandas as pd

# Define the variables
var1 = 'Delay_from_due_date'
var2 = 'Num_of_Delayed_Payment'
var3 = 'Outstanding_Debt'
var4 = 'Credit_History_Age'
var5 = 'Credit_Mix'
var6 = 'Num_Credit_Inquiries'
vars = [var1,var2,var3,var4,var5,var6]

# Data of the variables selected
data = [d.train[p].values for p in vars]

# Functions
funcs = [f.f1,f.f2,f.f3,f.f4,f.f5,f.f6]
all_scores = [[fc(x) for x in xi]for xi,fc in zip(data,funcs)]
final_score = [sum(x) for x in zip(*all_scores)]
model_score = [f.f7(x) for x in final_score]
original_score = d.train['Credit_Score'].values

# Load the original score and the score the model gives on a dataframe
df = pd.DataFrame({'Score Points':final_score,
                   'Model Score':model_score,
                   'Original Score':original_score})

# Find the accuracy of the model
accuracy = sum([1 if x==y else 0 for x,y in zip(original_score,model_score)])/len(original_score)*100