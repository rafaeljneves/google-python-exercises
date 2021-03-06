#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    # -Extract the year and print it
    with open(filename, 'r') as arquivo:
        dict_rank_names = {}
        list_rank_names = []
        for linha in arquivo:
            ano = re.search('(Popularity in )([1-2][0-9]{3})', linha)
            rank = re.search('<td.*?>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td>', linha)

            if ano:
                list_rank_names.insert(0, ano.group(2))
                #print(ano.group(2))

            # -Extract the names and rank numbers and just print them
            if rank:
                #print(rank.group(2), rank.group(3), rank.group(1))

                # -Get the names data into a dict and print it
                for i in range(2, 4):
                    key, values = rank.group(i), rank.group(1)
                    dict_rank_names[key] = values
                #print(dict_rank_names)

        # -Build the [year, 'name rank', ... ] list and print it
        for k, v in sorted(dict_rank_names.items(), reverse=True):
            list_rank_names.insert(0, k + ' ' + v)

        list_rank_names[0] = list_rank_names[-1]
        list_rank_names.pop(-1)


    return list_rank_names


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]


    #Extrai dados do arquivo escolhido
    if args[0].endswith('.html'):
        arquivo = args[0]
        print('arquivo: ', arquivo)
        print(extract_names(arquivo))

    # For each filename, get the names, then either print the text output
    # or write it to a summary file
    if args[0] == '--lista':
        for root, dirs, files in os.walk(os.getcwd()):
            for file in sorted(files):
                if file.endswith('.html'):
                    print(extract_names(file))


if __name__ == '__main__':
    main()
