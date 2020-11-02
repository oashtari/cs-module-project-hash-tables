def letter_count(s):
    d = {}

    for c in s:
        # function that checks if item is in alphabet
        if not c.isalpha():
            continue
        """
        if c not in d:
            d[c] = 1
        else:
            d[c] +=1 
        """

        if c not in d:
            d[c] = 0

        d[c]+=1

    return d 


print(letter_count("aabbba aa#$dd#!$dddabddf"))