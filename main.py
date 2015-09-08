import click
import newsoutlets
import random
from config import GlobalConfig


"""
For additional news APIs see: http://www.programmableweb.com/news/81-news-apis-digg-fanfeedr-and-clearforest/2012/02/01
"""

click.echo("Loading the news...")

option = GlobalConfig()

story_list = newsoutlets.feeder()

click.clear()

def mixer(full_story_list, sample_number):
    
    mixed_story_list = random.sample(set(full_story_list), sample_number)
    return mixed_story_list


def default_display(list_of_stories):
    
    index_num = 0
    for story in list_of_stories:
        index_num += 1
        click.secho('%r - ' % index_num, bold=True, nl=False)
        click.secho('%s ' % story.title, fg=option.headline_color, bold=True, nl=False)
        click.secho('-- %s -- ' % story.source, fg=option.source_color, bold=True, nl=False)
        click.secho('%s' % story.section, fg=option.section_color)
        click.secho('Story abstract: %s' % story.abstract, fg=option.abstract_color)
        click.echo()
    
    if index_num > 0:
        exit == False
        while exit != True:
            click.secho("Select an index number to go to story, or [Enter] to exit: ", fg='blue', bold=True, nl=False)
            raw_selection = raw_input()
            if raw_selection.isdigit():
                selection = int(raw_selection) - 1
                if selection <= index_num - 1:
                    story = mixed_story_list[selection]
                    click.launch(story.url)
                    if option.prompt_until_exit == True:
                        pass
                    else:
                        return exit == True
                else:
                    click.secho("Invalid entry", fg='red')
                    if option.prompt_until_exit == True:
                        pass
                    else:
                        return exit == True

            elif raw_selection == '':
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
