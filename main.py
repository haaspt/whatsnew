import requests
import click

"""
For NYT API documentation see: http://developer.nytimes.com/io-docs and http://developer.nytimes.com/docs/times_newswire_api/
For requests documentation see: http://www.python-requests.org/en/latest/
For additional news APIs see: http://www.programmableweb.com/news/81-news-apis-digg-fanfeedr-and-clearforest/2012/02/01
"""

click.clear()

raw_news = requests.get('http://api.nytimes.com/svc/news/v3/content/all/all/.json?limit=20&api-key=cb6b696a018707793e9436bda629bde3%3A4%3A66817738')

news = raw_news.json()

nyt_filter = ['Business', 'Business Day', 'Front Page', 'International Home', 'N.Y. / Region', 'N.Y./Region',
              'NYRegion', 'NYT Now', 'National', 'New York', 'New York and Region', 'Science', 'Technology',
              "Today's Headlines", 'U.S.', 'Washington', 'World']

"""List of possible values for section filter:
Arts, Automobiles, Autos, Blogs, Books, Booming, Business, Business Day, Corrections, Crosswords & Games, Crosswords/Games, Dining & Wine, Dining and Wine, Editors' Notes, Education, Fashion & Style, Food, Front Page, Giving, Global Home, Great Homes & Destinations, Great Homes and Destinations, Health, Home & Garden, Home and Garden, International Home, Job Market, Learning, Magazine, Movies, Multimedia, Multimedia/Photos, N.Y. / Region, N.Y./Region, NYRegion, NYT Now, National, New York, New York and Region, Obituaries, Olympics, Open, Opinion, Paid Death Notices, Public Editor, Real Estate, Science, Sports, Style, Sunday Magazine, Sunday Review, T Magazine, T:Style, Technology, The Public Editor, The Upshot, Theater, Times Topics, TimesMachine, Today's Headlines, Topics, Travel, U.S., Universal, UrbanEye, Washington, Week in Review. World, Your Money
"""

def default_display():
    index_num = 0
    story_index = []
    for story in news['results']:
        if story['section'] in nyt_filter:
            story_index.append(story)
            index_num += 1
            click.secho('%r - ' % index_num, bold=True, nl=False)
            click.secho('%s ' % story['title'], fg='blue', bold=True, nl=False)
            click.secho('-- %s -- ' % story['source'], fg='magenta', bold=True, nl=False)
            click.secho('%s' % story['section'], fg='red')
            click.secho('Story abstract: %s' % story['abstract'], fg='cyan')
            click.echo()
    
    if index_num > 0:
        click.secho("Select an index number to go to story, or [Enter] to exit: ", fg='blue', bold=True, nl=False)
        selection = raw_input()
        if selection.isdigit():
            selection = int(selection)
            story = story_index[selection-1]
            click.launch(story['url'])
        else:
            pass
    else:
        click.secho("No recent headlines to display", fg='blue', bold=True, nl=False)

default_display()
