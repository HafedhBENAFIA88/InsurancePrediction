from src.logger import logging
from src.components.data_extraction import DataExtraction
from src.components.data_processing import DataProcessing
from src.components.data_training import ModelTrainer
from src.exception import CustomException

data_extraction=DataExtraction()
tr_path,test_path=data_extraction.perform_extraction()
data_processing=DataProcessing()
train,test,obj_path=data_processing.perform_data_transformation(tr_path,test_path)
model_trainer=ModelTrainer()
r2=model_trainer.perform_training(train,test)
print( r2 )



