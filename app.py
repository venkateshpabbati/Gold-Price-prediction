from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

# Load forecast data safely
def load_forecast():
    try:
        forecast = pd.read_pickle('goldforecast.pkl')
        return forecast
    except FileNotFoundError:
        return pd.DataFrame(columns=['Date', 'Average forecast for the month'])

@app.route('/')
def home():
    forecast = load_forecast()
    return render_template(
        'home.html',
        tables=[forecast.to_html(classes='forecast', index=False)],
        titles=['Date', 'Average forecast for the month']
    )

@app.route('/name', methods=['GET', 'POST'])
def name():
    # Example: Handle POST or GET separately if needed
    if request.method == 'POST':
        # Process POST data here if necessary
        pass
    return render_template('Name.html')

if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_ENV') == 'development'
    app.run(debug=debug_mode)


# from flask import Flask, app, render_template, request,url_for, redirect
# import pickle
# import pandas as pd
# import numpy as np


# app = Flask(__name__)

# forecast = pd.read_pickle('goldforecast.pkl')
# forecast.head()

# @app.route('/')

# def home():
#     return render_template('home.html', tables= [forecast.to_html(classes = 'forecast')],
#     titles = ['Date','Average forecast for the month'], )

# @app.route('/Name', methods = ['POST'])
# def Name():
#     if request.method == 'POST':
#         return render_template('Name.html')









# if __name__ == '__main__':
#     import os
#     debug_mode = os.getenv('FLASK_ENV') == 'development'
#     app.run(debug=debug_mode)
