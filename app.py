from flask import Flask, render_template, request,json
from flask_cors import CORS, cross_origin
import pickle
import pandas as pd
import numpy as np

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

    brands.insert(0, "Select Company")
    purchase_year.insert(0, "Select Year")
    gear_box.insert(0, "Select Fuel Type")

    return json(brands=brands, car_models=car_models , purchase_year=purchase_year , gear_box=gear_box)

@app.route("/predict", methods=["POST"])
@cross_origin(supports_credentials=True)
def predict():
    brand = request.form.get('brand')
    car_model = request.form.get('model')
    # purchase_year = request.form.get('purchase_year')
    gear_box = request.form.get('gear_box')
    # kms_driven = request.form.get('kms_driven')

    prediction = model.predict(
        pd.DataFrame(columns=['model', 'brand', 'gear_box'], data=np.array([car_model, brand, gear_box]).reshape(1, 3)))
    # print(prediction)

    return str(np.round(prediction[0], 2))
    # return {"brand": brand, "car_model": car_model, "gear_box": gear_box}


if __name__ == "__main__":
    app.run(debug=True)
