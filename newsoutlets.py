import requests
from config import NYTOptions, GuardianOptions

class Story(object):
    """Data structure to organize the elements of each news story.
    Used by main.py"""

    def __init__(self, title, url, section, source, abstract):
        self.title = title
        self.url = url
        self.section = section
        self.source = source
        self.abstract = abstract


def nyt_feed():
    """Requests content from the New York times and returns it in JSON format"""

    config = NYTOptions()
    nyt_filter = ','.join(config.filter).replace(' ', '%20') # Items are comma separated, with spaces replaced by '%20' escape characters
    nyt_apikey = config.apikey.replace(':', '%3A') # Colons in API must be replaced with '%3A' escape characters
    request_string = 'http://api.nytimes.com/svc/news/v3/content/all/%s/.json?limit=%s&api-key=%s' % (nyt_filter, config.limit, nyt_apikey)
    nyt_news = requests.get(request_string).json()
    return nyt_news

def guardian_feed():
    """Requests content from the Guardian and returns it in JSON format"""
    
    config = GuardianOptions()
    guardian_filter = '%7C'.join(config.filter) # Items are separated by vertical pipes, which must be replaced by '%7C' escape characters
    request_string = 'http://content.guardianapis.com/search?section=%s&order-by=newest&page=%s&api-key=%s' % (guardian_filter, config.limit, config.apikey)
    guardian_news = requests.get(request_string).json()
    return guardian_news

def feeder():
    """Requests news feeds and creates a list of strings out of stories"""

    nyt_news = nyt_feed()
    guardian_news = guardian_feed()

    news_objects = []
    news_index = 0

    for story in nyt_news['results']:
        story = Story(story['title'].replace('&#8217;', "'").replace('&#8216;', "'"), story['url'], story['section'], story['source'], story['abstract'])
        news_objects.append(story)

    for story in guardian_news['response']['results']:
        story = Story(story['webTitle'], story['webUrl'], story['sectionName'], "The Guardian", "No abstract available")
        news_objects.append(story)

    return news_objects
