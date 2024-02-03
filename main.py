# Libraries and dependencies
import data as d
import functions as f

# pillar1 = 'Delay_from_due_date'
# range1 = [range(0,1),range(1,4),range(4,16),range(16,31),range(31,61),range(61,91)]
# values1 = [200,150,100,75,50,25,10]
# score = [f.score(range1,values1,x) for x in d.train[pillar1].values]

# pillar2 = 'Num_of_Delayed_Payment'
# range2 = [range(0,1),range(1,2),range(2,6),range(6,11)]
# values2 = [150,125,100,50,25]
# score2 = [f.score_num(range2,values2,x) for x in d.train[pillar2].values]

# pillar3 = 'Outstanding_Debt'
# range3 = [range(0,281),range(281,1156),range(1156,1431),range(1431,2586),range(2586,3781)]
# values3 = [300,250,200,150,100,50]
# score3 = [f.score_num(range3,values3,x) for x in d.train[pillar3].values]

# pillar4 = 'Credit_History_Age'
# range4 = [range(0,13),range(13,25),range(25,37),range(37,73),range(73,109),range(109,121)]
# values4 = [40,50,60,70,80,90,100]
# score4 = [f.score_num(range4,values4,x) for x in d.train[pillar4].values]

pillar5 = 'Credit_Mix'
range1 = ['Bad','Standard','Good']
values5 = [50,100,150]
score5 = [f.score_txt(range1,values5,x) for x in d.train[pillar5].values]
score = [f.score(range1,values5,x) for x in d.train[pillar5].values]
print(sum([0 if a==b else 1 for a,b in zip(score5,score)]))

# pillar6 = 'Num_Credit_Inquiries'
# range6 = [range(0,1),range(1,3),range(3,6),range(6,11),range(11,14)]
# values6 = [75,100,75,50,25,10]
# score6 = [f.score_num(range6,values6,x) for x in d.train[pillar6].values]

# final_score = [s1+s2+s3+s4+s5+s6 for s1,s2,s3,s4,s5,s6 in zip(score1,score2,score3,score4,score5,score6)]
# range7 = [range(0,601),range(0,801)]
# values7 = ['Poor','Standard','Good']

