import pandas as pd
import numpy as np
from sklearn import model_selection
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt

def main():

    df = pd.read_csv('/Users/lissjust/Desktop/fileForPlayerProjectionsAdjusted.csv') 
    print(df.shape)
    print df.describe()

    target_column = ['pointsScored'] 
    predictors = list(set(list(df.columns))-set(target_column))
    df[predictors] = df[predictors]/df[predictors].max()
    print df.describe()

    X = df[predictors].values
    y = df[target_column].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=40)
    print(X_train.shape); print(X_test.shape)
    

    lr = LinearRegression()
    lr.fit(X_train, y_train)

    

    pred_train_lr= lr.predict(X_train)
    print(np.sqrt(mean_squared_error(y_train,pred_train_lr)))
    print(r2_score(y_train, pred_train_lr))

    pred_test_lr= lr.predict(X_test)
    print(np.sqrt(mean_squared_error(y_test,pred_test_lr))) 
    print(r2_score(y_test, pred_test_lr))






    
    return



if __name__=="__main__":
    main()