def no_dups(s):
    # Your code here
    dups = {}

    words = s.split(' ')
    # print('words', words)

    if s == '':
        return s

    for word in words:
        if word not in dups:
            dups[word] = 0
        dups[word] +=1 

    dups = dups.keys()

    final = ' '

    return (final.join(dups))




if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))