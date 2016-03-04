
def length(string):
    """1:Caculates the length of any string,Also could do this with len(str)"""
    count = 0
    for letter in string:
        count += 1
    return count


def count_every_letter(string):
    """ 2: counts every letter, symbol and number in a given string. """
    results = {}
    for letter in string:
        if letter in results:
            results[letter] += 1
        else:
            results[letter] = 1
    return results 


def first2_last2(string):
    """ 3: returns a string with the first two and last chars from given string
    If the string is less than two char it returns 'Empty String'
    """
    if len(string) < 2:
        return "Empty String"
    else:
        return "{}{}".format(string[0:2], string[-2:])


def change_repeat(word):
    """ 4: replaces any re used letter in a string into a $. """
    word = list(word)
    used = []
    index = 0
    for letter in word:
        if letter in used:
            word[index] = '$'
        else:
            used.append(letter)
        index += 1
    return ''.join(word)


def swap_beginning(string1, string2):
    """ 5: Takes in two strings and returns it in one sring and swaps the first
    two letters of each word with the other. (ex: 'abc', 'xyz' = 'xyc abz')
    """
    new1 = string1[:2] + string2[2:]
    new2 = string2[:2] + string1[2:]
    return "{} {}".format(new1, new2)


def ingly(word):
    """ 6: Adds a 'ing' to the end of a given word.
    If the word allready ends with 'ing' we add 'ly instead.
    """
    if word[-3:] == 'ing':
        new_word = word + 'ly'
    else:
        new_word = word + 'ing'
    return new_word


def not_bad_good(string):
    """ 7: Recieves a string from user and if the sentence has not
    and then later bad we replace everything between them woth good!
    ex: 'The lyrics are not that bad!' = 'The lyrics are good!'
    """
    sentence = string.split()
    snot = string.find('not')
    sbad = string.find('bad')
    if sbad > snot:
        sentence = string.replace(string[snot:(sbad + 3)], 'good')
    else:
        sentence = string
    return sentence

def longest_word(lists):
    """ 8: Shows the longest word or words in a sentence! """
    lists = lists.split()
    longest = ''
    extra = ''
    for word in lists:
        if len(word) > len(longest):
            longest = word
            extra = ''
        elif len(word) == len(longest):
            extra += ", {}".format(word)
    print("The longest word in your sentence is {}!".format(len(longest)))
    print("These are the word:")
    return "        {}".format(longest + extra)


def remove_n(string, n):
    """ 9: Removes a given letter by by the number given."""
    words = list(string)
    del words[n-1]
    return ''.join(words)


def life_is_(string):
    """ 10: Swaps the first letter with the last letter of a given word."""
    new_string = string[-1:] + string[1:-1] + string[:1]
    return new_string


print(life_is_("nuzz yeah nuzz"))
