from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
cors = CORS(app)
model = pickle.load(open("LinearRegressionModel.pkl", "rb"))
df = pd.read_csv("Cleaned_Car_data.csv")


@app.route("/", methods=["GET", "POST"])
def index():
    car_models = sorted(df["model"].unique())
    companies = sorted(df["brand"].unique())
    # purchase_year = sorted(df["year"].unique(), reverse = True)
    fuel_types = sorted(df["gear_box"].unique())

    companies.insert(0, "Select Company")
    # purchase_year.insert(0, "Select Year")
    fuel_types.insert(0, "Select Fuel Type")

    return car_models


@app.route("/predict", methods=["POST"])
@cross_origin(supports_credentials=True)
def predict():
    brand = request.form.get('brand')
    car_model = request.form.get('model')
    # purchase_year = request.form.get('purchase_year')
    gear_box = request.form.get('gear_box')
    # kms_driven = request.form.get('kms_driven')

    # prediction = model.predict(pd.DataFrame(columns=['model', 'brand', 'gear_box', 'year'], data = np.array([car_model, company, fuel_type , 2030]).reshape(1, 4)))
    # print(prediction)

    # return str(np.round(prediction[0], 2))
    return {"brand": brand, "car_model": car_model, "gear_box": gear_box}


if __name__ == "__main__":
    app.run(debug=True)