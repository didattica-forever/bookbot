def get_num_words(text):
    return len(text.split())


def count_characters(text):
    dictionary = {}
    text = text.lower()
    for char in text:
        if str(char) not in dictionary.keys():
            dictionary[str(char)] = 1
        else:
            dictionary[str(char)] += 1
    return dictionary


# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(items):
    return items["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict: # converte il dictionary in una lista di dictionaries
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

