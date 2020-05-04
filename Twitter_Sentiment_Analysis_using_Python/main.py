from flask import Flask,render_template,request
from twitter import TwitterClient
app=Flask(__name__)
import plotly.graph_objects as go
api = TwitterClient()
@app.route("/fatch",methods=['GET','POST'])
def index():
    if (request.method == 'POST'):
        query1 = request.form.get('query')

    tweets = api.get_tweets(query=query1, count=200)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    posper=100 * len(ptweets) / len(tweets)

    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    negper=100 * len(ntweets) / len(tweets)

    # percentage of neutral tweets
    neuper=100 * (len(tweets) - len(ntweets) - len(ptweets)) / len(tweets)

    labels = ['Positive', 'Negative', 'Neutral']
    values = [int(posper), int(negper), int(neuper)]
    topic = "Topic: " + query1
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, name=topic)])
    fig.update_layout(title_text="Twitter Sentiment Analysis")
    fig.show()
    return render_template('index.html',ip=query1,pt=ptweets,nt=ntweets,labels=labels,values=values)


@app.route("/")
def main():
    return render_template('main.html')


app.run(debug=True)