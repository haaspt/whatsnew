class GlobalConfig(object):

    def __init__(self):
        self.prompt_until_exit = True  # If True in verbose the user will be prompted until s/he chooses to exit
        self.article_limit = 10 # By default only 10 stories will be displayed, future version will allow this to be set by CLI argument
        self.headline_color = 'cyan'
        self.source_color = 'magenta'
        self.section_color = 'red'
        self.abstract_color = 'yellow'
        self.prompt_color = 'green'

class NewsFeedConfig(object):
    """Configure options for the newsfeeds"""

    def __init__(self):
        self.limit = 20  # Number of articles to be returned by query. Most feeds are limited to 20, some return more.
