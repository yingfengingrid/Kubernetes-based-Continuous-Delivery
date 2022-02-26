from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)



@app.route("/")
def home():
    html = f"<h3>Sklearn Prediction Home</h3>"
    return html.format(format)

# TO DO:  Log out the prediction value
@app.route("/predict", methods=['POST'])
def predict():
    """Performs an sklearn prediction

    input looks like:
            {
    "CHAS":{
      "0":0
    },
    "RM":{
      "0":6.575
    },
    "TAX":{
      "0":296.0
    },
    "PTRATIO":{
       "0":15.3
    },
    "B":{
       "0":396.9
    },
    "LSTAT":{
       "0":4.98
    }

    result looks like:
    { "prediction": [ 20.35373177134412 ] }

    """


    json_payload = request.json
    LOG.info(f"JSON payload: {json_payload}")
    inference_payload = pd.DataFrame(json_payload)
    LOG.info(f"inference payload DataFrame: {inference_payload}")
    
    prediction = list(clf.predict(inference_payload))
    return jsonify({'prediction': prediction})

if __name__ == "__main__":
    data=np.loadtxt('housing.csv')
    
    Y=data[:,-1]
    X=data[:,0:13]
    clf=Pipeline([('scaler', StandardScaler()), ('model', LinearRegression())])
    clf.fit(X,Y)
    
    app.run(host='0.0.0.0', port=80, debug=True)
