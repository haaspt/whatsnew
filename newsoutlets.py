import requests
from config import NYTOptions


def nyt_feed():
    """Requests content from the New York times and returns it in JSON format
    """
    config = NYTOptions()
    nyt_filter = ','.join(config.filter).replace(' ', '%20')
    apikey = config.apikey.replace(':', '%3A')
    request_string = 'http://api.nytimes.com/svc/news/v3/content/all/%s/.json?limit=%s&api-key=%s' % (nyt_filter, config.limit, apikey)
    nyt_news = requests.get(request_string).json()
    return nyt_news
