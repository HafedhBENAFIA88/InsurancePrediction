import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder , StandardScaler
import os
from src.utils import save_object

from src.exception import CustomException
from src.logger import logging



@dataclass
class DataProcessingConfig:
    processing_obj_path=os.path.join('artifacts','processor.pkl')



class DataProcessing:
    def __init__(self):
        self.data_processing_config=DataProcessingConfig()

    def define_transformation(self):

        '''
        This function allows to apply the necessary transformations forthe project to the data set

        '''

        try:

            numerical_columns=["age","bmi","children"]
            categorical_columns=['sex','smoker','region']
            
            logging.info(f"The categorical columns are:{categorical_columns}")
            logging.info(f"The numerical columns are:{numerical_columns}")

            numerical_pipeline=Pipeline(
                steps=[
                      ("imputer", SimpleImputer(strategy='median')),
                      ('Scaler', StandardScaler(with_mean=False)) ])
           
            
            categorical_pipeline=Pipeline(steps=[
                                        ("imputer",SimpleImputer(strategy="most_frequent")),
                                        ('one_hot_encoder',OneHotEncoder()),
                                        ('scaler',StandardScaler(with_mean=False))])

            
            

            processor=ColumnTransformer([ ('num_pipeline',numerical_pipeline,numerical_columns),
                                            ('cat_pipeline',categorical_pipeline,categorical_columns)]
            )
            return processor
        
        except Exception as e:
                raise CustomException(e,sys)       

    def perform_data_transformation (self,train_path,test_path):
         try:
              train_df=pd.read_csv(train_path)
              test_df=pd.read_csv(test_path)
              logging.info('reading the train and test data is complete , ready for processing')
              
              processor=self.define_transformation()
              logging.info('defining the required transformations to the data')

              target_column_name="charges"
             # numerical_columns=["writing_score","reading_score"]

              X_train=train_df.drop(columns=[target_column_name],axis=1)
              y_train=train_df[target_column_name]
              X_test=test_df.drop(columns=[target_column_name],axis=1)
              y_test=test_df[target_column_name]
               
              logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
                )

              X_train_T=processor.fit_transform(X_train)
              X_test_T=processor.transform(X_test) 

              train_arr = np.c_[ X_train_T, np.array(y_train)]
            
              test_arr = np.c_[X_test_T, np.array(y_test)]

              logging.info(f"Saving preprocessing object.")

              save_object(

                file_path=self.data_processing_config.processing_obj_path,
                obj=processor )

              return (
                train_arr, test_arr,
                self.data_processing_config.processing_obj_path,
            )

         except Exception as e:
                raise CustomException(e,sys)  