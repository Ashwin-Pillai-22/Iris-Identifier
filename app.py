from flask import Flask, render_template, request, url_for
import pandas as pd
import joblib
import numbers

model = joblib.load("Iris/model.pkl")
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods = ["POST"])
def predict():
    try:
        feature = [
            float(request.form["sepal_length"]),
            float(request.form["sepal_width"]),
            float(request.form["petal_length"]),
            float(request.form["petal_width"])
        ]
        
        for f in feature:
            if f < 0:
                return render_template("index.html", prediction = "No negative values.")
        prediction = model.predict([feature])[0]


        iris_types = {"Iris-setosa": "Setosa", "Iris-versicolor": "Versicolor", "Iris-virginica": "Virginica"}
        iris_images = {"Iris-setosa": "setosa.png", "Iris-versicolor": "versicolor.png", "Iris-virginica": "virginica.png"}

        res = iris_types[prediction]
        img = iris_images[prediction]

        return render_template("index.html", prediction = res, image = img)

    except Exception as e:
        return render_template("index.html", prediction = "Please provide valid input.")
if __name__ == "__main__":
    app.run(port=5002)