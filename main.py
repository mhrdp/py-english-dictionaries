from dictionaries.datamuse import Datamuse
from dictionaries.freedict import FreeDictionary

import argparse
import colorama
import os
import sys

colorama.init()

def main_parser():
    parser = argparse.ArgumentParser(
        # prog = 'Python English Dictionaries',
        description = 'Access various english database APIs',
        usage = '%(prog) [option] word [optional:max_result]',
        allow_abbrev = False,
    )
    
    parser.add_argument(
        '--datamuse',
        type = str,
        help = 'type your word here',
        required = False,
    )
    
    max_length = None
    if len(sys.argv) > 2:
        if sys.argv[1] == '-datamuse':
            if max_length:
                max_length = sys.argv[4]
                return datamuse_parser(sys.argv[3], max_result=max_length)
            return datamuse_parser(sys.argv[3])

        if sys.argv[1] == '-freedict':
            return free_dictionary_parser(sys.argv[3])

def datamuse_parser(word, max_result=None):
    cols = os.get_terminal_size().columns
    datamuse_init = Datamuse()
    word = word.replace(' ', '+').lower()
    
    empty_text = '\nSorry, apparently no such result that you desire.'
    help_text = f'\nResult from word {word} in Datamuse:'
    sys.stdout.write(colorama.Style.BRIGHT + help_text + '\n')
    
    if sys.argv[2] == 'rythm':
        rythm_result = datamuse_init.words(rel_rhy=word, max=max_result)
        if len(rythm_result) > 0:
            for result in rythm_result:
                sys.stdout.write(
                    colorama.Fore.CYAN +
                    colorama.Style.DIM +
                    result['word'].ljust(int(cols//3))
                )
            sys.stdout.write('\n\n')
        else:
            # This is a manual example of ANSI code to change terminal text to red
            # This is just for an example, probably still need colorama.init()
            sys.stdout.write('\033[31m' + empty_text + '\n\n')
    
    if sys.argv[2] == 'like':
        like_result = datamuse_init.words(ml=word)
        if len(like_result) > 0:
            for result in like_result:
                sys.stdout.write(
                    colorama.Fore.CYAN +
                    colorama.Style.DIM +
                    result['word'].ljust(int(cols//3))
                )
            sys.stdout.write('\n\n')
        else:
            sys.stdout.write(colorama.Fore.RED + empty_text + '\n\n')

    if sys.argv[2] == 'suggest':
        suggest_result = datamuse_init.suggest(s=word)
        if len(suggest_result) > 0:
            for result in suggest_result:
                sys.stdout.write(
                    colorama.Fore.CYAN +
                    colorama.Style.DIM +
                    result['word'].ljust(int(cols//3))
                )
            sys.stdout.write('\n\n')
        else:
            sys.stdout.write(colorama.For.RED + empty_text + '\n\n')

def free_dictionary_parser(word):
    freedict_init = FreeDictionary()
    word = word.replace(' ', '+').lower()

    empty_text = '\nSorry, apparently no such result that you desire'
    help_text = f'\nResult from word {word} is:'
    sys.stdout.write(colorama.Style.BRIGHT + help_text + '\n')

    if sys.argv[2] == 'all':
        all_result = freedict_init.get_definitions(word)
        all_result[0]['word'] = all_result[0]['word'].upper()
        
        if len(all_result) > 0:
            sys.stdout.write(
                colorama.Style.BRIGHT +
                all_result[0]['word'] + '\n'
            )

            for result in all_result:
                sys.stdout.write(
                    colorama.Fore.WHITE +
                    colorama.Style.DIM +
                    result['meanings'][0]['partOfSpeech'] + '\n'
                )

                sys.stdout.write(
                    colorama.Fore.CYAN +
                    colorama.Style.BRIGHT +
                    'Meaning: ' +
                    result['meanings'][0]['definitions'][0]['definition'] + '\n'
                )

                if result['meanings'][0]['definitions'][0]['synonyms']:
                    sys.stdout.write(
                        'Synonyms: ' +
                        result['meanings'][0]['definitions'][0]['synonyms'][0] +
                        '\n\n'
                    )

                if result['meanings'][0]['definitions'][0]['antonyms']:
                    sys.stdout.write(
                        'Antonyms: ' +
                        result['meanings'][0]['definitions'][0]['antonyms'][0] +
                        '\n\n'
                    )


            sys.stdout.write('\n\n')
        else:
            sys.stdout.write(colorama.Fore.RED + empty_text + '\n\n')
            

if __name__ == '__main__':
    main_parser()
