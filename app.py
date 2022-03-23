from flask import Flask , render_template , request
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)


@app.route("/", methods = ["GET" , "POST"])
def home():
    if request.method == "POST":
        try:
            T = float(request.form["Temperature"])
            P = request.form["Pressure"]
            XCO2 = request.form["CO2 mole fraction"]
            pH = request.form["pH"]
            Ca2= request.form["Calcium ion (ppm)"]
            Na = request.form["Sodium ion (ppm)"]
            Mg2 = request.form["Magnesium ion (ppm)"]
            Fe2 = request.form["Iron ion (ppm)"]
            HCO3 = request.form["Bicarbonate ion (ppm)"]
            SO4 = request.form["Sulfate ion (ppm)"]
            Cl = request.form["Chlorine ion (ppm)"]
            CO3 = request.form["Carbonate ion (ppm)"]
            TDS = request.form["TDS (ppm)"]


            def predict_scale():
                """
                T = 0
                P = 0
                XCO2 = 0
                pH = 0
                Ca2= 0
                Na = 0
                Mg2 = 0
                Fe2 = 0
                HCO3 = 0
                SO4 = 0
                Cl = 0
                CO3 = 0
                TDS = 0"""

                """
                if request.method == "POST":
                    try:
                T = float(request.form["Temperature"])
                P = request.form["Pressure"]
                XCO2 = request.form["CO2 mole fraction"]
                pH = request.form["pH"]
                Ca2= request.form["Calcium ion (ppm)"]
                Na = request.form["Sodium ion (ppm)"]
                Mg2 = request.form["Magnesium ion (ppm)"]
                Fe2 = request.form["Iron ion (ppm)"]
                HCO3 = request.form["Bicarbonate ion (ppm)"]
                SO4 = request.form["Sulfate ion (ppm)"]
                Cl = request.form["Chlorine ion (ppm)"]
                CO3 = request.form["Carbonate ion (ppm)"]
                TDS = request.form["TDS (ppm)"]"""
        
    
        

    
    
                prediction = classifier.predict([[
                    T,
                    P,
                    XCO2,
                    pH,
                    Ca2,
                    Na,
                    Mg2,
                    Fe2,
                    HCO3,
                    SO4,
                    Cl,
                    CO3,
                    TDS
                    ]])

                if (prediction[0] > 0.5):
                    prediction = "Scale is depositing."
                else:
                    prediction = "Scale is not depositing."

                return render_template("index.html", p=prediction)
        except:
            print("Please insert a valid number.")

    return render_template("index.html")

    ####return render_template("index.html")


###
#app.route("/", methods = ["GET", "POST"])
#def marks():
    # HTML -> py file
    #if request.method == "POST":hrs = request.form["hrs"]
       ## marks_pred = m.marks_prediction(hrs)

    # send data from py -> to HTML
    ##return render_template("index.html", n = marks_pred)###



if __name__ == "__main__":
    app.run(port=2022, debug=True)