Twitter Sentiment Analysis
-----
### Introduction
This app use to analysis tranding topic in three category sentiment positive, negative, neutral.

### Overview


* Enter tranding topic.
* find tweets in different category.
* analysis of sentiment in pie chart.

### Tech Stack

Our tech stack will include:

* **textblob** to be our NLP Library
* **plotly** to be for pie-chart display
* **tweepy**  for Authorize twitter API client
* **Python3** and **Flask** as our server language and server framework
* **HTML**, **CSS**, and **Javascript** with [Bootstrap 3](https://getbootstrap.com/docs/3.4/customize/) for our website's frontend

 ```sh
  ├── README.md
  ├── app.py *** the main driver of the app. Includes your SQLAlchemy models.
                    "python app.py" to run after installing dependences
  ├──twitter.py *** for authentication twitter
  ├── requirements.txt *** The dependencies we need to install with "pip3 install -r requirements.txt"
  ├── static
  │   ├── css 
  └── templates *** Html pages
  
  ```
### Setup
1. Install the dependencies:
  ```
  $ pip install -r requirements.txt
  ```
2. Authorize twitter API client in twitter.py file:
  ```
    keys and tokens from the Twitter Dev Console
		consumer_key = 'xxxxxxxxxxxxxxxxxxx'
		consumer_secret = 'xxxxxxxxxxxxxxxxxx'
		access_token = 'xxxxxxxxxxxxxxxxxxxxxx'
		access_token_secret = 'xxxxxxxxxxxx'

  ```
  Refer this Page: https://www.geeksforgeeks.org/twitter-sentiment-analysis-using-python/.

3. Run the development server:
  ```
  $ python app.py
  ```
###Dashboard
![Home page](https://github.com/imshubh17/Projects/blob/master/images/tsa/input.PNG?raw=true "Main Page")
![Home page](https://github.com/imshubh17/Projects/blob/master/images/tsa/dashboard.PNG?raw=true "Main Page")
![Home page](https://github.com/imshubh17/Projects/blob/master/images/tsa/tweets.PNG?raw=true "Main Page")



####We follow these 3 major steps in our program:
    Authorize twitter API client.
    Make a GET request to Twitter API to fetch tweets for a particular query.
    Parse the tweets. Classify each tweet as positive, negative or neutral.
