import pandas as pd  
import matplotlib.pyplot as plt
#import sklearn 
import seaborn as sns
import scipy 
import numpy as np

#load data 
stitanic_test_file_path = 'test.csv'
stitanic_train_file_path = 'train.csv'

stitanic_data = pd.read_csv(stitanic_train_file_path)
df_test = pd.read_csv(stitanic_test_file_path)


#clean and explore data


# Home planet
#class str
#check gt lớn nhất 
#print(stitanic_data['HomePlanet'].value_counts()) : Earth là nhiều nhất 
#fill
#create new col
#drop oldcol

stitanic_data['HomePlanet'] = stitanic_data['HomePlanet'].fillna("Earth")
stitanic_homeplanet = pd.get_dummies(stitanic_data['HomePlanet'] , dtype = float)
stitanic_data = pd.concat([stitanic_data , stitanic_homeplanet ] ,axis = 1)
del stitanic_data["HomePlanet"]

#test
df_test['HomePlanet'] = df_test['HomePlanet'].fillna("Earth")
df_homeplanet = pd.get_dummies(df_test['HomePlanet'] , dtype = float)
df_test = pd.concat([df_test , df_homeplanet] ,axis = 1) 
del df_test['HomePlanet'] 


#stitanic_data = pd.concat([stitanic_data, pd.get_dummies(stitanic_data['HomePlanet'] , dtype = float) ], axis=1 )

#cryosleep
#class bool 
#check the quantity of 0 and 1
#stitanic_data['CryoSleep'].value_counts()
# number of zero >number of 1
#replace  nan = 0 
stitanic_data['CryoSleep'] = stitanic_data['CryoSleep'].fillna(0)
stitanic_data['CryoSleep'] = stitanic_data['CryoSleep'].replace([False,True],[ 0 , 1 ])
#test
df_test['CryoSleep'] = df_test['CryoSleep'].fillna(0)
df_test['CryoSleep'] = df_test['CryoSleep'].replace([False,True],[ 0 , 1 ])



#Cabin
# split cabin -> deck  , num , side

stitanic_data['C_Deck'] = stitanic_data['Cabin'].str[0] 
stitanic_data['C_Num'] = stitanic_data['Cabin'].str[2 : -2]
stitanic_data['C_Side'] = stitanic_data['Cabin'].str[-1]

#drop cabin
#del stitanic_data['Cabin'] 
#check gt lon nhat F G E B C D A T 
#print(stitanic_data['C_Deck'].value_counts())
#check gt lon nhat  S : 4288 P :4206
#print(stitanic_data['C_Side'].value_counts()) 

#fill num
stitanic_data['C_Deck'] = stitanic_data['C_Deck'].fillna("F")
stitanic_data['C_Num'] = stitanic_data['C_Num'].fillna(stitanic_data['C_Num'].median()) # fill with median or số xuất hiện nhiều nhất
stitanic_data['C_Side'] = stitanic_data['C_Side'].fillna("S")
#new col deck_f

stitanic_deck = pd.get_dummies(stitanic_data['C_Deck'], prefix = "C_Deck" , dtype = float)
stitanic_data = pd.concat([stitanic_data , stitanic_deck ] ,axis = 1)

stitanic_side = pd.get_dummies(stitanic_data['C_Side'], prefix = "C_Side" , dtype = float)
stitanic_data = pd.concat([stitanic_data , stitanic_side] ,axis = 1)

#drop col
del stitanic_data['Cabin']
del stitanic_data['C_Deck']
del stitanic_data['C_Side']

#test
#split -> deck , num , side 
df_test['C_Deck'] = df_test['Cabin'].str[0] 
df_test['C_Num'] = df_test['Cabin'].str[2 : -2]
df_test['C_Side'] = df_test['Cabin'].str[-1]

#fill
# F G  E  B  C  D  A  T
#print(df_test['C_Deck'].value_counts())

#fill
df_test['C_Deck'] = df_test['C_Deck'].fillna("F")
df_test['C_Num'] = df_test['C_Num'].fillna(df_test['C_Num'].median()) # fill with median or số xuất hiện nhiều nhất
df_test['C_Side'] = df_test['C_Side'].fillna("S") # fill S hay random vì S 2093 P 2084

#
df_deck = pd.get_dummies(df_test['C_Deck'], prefix = "C_Deck", dtype = float)
df_test = pd.concat([df_test , df_deck],axis = 1) 
 
df_side = pd.get_dummies(df_test['C_Side'], prefix = "C_Side", dtype = float) # có nên để trong 1 cột ko ?
df_test = pd.concat([df_test , df_side],axis = 1) 

#drop col
del df_test['Cabin']
del df_test['C_Deck']
del df_test['C_Side']


#Destination
#class str 
#check gt lon nhat 
#print(stitanic_data['Destination'].value_counts()) TRAPPIST-1e
#fill
#newcol
#drop oldcol

stitanic_data['Destination'] = stitanic_data['Destination'].fillna('TRAPPIST-1e')
stitanic_destination = pd.get_dummies(stitanic_data['Destination'], dtype = float)
stitanic_data = pd.concat([stitanic_data ,stitanic_destination ],axis = 1) 
del stitanic_data['Destination']

