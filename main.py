import pandas as pd  #clean data
import numpy as np   #clean data
import matplotlib.pyplot as plt
#import sklearn 
import seaborn as sns
import scipy 

#load data 
stitanic_test_file_path = 'test.csv'
stitanic_train_file_path = 'train.csv'

stitanic_data = pd.read_csv(stitanic_train_file_path)


#clean and explore data

# check null 

missing_cnt = stitanic_data.isnull().sum()

# loại data có ít nhất 1 hàng có gt null )



stitanic_first_data_ = stitanic_data.dropna()


#xoá tuổi = 0

#print(stitanic_data.describe())

             

#xem data có make sense ko

#plot 3 variables

#Age
#cabin 
#vip 
#cyrosleep

stitanic_new_data_features = ['Age' ,'CryoSleep','Cabin','VIP']

X = stitanic_data[stitanic_new_data_features]

print(X.describe()) 
#correlation analysis

#algorithm
#metric accuracy
#split data into train and test (8:2)
#logistic regression

# 

#decision tree 



