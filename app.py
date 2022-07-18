from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle

app = Flask(__name__, template_folder='template')

@app.route('/')
def home():
    return render_template('home.html')

file_model = open('model_75.pkl', 'rb')
model = pickle.load(file_model)

@app.route('/predict')
def index():
    return render_template('prediksi.html')

@app.route('/predict', methods=['POST'])
def predict():
    
    Year = float(request.form['Year'])
    Month = float(request.form['Month'])
    Day = float(request.form['Day'])
    Hour = float(request.form['Hour'])
    
    x = np.array([[Year, Month, Day, Hour]])
    
    prediction = model.predict(x)
    output = prediction
    
    if output >= 0.934:
        output = "Pasang"
    else:
        output = "Surut"
    
    return render_template('prediksi.html', hasil = output)

@app.route('/wisata')
def wisata():
    return render_template('wisata.html')

@app.route('/gak')
def gak():
    return render_template('Pariwisata-GAK.html')

@app.route('/snorkeling')
def snorkeling():
    return render_template('Pariwisata-Snorkeling.html')

@app.route('/umang_umang')
def umang_umang():
    return render_template('Pariwisata-Umang Umang.html')

@app.route('/tentang')
def tentang():
    return render_template('tentang.html')

@app.route('/about_sebesi')
def about_sebesi():
    return render_template('about_sebesi.html')

if __name__ == '__main__':
    app.run(debug = True)
