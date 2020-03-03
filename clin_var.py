import os 
import pandas as pd 
from sklearn.model_selection import train_test_split

data = pd.read_csv('/Users/mattcarroll/Downloads/clinvar_conflicting.csv')



data_x = data.drop(['CLASS'],axis = 1)
data_y = data['CLASS']



#class is a binary representation. if multiple people deem it to be of different threats, you get 1, if they match you get 0 for class 
#split data into training and testing groups
xTrain, xTest, yTrain, yTest = train_test_split(data_x, data_y, test_size = 0.2, random_state = 56)

#ok data loaded and seperated into testing a training groups 
#lets begin getting to know the data and cleaning it up a bit 
#a large portion of the data is categorical, with the rest being mostly floats 
#we can try initially just using the floats to model

xTrain_numerical = xTrain.select_dtypes(exclude = ['object'])
xTest_numerical = xTest.select_dtypes(exclude = ['object'])

#this will be a priative model, but we still have a large number of missing values to work with 
#I will impute the values for the missing values 

cols_missing_values = ['ORIGIN', 'SSR','DISTANCE','STRAND','STRAND','MOTIF_POS','MOTIF_SCORE_CHANGE','LoFtool','CADD_PHRED','CADD_RAW','BLOSUM62']

for i in cols_missing_values:
    xTrain_numerical[i].fillna(xTrain[i].mean(),inplace = True)
    xTest_numerical[i].fillna(xTest[i].mean(),inplace = True)

    #still unclear to me if i want to impute values for my test subset of data
    
