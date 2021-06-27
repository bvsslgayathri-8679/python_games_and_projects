import numpy as np
import pandas as pd 

dataframe=pd.read_csv('matches.csv')
newds=dataframe[['team1','team2','toss_decision','toss_winner','winner']]

newds.dropna(inplace=True)


allteams={}

cnt=0
for i in range(len(dataframe)):
    if dataframe.loc[i]['team1'] not in allteams:
        allteams[dataframe.loc[i]['team1']]=cnt
        cnt+=1
    if dataframe.loc[i]['team2'] not in allteams:
        allteams[dataframe.loc[i]['team2']]=cnt
        cnt+=1    


X=newds[['team1','team2','toss_winner','winner']]

Y=newds[['winner']]

encoded_teams={w:k for k,w in allteams.items()}

X=np.array(X)
Y=np.array(Y)

for i in range(len(X)):
    X[i][0]=allteams[X[i][0]]
    X[i][1]=allteams[X[i][1]]
fb={'field':0,'bat':1}

for i in range(len(X)):
    X[i][2]=fb[X[i][2]]

  



for i in range(len(X)):
    if X[i][3]==X[i][0]:
        X[i][3]=0
    else:
        X[i][3]=0
 


ones, zeros = 0,0
for i in range(len(X)):
    if Y[i] == X[i][0] :
        if zeros <= 375:
            Y[i] = 0
            zeros += 1
        else:
            Y[i] = 1
            ones += 1
            t = X[i][0]
            X[i][0] = X[i][1] 
            X[i][1] = t
        
    
        
    if Y[i] == X[i][1] :
        if ones <= 375:
            Y[i] = 1
            ones += 1
        else:
            Y[i] = 0
            zeros += 1
            t = X[i][0]
            X[i][0] = X[i][1] 
            X[i][1] = t



X = np.array(X, dtype='int32')
Y = np.array(Y, dtype='int32')
Y_backup = Y.copy()

Y = Y_backup.copy()



from sklearn.preprocessing import LabelEncoder
teams = LabelEncoder()
teams.fit(allteams)

encoded_teams = teams.transform(allteams)

with open('vocab.pkl', 'wb') as f:
    pkl.dump(encoded_teams, f)
with open('inv_vocab.pkl', 'wb') as f:
    pkl.dump(allteams, f)
    

from sklearn.model_selection import train_test_split
X_train, X_test, y_train,y_test = train_test_split(X, y, test_size=0.05)


from sklearn.svm import SVC
model1 = SVC().fit(X_train, y_train)
model1.score(X_test, y_test)

from sklearn.tree import DecisionTreeClassifier
model2 = DecisionTreeClassifier().fit(X_train, y_train)
model2.score(X_test, y_test)

from sklearn.ensemble import RandomForestClassifier
model3 = RandomForestClassifier(n_estimators=250).fit(X, y)
model3.score(X_test, y_test)





test = np.array([2,4, 1, 4]).reshape(1,-1)
model1.predict(test)
model2.predict(test)
model3.predict(test)



import pickle as pkl

with open('model.pkl', 'wb') as f:
    pkl.dump(model3, f)



with open('model.pkl', 'rb') as f:
    model = pkl.load(f)



model.predict(test)
