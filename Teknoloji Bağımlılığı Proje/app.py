from flask import Flask, render_template
import feedparser

app = Flask(__name__)

@app.route('/')
def index():

    rss_url = 'https://techcrunch.com/feed/'


    feed = feedparser.parse(rss_url)


    return render_template('index.html', feed=feed)

if __name__ == '__main__':
    app.run(debug=True)