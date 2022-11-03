from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
import os
import json
import pickle
import pandas as pd
import numpy as np

load_dotenv()
app = Flask(__name__)
cors = CORS(app)
model = pickle.load(open("CarPricePredict.pkl", "rb"))
df = pd.read_csv("Cleaned_Car_data.csv")

@app.route("/", methods=["GET", "POST"])
def index():
    car_models = sorted(df["model"].unique())
    brands = sorted(df["brand"].unique())
    purchase_year = sorted(df["year"].unique(), reverse=True)
    gear_box = sorted(df["gear_box"].unique())
    energy = sorted(df["energy"].unique())

    return jsonify({"car_models": car_models, "brands": brands, "gear_box": gear_box, "energy": energy})


@app.route("/predict", methods=["POST"])
@cross_origin(supports_credentials=True)
def predict():
    brand = request.form.get('brand')
    car_model = request.form.get('model')
    purchase_year = request.form.get('purchase_year')
    gear_box = request.form.get('gear_box')
    energy = request.form.get('energy')
    trim = request.form.get('trim')

    if request.headers.get('Authorization') == os.environ["API_KEY"]:

        prediction = model.predict(
        pd.DataFrame(columns=['model', 'brand', 'gear_box', 'energy' , 'year' , 'trim'], data=np.array([car_model, brand, gear_box,energy,purchase_year,trim]).reshape(1, 6)))

        return str(np.round(prediction[0], 2))
    else:
        return jsonify({"message": "Unauthorized"})


if __name__ == "__main__":
    app.run(debug=True)
