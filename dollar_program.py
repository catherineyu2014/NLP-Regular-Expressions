# Catherine Yu
# NLP HW2 Program 1 -- dollar program

import re
import argparse
import numpy as np

# read file
def read_file(filename):
    with open (filename, 'r') as file:
        data = file.read()
    return data

# process file & extract
def process_file(data):
    num_dollars = re.findall(r'\$ ?[0-9]+(?:,[0-9]{3})*(?:\.[0-9]{2})?(?: ?[mM]illion|[tT]rillion|[bB]illion|[hH]undred|[tT]housand)? *(?:[cC]ents?)?(?:[dD]ollars?)?', data)

    str_dollars = re.findall(r'(?<!\')\b(?:\$ ?)?((?:(?:[aA]|[oO]ne|[tT]wo|[tT]hree|[fF]our|[fF]ive|[sS]ix|[sS]even|[eE]ight|[nN]ine|[tT]en|[tT]wenty|[tT]hirty|[fF]orty|[fF]ifty|[sS]ixty|[sS]eventy|[eE]ighty|[nN]inety)\b(?: ?(?:[hH]undred))?\b(?: ?(?:[mM]illion|[bB]illion|[tT]housand))?\b ?-?(?:[cC]ents?|[dD]ollars?)))\b', data)
    
    dollars = num_dollars + str_dollars
    
    return dollars

def main():
    parser = argparse.ArgumentParser(description='Process a text file for matching dollar amounts.')
    parser.add_argument('filename', type=str, help='The text file to process')
    args = parser.parse_args()

    data = read_file(args.filename)
    dollars_list = process_file(data)
    print(len(dollars_list))

    # create and open text file
    file = open('dollar_output.txt', 'w')
    for d in dollars_list:
        file.write(str(d) + '\n')

if __name__ == '__main__':
    main()
