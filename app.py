from flask import Flask, request, render_template, url_for
import pickle
import numpy as np
import pandas as pd


app = Flask(__name__)
with open("model.pkl","rb") as file:
    model = pickle.load(file)

@app.route("/")
def a():
    return render_template("index.html")

@app.route("/inspect")
def home():
    return render_template("inspect.html")


@app.route("/output", methods=["GET", "POST"])
def output():
    if request.method == 'POST':
        
        var1 = request.form["gender"]
        var2 = request.form["age"]
        var3 = request.form["hyper_tension"]
        var4 = request.form["heart_disease"]
        var5 = request.form["ever_married"]
        var6 = request.form["work_type"]
        var7 = request.form["Residence_type"]
        var8 = request.form["avg_glucose_level"]
        var9 = request.form["bmi"]
        var10 = request.form["smoking_status"]

        # Convert the input data into a numpy array
        predict_data = [[var1, var2, var3, var4, var5, var6, var7, var8, var9, var10]]

        # Use the loaded model to make predictions
        predict = model.predict(predict_data)

        if (predict == 1):
            return render_template('output.html', predict="stroke")
        else:
            return render_template('output.html', predict="no stroke")
    return render_template("output.html")

if __name__ == "__main__":
    app.run(debug= True)