#test
df_test['Destination'] = df_test['Destination'].fillna('TRAPPIST-1e')
df_destination = pd.get_dummies(df_test['Destination'], dtype = float)
df_test = pd.concat([df_test , df_destination],axis = 1) 
del df_test['Destination']

#Age
#class int
stitanic_data['Age'] = stitanic_data['Age'].fillna(stitanic_data['Age'].median())
df_test['Age'] = df_test['Age'].fillna(df_test['Age'].median())

#Vip
#class bool
#stitanic_data['VIP'].value_counts()
#print( stitanic_data['VIP'].value_counts())  false > true 
stitanic_data['VIP'] = stitanic_data['VIP'].fillna(0)
stitanic_data['VIP'] = stitanic_data['VIP'].replace([False,True],[ 0 , 1 ])
df_test['VIP'] = df_test['VIP'].fillna(0)
df_test['VIP'] = df_test['VIP'].replace([False,True],[ 0 , 1 ])


#RoomService 
#class int
stitanic_data['RoomService'] = stitanic_data['RoomService'].fillna(stitanic_data['RoomService'].median())
df_test['RoomService'] = df_test['RoomService'].fillna(df_test['RoomService'].median())

#FoodCourt
#class int
stitanic_data['FoodCourt'] = stitanic_data['FoodCourt'].fillna(stitanic_data['FoodCourt'].median())
df_test['FoodCourt'] = df_test['FoodCourt'].fillna(df_test['FoodCourt'].median())

#ShoppingMall
#class int
stitanic_data['ShoppingMall'] = stitanic_data['ShoppingMall'].fillna(stitanic_data['ShoppingMall'].median())
df_test['ShoppingMall'] = df_test['ShoppingMall'].fillna (df_test['ShoppingMall'].median())

#Spa
#class int
stitanic_data['Spa'] = stitanic_data['Spa'].fillna(stitanic_data['Spa'].median())
df_test['Spa'] = df_test['Spa'].fillna( df_test['Spa'].median() )

#VRDeck

stitanic_data['VRDeck'] = stitanic_data['VRDeck'].fillna(stitanic_data['VRDeck'].median())
df_test['VRDeck'] = df_test['VRDeck'].fillna( df_test['VRDeck'].median() )

#Name
#drop
del stitanic_data["Name"]
del df_test['Name']


#Transported
stitanic_data['Transported'] = stitanic_data['Transported'].replace([False,True],[ 0 , 1 ])


#xem data có make sense ko
#plot 3 variables

 
#correlation analysis
stitanic_cor = stitanic_data.corr(method='pearson')
plt.figure(figsize=(len (stitanic_data.columns) ,len (stitanic_data.columns)))
plt.title( "correlation analysis")
sns.heatmap(data=stitanic_cor, annot=True)


#count = 0 
#stitanic_cor.columns :
#for coll in stitanic_cor.columns :
#    for row in stitanic_cor.columns : #range (len (stitanic_cor[coll]) ) :
#       if stitanic_cor[coll][row] >= 0.3 and stitanic_cor[coll][row] != 1:
#           count += 1
#           print ( coll , row , sep = ' ')
#           print ( " - " , str(stitanic_cor[coll][row]) , end = '\n')
    
#print (" count = " , str(count) )


#algorithm


#metric accuracy

from sklearn.metrics import accuracy_score


#split data into train and test (8:2)

from sklearn.model_selection import train_test_split

stitanic_data_base =  [ item for item in stitanic_data.columns if item != 'Transported' and item != 'PassengerId']
X = stitanic_data[stitanic_data_base] 

y = stitanic_data['Transported']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2 , random_state = 42)

#logistic regression
from sklearn.linear_model import LogisticRegression

model_logistic = LogisticRegression()
model_logistic.fit(X_train, y_train)
predict_log_train = model_logistic.predict(X_train)
predict_log_test = model_logistic.predict(X_test) 
#predict_ans = model_logistic.predict(df_test)
train_log_pt = accuracy_score (predict_log_train , y_train )
test_log_pt = accuracy_score (predict_log_test , y_test )
print ( train_log_pt, test_log_pt , sep = '\n')


# 

#decision tree 
'''
from sklearn.tree import DecisionTreeClassifier

model_tree = DecisionTreeClassifier( max_depth = 5, random_state = 1)
model_tree.fit(X_train , y_train)
predict_tree_train = model_tree.predict(X_train)
predict_tree_test= model_tree.predict(X_test)
train_tree_pt = accuracy_score(predict_tree_train , y_train)
test_tree_pt = accuracy_score(predict_tree_test , y_test)
print ( train_tree_pt , test_tree_pt , sep = '\n')
'''

#submission 
#choosing model 

#predict_ans = model_logistic.predict(df_test)
#print(predict_ans)



#missing_cnt = stitanic_data.isnull().sum()

#print(stitanic_data['Transported'].head())
#print (stitanic_data.describe()) 
#print(missing_cnt)

