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
@app.route('/recommend1')
def recommend1():
    return render_template('popularity.html')


@app.route('/bookName')
def show_book_name():
    book_name = list(pd.read_csv('collaborative_models/unique_book_name.csv')['Book-Title'].values)
    return render_template("bookname.html",list_fo_book_name = book_name)



if __name__ == "__main__":
    app.run(debug=True)