import requests
import click
from filters import nyt_filter

"""
For NYT API documentation see: http://developer.nytimes.com/io-docs and http://developer.nytimes.com/docs/times_newswire_api/
For requests documentation see: http://www.python-requests.org/en/latest/
For additional news APIs see: http://www.programmableweb.com/news/81-news-apis-digg-fanfeedr-and-clearforest/2012/02/01
"""

click.clear()

raw_news = requests.get('http://api.nytimes.com/svc/news/v3/content/all/all/.json?limit=20&api-key=cb6b696a018707793e9436bda629bde3%3A4%3A66817738')

news = raw_news.json()

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
