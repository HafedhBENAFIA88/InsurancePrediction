import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
#from src.components.data_transformation import DataTransformationConfig
#from src.components.data_transformation import DataTransformation
#from src.components.model_trainer import ModelTrainer
#from src.components.model_trainer import ModelTrainerConfig



@dataclass
class DataExtractConfig:
    train_path: str=os.path.join('artifacts','train.csv')
    test_path: str=os.path.join('artifacts','test.csv')
    raw_path: str=os.path.join('artifacts','data.csv')


class DataExtraction:

    def __init__(self):
         self.extract_config=DataExtractConfig()

    def perform_extraction (self):
        logging.info('Starting the data extraction component here')
        
        try:
            df=pd.read_csv('./src/data/insurance.csv')
            logging.info('Reading successfully the database in the your input path ')

            os.makedirs(os.path.dirname(self.extract_config.train_path),exist_ok=True)

            df.to_csv(self.extract_config.raw_path,index=False,header=True)

            logging.info("Saving the data successfully, now let's split the data , and save the test and train splits ")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=10)
            train_set.to_csv(self.extract_config.train_path,index=False,header=True)
            test_set.to_csv(self.extract_config.test_path,index=False,header=True)
            logging.info("Splitting data and saving training and test splits is successful , therefore ingestion of the data completed")

            return ( self.extract_config.train_path, self.extract_config.test_path)
        
        except Exception as e:
            raise CustomException (e,sys)