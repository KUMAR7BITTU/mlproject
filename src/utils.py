# Any functionality that we are writing in common way which will be used in entire application so that i will basically say as utils.py .

import os
import sys
import numpy as np
import pandas as pd
import dill
# dill is also another library which will also help us to create pickle file .
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score
from src.exception import CustomException
def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb")as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys);

# Let suppose we have to read a data from dataset , i can create a mongodbclient here . If i have to save my model into the cloud , i can write the code over here . we will call the utils's code inside the component .

# Here we will write code related to evaluation method .

def evaluate_models(X_train,y_train,X_test,y_test,models,param):
    try:
        report={}
        
        for i in range(len(list(models))):
            model= list(models.values())[i]
            
            para=param[list(models.keys())[i]]
            # Take this parameter (para) and apply GridSearchCV 
            # gs=GridSearchCV(model,para,cv=cv,n_jobs=n_jobs,verbose=verbose,refit=refit)
            gs=GridSearchCV(model,para,cv=3)
            # cv = cross validation
            gs.fit(X_train,y_train)
            
            
            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train) # Train Model
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)
            train_model_score = r2_score(y_train,y_train_pred)
            test_model_score = r2_score(y_test,y_test_pred)
            report[list(models.keys())[i]]=test_model_score
            
        return report
        
    except Exception as e:
        raise CustomException(e,sys)  

# This function is just opening the pickle file in readbyte mode and it is just loading the pickle file by using this dil .
def load_object(file_path):
    try:
        with open(file_path,"rb") as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise CustomException(e,sys)       