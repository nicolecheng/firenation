from flask import Flask, render_template, session, redirect, url_for, request
from utils import api, analyze

app = Flask(__name__)
feed = analyze.get_feed()

@app.route("/", methods = ['GET', 'POST'])
def home(): 
    return render_template('home.html')

@app.route("/<train_name>/", methods = ['GET', 'POST'])
def train(train_name):
    stops = analyze.get_stops(train_name)
    return render_template('train.html', stops = stops)
''' 
    info = {}
    for a in stops{
         direction = analyze.get_direction(a)
         arrivaltime = analyze.get_arrival_time(a)
         info[a] = infu
    }
'''
    

if __name__ == "__main__":
    app.debug = True
    app.run()

    
