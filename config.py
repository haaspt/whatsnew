from filters import nyt_filter

class GlobalConfig(object):

    def __init__(self):
        self.prompt_until_exit = True  #If True in verbose the user will be prompted until s/he explicitly choses to exit

class NYTOptions(object):

    def __init__(self):
        self.filter = nyt_filter  #select prefered sections in filters.py
        self.limit = 10  #number of articles to be returned by query
        self.apikey = 'cb6b696a018707793e9436bda629bde3:4:66817738'
