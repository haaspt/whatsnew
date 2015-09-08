import click
import newsoutlets
import random
from config import GlobalConfig


"""
For additional news APIs see: http://www.programmableweb.com/news/81-news-apis-digg-fanfeedr-and-clearforest/2012/02/01
"""

click.clear()

option = GlobalConfig()

story_list = newsoutlets.feeder()

def mixer(full_story_list, sample_number):
    
    mixed_story_list = random.sample(set(full_story_list), sample_number)
    return mixed_story_list


def default_display(list_of_stories):
    
    index_num = 0
    for story in list_of_stories:
        index_num += 1
        click.secho('%r - ' % index_num, bold=True, nl=False)
        click.secho('%s ' % story.title, fg='blue', bold=True, nl=False)
        click.secho('-- %s -- ' % story.source, fg='magenta', bold=True, nl=False)
        click.secho('%s' % story.section, fg='red')
        click.secho('Story abstract: %s' % story.abstract, fg='cyan')
        click.echo()
    
    if index_num > 0:
        exit == False
        while exit != True:
            click.secho("Select an index number to go to story, or [Enter] to exit: ", fg='blue', bold=True, nl=False)
            selection = raw_input()
            if selection.isdigit():
                selection = int(selection)
                story = mixed_story_list[selection-1]
                click.launch(story.url)
                if option.prompt_until_exit == True:
                    pass
                else:
                    return exit == True

            elif selection == '':
                return exit == True

            else:
                click.secho("Invalid entry", fg='red')
                if option.prompt_until_exit == True:
                    pass
                else:
                    return exit == True
                
    else:
        click.secho("No recent headlines to display", fg='blue', bold=True, nl=False)
        click.echo()

mixed_story_list = mixer(story_list, option.article_limit)
default_display(mixed_story_list)
