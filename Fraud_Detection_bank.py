

import pandas as pd
import numpy as np

#import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import roc_curve, auc

#import xgboost as xgb
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
import pickle

# set seaborn style because it prettier
#sns.set()
# %% read and plot
data = pd.read_csv("Data/bs140513_032310.csv")
data = data[['age', 'gender', 'merchant','category','amount', 'fraud' ]]
data.head(5)

# Create two dataframes with fraud and non-fraud data 
df_fraud = data.loc[data.fraud == 1] 
df_non_fraud = data.loc[data.fraud == 0]



# %% Preprocessing


# turning object columns type to categorical for later purposes
col_categorical = data.select_dtypes(include= ['object']).columns
for col in col_categorical:
    data[col] = data[col].astype('category')


# categorical values ==> numeric values
data[col_categorical] = data[col_categorical].apply(lambda x: x.cat.codes)

# define X and y
X = data.drop(['fraud'],axis=1)
y = data['fraud']


#  cross validation is no needed since we have a lot of instances
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=42,shuffle=True,stratify=y)



# The base score should be better than predicting always non-fraduelent
print("Base score we must beat is: ", 
      df_non_fraud.fraud.count()/ np.add(df_non_fraud.fraud.count(),df_fraud.fraud.count()) * 100)



# %% Random Forest Classifier

rf_clf = RandomForestClassifier(n_estimators=100,max_depth=8,random_state=42,
                                verbose=1,class_weight="balanced")

rf_clf.fit(X_train,y_train)
y_pred = rf_clf.predict(X_test)
print('X_test',X_test)


# 98 % recall on fraudulent examples but low 24 % precision.
print("Classification Report for Random Forest Classifier: \n", classification_report(y_test, y_pred))
print("Confusion Matrix of Random Forest Classifier: \n", confusion_matrix(y_test,y_pred))

# save the model to disk
filename = 'finalized_model.sav'
pickle.dump(rf_clf, open(filename, 'wb'))

