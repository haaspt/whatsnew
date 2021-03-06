import feedparser
from bs4 import BeautifulSoup
from config import NewsFeedConfig

class NewsFeed(object):

    def __init__(self, outlet, section, url, language):
        self.outlet = outlet
        self.section = section
        self.url = url
        self.language = language

    def getFeed(self):
        self.feed = feedparser.parse(self.url)

    def __str__(self):
        return "Feed name: %s, Section: %s" % (self.outlet, self.section)

class Story(object):
    """Data structure to organize the elements of each news story.
    Used by main.py"""

    def __init__(self, title, url, section, source, abstract):
        self.title = title
        self.url = url
        self.section = section
        self.source = source
        self.abstract = abstract


# New York Times Feeds (http://www.nytimes.com/services/xml/rss/index.html) {

nyt_home = NewsFeed('New York Times', 'Front Page', 'http://www.nytimes.com/services/xml/rss/nyt/HomePage.xml', 'English')

nyt_international = NewsFeed('New York Times', 'International', 'http://www.nytimes.com/services/xml/rss/nyt/InternationalHome.xml', 'English')

nyt_world = NewsFeed('New York Times', 'World', 'http://www.nytimes.com/services/xml/rss/nyt/World.xml', 'English')

nyt_us = NewsFeed('New York Times', 'U.S.', 'http://www.nytimes.com/services/xml/rss/nyt/US.xml', 'English')

nyt_politics = NewsFeed('New York Times', 'Politics', 'http://www.nytimes.com/services/xml/rss/nyt/Politics.xml', 'English')

# }

# Washington Post Feeds (http://www.washingtonpost.com/rss-feeds/2014/08/04/ab6f109a-1bf7-11e4-ae54-0cfe1f974f8a_story.html) {

wapo_politics = NewsFeed('Washington Post', 'Politics', 'http://feeds.washingtonpost.com/rss/politics', 'English')

wapo_world = NewsFeed('Washington Post', 'World', 'http://feeds.washingtonpost.com/rss/world', 'English')

wapo_us = NewsFeed('Washington Post', 'National', 'http://feeds.washingtonpost.com/rss/national', 'English')

# }

# The Guardian (http://www.theguardian.com/uk/rss and elsewhere) {

guardian_front = NewsFeed('Guardian', 'Front Page', 'http://www.theguardian.com/uk/rss', 'English')

guardian_world = NewsFeed('Guardian', 'World', 'http://www.theguardian.com/world/rss', 'English')

guardian_politics = NewsFeed('Guardian', 'Politics', 'http://www.theguardian.com/politics/rss', 'English')

# }

feed_list = [nyt_home, nyt_world, nyt_international, wapo_politics, wapo_us, guardian_world, guardian_front]

def feeder():

    story_list = []
    for news_feed in feed_list:
        news_feed.getFeed()

        for story in news_feed.feed.entries[0:NewsFeedConfig().limit]:

            # This is ugly. I'll fix this {
            if news_feed.outlet == 'New York Times':
                abstract = BeautifulSoup(story.summary, "html5lib").contents[0]
            elif news_feed.outlet == 'Washington Post':
                abstract = BeautifulSoup(story.summary, "html5lib").contents[0]
            elif news_feed.outlet == 'Guardian':
                try:
                    abstract = BeautifulSoup(story.summary, "html5lib").p.contents[0]
                except AttributeError:
                    abstract = BeautifulSoup(story.summary, "html5lib").contents[0]
            else:
                abstract = 'ERROR: Undefined news outlet'
            # }ugly

            story = Story(story.title, story.link, news_feed.section, news_feed.outlet, abstract)
            story_list.append(story)

    return story_list
