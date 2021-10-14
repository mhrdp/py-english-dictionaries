from dictionaries.datamuse import Datamuse

import argparse
import colorama
import os
import sys

colorama.init()

def main_parser():
    parser = argparse.ArgumentParser(
        # prog = 'Python English Dictionaries',
        description = 'Access various english database APIs',
        usage = '%(prog) [option] word [max_result]',
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
        if sys.argv[1] == '--datamuse':
            if max_length:
                max_length = sys.argv[4]
                return datamuse_parser(sys.argv[3], max_result=max_length)
            return datamuse_parser(sys.argv[3])

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
                    result['word'].ljust(int(cols//3)) +
                    '\n\n'
                )
        else:
            # This is a manual example of ANSI code to change terminal text to red
            # This is just for an example if you don't want to use colorama library
            sys.stdout.write('\033[31m' + empty_text + '\n\n')
    
    if sys.argv[2] == 'like':
        like_result = datamuse_init.words(ml=word)
        if len(like_result) > 0:
            for result in like result:
                sys.stdout.write(
                    colorama.Fore.CYAN +
                    colorama.Style.DIM +
                    result['word'].ljust(int(cols//3)) +
                    '\n\n'
                )
        else:
            sys.stdout.write(colorama.Fore.RED + empty_text + '\n\n')
            

if __name__ == '__main__':
    main_parser()
