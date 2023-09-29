from flask import Flask,jsonify,request
import pandas as pd



movies_data = pd.read_csv("final.csv")



app = Flask(__name__)


all_movies = movies_data[["original_title","poster_link","release_date","runtime","weighted_rating"]]
movies = []
liked_movies = []
did_not_watched = [],
did_not_liked_movies = []

def assigned_value():
    m_data = {
        "original_title":
        all_movies.iloc[0,0],
        "poster_link":
        all_movies.iloc[0,1],
        "release_data":
        all_movies.iloc[0,2]or "N/A",
        "runtime":
        all_movies.iloc[0,3],
        "weighted_rating":
        all_movies.iloc[0,4]/2
    }
    return m_data

@app.route("/movies")
def get_movies():
    movies_data = assigned_value()
    return jsonify({"data":movies_data,"status":"Sucesso"})



#@app.route("/liked")
#def liked_movies():
    



if __name__ == "__main__":
    app.run()

