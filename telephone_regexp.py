# Catherine Yu
# NLP HW2 Program 2 -- telephone program

import re
import argparse

# read file
def read_file(filename):
    with open (filename, 'r') as file:
        data = file.read()
    return data

# process file & extract
def process_file(data):
    #num = re.findall(r'(?:\+1)? ?\(?([0-9]{3})\)? ?(?:-| )?([0-9]{3}(?:-| )?[0-9]{4})', data)
    num = re.findall(r'(?:\+1 ?)?(\(?[0-9]{3}\)?[- ]?[0-9]{3}[- ]?[0-9]{4})', data)
    return num

def main():
    parser = argparse.ArgumentParser(description='Process a text file for matching telephone numbers.')
    parser.add_argument('filename', type=str, help='The text file to process')
    args = parser.parse_args()

    data = read_file(args.filename)
    telephone_list = process_file(data)
    
    #print(telephone_list)

    # create and open text file
    file = open('telephone_output.txt', 'w')
    for t in telephone_list:
        file.write(t + '\n')

    

if __name__ == '__main__':
    main()
