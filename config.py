from filters import nyt_filter, guardian_filter


class GlobalConfig(object):

    def __init__(self):
        self.prompt_until_exit = True  # If True in verbose the user will be prompted until s/he chooses to exit
        self.article_limit = 10 # By default only 10 stories will be displayed, future version will allow this to be set by CLI argument

class NYTOptions(object):
    """For NYT API documentation see: http://developer.nytimes.com/io-docs and http://developer.nytimes.com/docs/times_newswire_api/"""


    def __init__(self):
        self.filter = nyt_filter  # Select preferred sections in filters.py
        self.limit = 20  # Number of articles to be returned by query
        self.apikey = 'cb6b696a018707793e9436bda629bde3:4:66817738'


class GuardianOptions(object):
    """For the Guardian API documentation see: http://open-platform.theguardian.com/documentation/"""


    def __init__(self):
        self.filter = guardian_filter
        self.limit = 20
        self.apikey = 'qtz5kdh2ajykqydk75r79nje'
