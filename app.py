from flask import Flask,url_for,request,render_template
import numpy as np
import pandas as pd
import joblib
import warnings
warnings.filterwarnings('ignore')
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')






if __name__ == "__main__":
    app.run(debug=True)