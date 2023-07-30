import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass


    def predict(self,inputs):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            processor_path=os.path.join('artifacts','processor.pkl')
            model=load_object(file_path=model_path)
            processor=load_object(file_path=processor_path)
            data_processed=processor.transform(inputs)
            prediction=model.predict(data_processed)
            return prediction
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__( self, 
            age: int,
            sex: str ,
            weight: int ,
            height: float,
            children: int,
            smoker: str,
            region: str ):
            
            self.sex = sex

            self.age = age

            self.weight = weight

            self.height = height

            self.children= children

            self.smoker = smoker
    
            self.region = region
    

    def data_into_dataframe(self):
        
     try:
            
            data_dict = {
                "age": [self.age],
                "sex": [self.sex],
                "bmi": [float(self.weight) / float(self.height) ],
                "children": [self.children],
                "smoker": [self.smoker],
                "region": [self.region],
            }
            print(self.weight)
            return pd.DataFrame(data_dict)

     except Exception as e:
            raise CustomException(e, sys)

    


