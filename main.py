import click
import newsfeeds
import random
import sys
from config import GlobalConfig

def terminal_resize():
    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=40, cols=150))

def mixer(full_story_list, sample_number):
    """Selects a random sample of stories from the full list to display to the user.
    Number of stories is set in config.py
    Todo: Add argument support for number of stories to display
    """

    mixed_story_list = random.sample(set(full_story_list), sample_number)
    return mixed_story_list


def default_display(list_of_stories):
    """Displays a set of stories in the following format:
    n - Story Title -- OutletName -- Section 
    Story abstract: Lorem ipsum dolor sit amet
    """

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
        exit_now == False
        while exit_now != True:
            click.secho("Select an index number to go to story, or [Enter] to exit: ", fg=option.prompt_color, bold=True, nl=False)
            raw_selection = raw_input()
            if raw_selection.isdigit():
                selection = int(raw_selection) - 1
                if selection <= index_num - 1:
                    story = mixed_story_list[selection]
                    click.launch(story.url)
                    if option.prompt_until_exit == True:
                        pass
                    else:
                        return exit_now == True
                else:
                    click.secho("Invalid entry", fg='red')
                    if option.prompt_until_exit == True:
                        pass
                    else:
                        return exit_now == True

            elif raw_selection == '':
                return exit_now == True

            else:
                click.secho("Invalid entry", fg='red')
                if option.prompt_until_exit == True:
                    pass
                else:
                    return exit_now == True
                
        else:
            click.secho("No recent headlines to display", fg=option.prompt_color, bold=True, nl=False)
            click.echo()

def main():
    click.echo("Loading the news...")
    global option
    option = GlobalConfig()
    story_list = newsfeeds.feeder()
    global exit_now
    exit_now = False
    terminal_resize()
    click.clear()
    mixed_story_list = mixer(story_list, option.article_limit)
    default_display(mixed_story_list)

if __name__ == '__main__':
    main()
