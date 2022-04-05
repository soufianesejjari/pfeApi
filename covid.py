# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from flask import Flask, jsonify,request
from pypmml import Model
import pandas as pd

lr = Model.fromFile( "Arbre.xml")

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello!</h1>"
@app.route('/predict', methods=['POST'])
def predict():
    if lr:
        try:
            json_ = request.json
            print(json_)
            query = pd.get_dummies(pd.DataFrame(json_))
            prediction =lr.predict(query)
            predictionResult=prediction['predicted_corona_result']
            print()
            r=[list(prediction.get('predicted_corona_result'))[0]]
            r.append(list(prediction.get('probability'))[0])
            test=r[0]
            print(r)
            return jsonify({'prediction': r[0], 'probability':r[1]})

        except:

            return jsonify({})
    else:
        print ('Train the model first')
        return ('No model here to use')

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="localhost", port=5001)