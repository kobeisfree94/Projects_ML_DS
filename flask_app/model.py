import os
import sqlite3
import pandas as pd
import numpy as np
import pickle
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.metrics import classification_report
from sklearn.metrics import mean_absolute_error, r2_score, f1_score
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from scipy.stats import randint, uniform
import joblib


#Connecting to SQLite DB and bringing up DataFrames
DB_FILENAME = 'ASG1996-2021.db'
DB_FILEPATH = os.path.join(os.getcwd(), DB_FILENAME)
con = sqlite3.connect(DB_FILENAME)
df = pd.read_sql_query("SELECT * FROM ASG", con)
df1 = pd.read_sql_query("SELECT * FROM ASG2020", con)
test = pd.read_csv('2021 Stats.csv')

#AllStar2020 List 
all_star2020_list = ['Bradley Beal', 'Kyrie Irving', 'Giannis Antetokounmpo', 'Kevin Durant', 'Joel Embiid', 'Jaylen Brown',	'James Harden', 'Zach LaVine', 'Ben Simmons', 'Julius Randle','Domantas Sabonis', 'Jayson Tatum', 'Nikola Vucevic',
                'Stephen Curry', 'Luka Doncic', 'LeBron James', 'Kawhi Leonard', 'Nikola Jokic', 'Devin Booker', 'Mike Conley Jr', 'Damian Lillard', 'Donovan Mitchell', 'Chris Paul', 'Anthony Davis', 'Paul George', 'Zion Williamson', 'Rudy Gobert']

all_star2020 = pd.DataFrame(data=all_star2020_list, columns=['PLAYER'])

#df DataWrangling
df= df.fillna(0)
df= df.drop(columns=['DEFWS', 'Team GP', 'USG%', 'PIE', 'Team Conference Rank', 'Avg. Pace', 'W','Prior ASG Appearances', 'AS Last Year?' ], axis=1)
df['Selected?'] = df['Selected?'].replace('', 0)
#for value in df['Selected?']:
#    if type(value) != int and type(value) != float:
#        print(value)
#        print(type(value))
df['Selected?'] = df['Selected?'].astype(int)

#df1 DataWrangling
df1['Player']= df1['Player'].str.split('\\').str[0]
df1 = df1.drop(columns=['Rk','Pos', 'Age', 'GS', 'MP', 'FG%', '3P%', '2P', '2P%', 'eFG%', 'FT%', 'ORB', 'DRB', 'PF', '2PA', '3PA'], axis=1)
df1 = df1.rename(columns={"Tm": "TEAM", "G": "GP", "3P": "3PM", "PTS_" : "PTS", "TRB" : "REB", "Player": "PLAYER"})
df1['Year'] = '2020'
df1['TS%'] = round((df1['PTS']/ (2*(df1['FGA']+0.44*df1['FTA'])))*100,1)  #TS%(Points/ [2*(Field Goals Attempted+0.44*Free Throws Attempted)])
df1 = df1[['Year', 'PLAYER', 'TEAM' ,'GP', 'PTS', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'TS%', '3PM']]
df1['Selected?'] = df1.PLAYER.isin(all_star2020_list).astype(int)

#Combine into main df
df = pd.concat([df, df1]).reset_index().drop(columns=['index'], axis=1)
df['GP'] = df['GP'].astype(float)

#Test Set Wrangling
test.columns = test.iloc[0]
test = test[1:].reset_index().drop(columns=['index'])
test['Player']= test['Player'].str.split('\\').str[0]
test = test.drop(columns=['Rk','Pos', 'Age', 'GS', 'MP', 'FG%', '3P%', '2P', '2P%', 'eFG%', 'FT%', 'ORB', 'DRB', 'PF', '2PA', '3PA'], axis=1)
test = test.rename(columns={"Tm": "TEAM", "G": "GP", "3P": "3PM", "PTS▼" : "PTS", "TRB" : "REB"})
test[['GP', 'FG', 'FGA', '3PM', 'FT', 'FTA', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PTS']] = test[['GP', 'FG', 'FGA', '3PM', 'FT', 'FTA', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PTS']].astype(float)
test['Year'] = '2021'
test['Selected?'] = '0'
test['TS%'] = round((test['PTS']/ (2*(test['FGA']+0.44*test['FTA'])))*100,1)
test = test[['Year', 'Player', 'TEAM', 'GP', 'PTS', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'TS%', '3PM', 'Selected?']]
test = test.sort_values(by='PTS', ascending=False).reset_index().drop(columns=['index'], axis=1)
test_save = test[['Year', 'Player', 'TEAM', 'GP']] ##Save for Later
test = test.dropna()


#Split Data into Train/Val
target = "Selected?"
features = ['PTS', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'TS%', '3PM']

train, val = train_test_split(df, train_size= 0.8, stratify=df[target], shuffle=True, random_state=1)

print(train.shape, val.shape, test.shape)

X_train = train[features]
y_train = train[target]
X_val = val[features]
y_val = val[target]
X_test = test[features]
y_test = test[target]

#RandomForestClassifier
forest = RandomForestClassifier(n_jobs=-1, random_state=2, class_weight='balanced')


forest.fit(X_train, y_train)
print("Train Acc:", forest.score(X_train, y_train))
print("Val Acc:", forest.score(X_val, y_val))
print(classification_report(y_val, forest.predict(X_val)))


#Prediction of 2022 All Stars
test= test[['PTS', 'REB', 'AST', 'STL', 'BLK','TOV', 'TS%', '3PM']]
test['AS Prob.'] = [prob[1] for prob in forest.predict_proba(test)]
test['Model Prediction'] = test['AS Prob.'].map(lambda x : 'Yes' if x > .40 else 'No')
ALL_STAR2022= pd.concat([test_save, test], axis=1)
ALL_STAR2022= ALL_STAR2022.sort_values(by="AS Prob.", ascending=False).reset_index().drop(columns=['index'])
prediction = ALL_STAR2022[ALL_STAR2022['Model Prediction'] == 'Yes']
print(prediction)
joblib.dump(prediction, 'result.pkl')