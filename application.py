from flask import Flask,request,render_template
import pandas as pd
import numpy as np
from src.pipeline.prediction_pipeline import CustomData,PredictPipeline

from sklearn.preprocessing import StandardScaler

application=Flask(__name__)

app=application

#home page route
@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/predict_charges',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
       return render_template('home.html')
    else:
        input=CustomData(
            sex=request.form.get('sex'),
            age=request.form.get('age'),
            region=request.form.get('region'),
            smoker=request.form.get('smoker'),
            height=request.form.get('height'),
            weight=request.form.get('weight'),
            children=request.form.get('children') )
        
        input_df=input.data_into_dataframe()
        print(input_df)
        predict_pipeline=PredictPipeline()
        results=predict_pipeline.predict(input_df)
        return render_template('home.html',results=results[0])
    

if __name__=="__main__":
    app.run(host="0.0.0.0")
