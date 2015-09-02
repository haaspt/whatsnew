import requests
import click
import os

"""
For NYT API documentation see: http://developer.nytimes.com/io-docs and http://developer.nytimes.com/docs/times_newswire_api/
For requests documentation see: http://www.python-requests.org/en/latest/
For additional news APIs see: http://www.programmableweb.com/news/81-news-apis-digg-fanfeedr-and-clearforest/2012/02/01
"""

os.system('clear')

raw_news = requests.get('http://api.nytimes.com/svc/news/v3/content/all/all/.json?limit=10&api-key=cb6b696a018707793e9436bda629bde3%3A4%3A66817738')

news = raw_news.json()

for story in news['results']:
    click.secho('%s ' % story['title'], fg='blue', bold=True, nl=False)
    click.secho('-- %s -- ' % story['source'], fg='magenta', bold=True, nl=False)
    click.secho('%s' % story['section'], fg='red')
    click.secho('Story abstract: %s' % story['abstract'], fg='cyan')
    print ""
    
click.secho("Press any key to exit: ", fg='blue', bold=True, nl=False)
click.pause(info="")
click.echo()
