import requests

def nyt_feed():
    """Requests content from the New York times and returns it in JSON format
    """

    raw_news = requests.get('http://api.nytimes.com/svc/news/v3/content/all/all/.json?limit=20&api-key=cb6b696a018707793e9436bda629bde3%3A4%3A66817738')

    nyt_feed = raw_news.json()

    return nyt_feed
