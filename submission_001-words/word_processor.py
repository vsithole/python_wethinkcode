
import string

def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)


def convert_to_word_list(text):
   
    delimiters = ".,;? "
    new_text = split(delimiters, text)
    
    lowered = list(map(lambda x : x.lower(),new_text))
    new_lower = [word for word in lowered if word != ""]

    return new_lower


def words_longer_than(length, text):
    
    new_lower = convert_to_word_list(text)
    longer = [word for word in new_lower if len(word) > length]
    
    return longer


def words_lengths_map(text):

    list_text = convert_to_word_list(text)

    list_len = list(map(lambda new_lis:len(new_lis),list_text))
    list_len.sort()
    new_dict = dict((i, list_len.count(i)) for i in list_len)
    
    return new_dict

def letters_count_map(text):
    
    list_text = convert_to_word_list(text)

    newm = list(string.ascii_lowercase)
    new__ = [x for z in list_text for x in z]
    new_dict = dict((i, new__.count(i)) for i in newm)

    return new_dict

def most_used_character(text):
    if text =='':
        return 
    else:
        dict_list = letters_count_map(text)
        max_val = max(dict_list, key= dict_list.get)
        
        return max_val

