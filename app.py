
from flask import Flask, app, render_template, request,url_for, redirect
import pickle
import pandas as pd
import numpy as np


app = Flask(__name__)

forecast = pd.read_pickle('goldforecast.pkl')
forecast.head()

@app.route('/')

def home():
    return render_template('home.html', tables= [forecast.to_html(classes = 'forecast')],
    titles = ['Date','Average forecast for the month'], )

@app.route('/Name', methods = ['POST'])
def Name():
    if request.method == 'POST':
        return render_template('Name.html')









if __name__ == '__main__':
    import os
    debug_mode = os.getenv('FLASK_ENV') == 'development'
    app.run(debug=debug_mode)