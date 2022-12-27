from flask import Flask,url_for,request,render_template
import numpy as np
import pandas as pd
import joblib
import warnings
warnings.filterwarnings('ignore')
# load the models
popular = pd.read_csv('popularity_based/popularity_based.csv')
pt = joblib.load('collaborative_models/pivot_table_data.lb')
similarity_scores = joblib.load('collaborative_models/similarity_score.lb')
books = joblib.load('collaborative_models/collaborative_recmdsystem_data.lb')

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
# to get all famous books name
@app.route('/bookName')
def show_book_name():
    book_name = list(pd.read_csv('collaborative_models/unique_book_name.csv')['Book-Title'].values)
    return render_template("bookname.html",list_fo_book_name = book_name)
# to get the popularity based recommandation system
@app.route('/recommend1')
def recommend1():
    return render_template('popularity.html',
                           book_name = list(popular['Book-Title'].values),
                           author=list(popular['Book-Author'].values),
                           image=list(popular['Image-URL-M'].values),
                           votes=list(popular['num_ratings'].values),
                           rating=list(popular['avg_rating'].values),
                           publisher=list(popular['Publisher'].values)
                           
                           )
# to display the recommandation-2 html file
@app.route('/recommend2')
def recommend2():
    return render_template('recomandation.html')

# to get the recommandation by the recommandation-2
@app.route('/recommend_books',methods=['post'])
def recommend():
    try:
        user_input = request.form.get('user_input')
        index = np.where(pt.index == user_input)[0][0]
        similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:9]
    except:
        return render_template("errorrr.html")
    else:
        data = []
        for i in similar_items:
            item = []
            temp_df = books[books['Book-Title'] == pt.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Publisher'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Year-Of-Publication'].values))


            data.append(item)
        # print(data)
        return render_template('recomandation.html',data=data)









if __name__ == "__main__":
    app.run(debug=True)