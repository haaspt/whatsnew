import requests
from config import NYTOptions

def nyt_feed():
    """Requests content from the New York times and returns it in JSON format
    """
    config = NYTOptions()
    filter = ','.join(config.filter).replace(' ', '%20')
    apikey = config.apikey.replace(':', '%3A')
    request_string = 'http://api.nytimes.com/svc/news/v3/content/all/%s/.json?limit=%s&api-key=%s' % (filter, config.limit, apikey)
    nyt_feed = requests.get(request_string).json()

    return nyt_feed
