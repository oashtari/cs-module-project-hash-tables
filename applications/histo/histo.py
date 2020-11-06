# Your code here
import random

# Read in all the words in one go
def convert(sntnc):
    if sntnc == '':
        return sntnc

    sntnc = sntnc.strip()
    sntnc = sntnc.replace('\n', ' ')
    sntnc = sntnc.replace('\r', ' ')
    sntnc = sntnc.replace('\t', ' ')

    to_ignore = r'":;,.-+=/\\|[]{}()*^&'

    new_sntnc = ''
    for char in sntnc:
        if char not in to_ignore:
            new_sntnc += char

    return new_sntnc.split()


with open("robin.txt") as f:
    words = f.read()
    
    cleaned_words = convert(words)

    # print('words', cleaned_words)   

    # new_words = words.split(' ')
    # Your code here
    words_dict = {}

    # list_of_words = convert(s)

    list_of_words = [i.lower() for i in cleaned_words]

    for word in list_of_words:
        if word != '':
            if words_dict.get(word) is None:
                words_dict[word] = 1
            else:
                words_dict[word] +=1

    whole_list = list(words_dict.items())

    whole_list.sort(key=lambda x: x[1], reverse=True)

    largest_key = max(len(key) for key in words_dict.keys())

    for item in whole_list:
        if not item[0].isalpha():
            pass
        else:
            space_num = largest_key - len(item[0])
            spaces = ' ' * space_num + '  '
            line = '#' * item[1]

            print(f'{item[0]}:{spaces}{line}')