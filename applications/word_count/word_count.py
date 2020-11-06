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

    # return new_sntnc



    return new_sntnc.split()

def word_count(s):
    # Your code here
    words = {}

    list_of_words = convert(s)

    list_of_words = [i.lower() for i in list_of_words]
    # print('list', list_of_words)

    if len(list_of_words) == 0:
        return words

    for word in list_of_words:
        if word != '':
            if words.get(word) is None:
                words[word] = 1
            else:
                words[word] +=1
            # if word not in words:
            #     words[word] = 0
            # words[word]+=1

    return words

# def word_count(s):
#     s += ' '
#     word_dict = {}
#     cur_word = ''
#     for c in s:
#         if c.isspace():
#             if cur_word in word_dict:
#                 word_dict[cur_word] += 1
#             elif cur_word != '':
#                 word_dict[cur_word] = 1
#             cur_word = ''
#         elif c.isalnum() or c == "'":
#             cur_word += c.lower()
#     return word_dict




if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('":;,.-+=/\\|[]{}()*^&'))
    print(word_count('a a\ra\na\ta \t\r\n'))