import os
import sys
import numpy as np
import pandas as pd
from src.exception import CustomException
import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from src.logger import logging

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    

def models_evaluation(X_train, y_train,X_test,y_test,models):
    try:
        report = {}

        for i in range(len(list(models))):
            logging.info(f" looking at the model {list(models.keys())[i]}")
            model = list(models.values())[i]
            #para = params[list(models.keys())[i]]

            #gs = GridSearchCV(model,para,cv=3)
            model.fit(X_train,y_train)
         
            #model.set_params(**gs.best_params_)
            #model.fit(X_train,y_train)

            #model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_score = r2_score(y_train, y_train_pred)

            test_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_score

        return report

    except Exception as e:
        raise CustomException(e, sys)


def load_object(file_path):

  try:
      with open(file_path,'rb') as file_obj:
          return pickle.load(file_obj)
  except Exception as e:
          raise CustomException(e, sys)