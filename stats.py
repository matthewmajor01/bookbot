def get_num_words (text):

    words =  text.split()
    num_words = len(words)
    return num_words

def get_character_dict (text):
    character_dict = {}

    for c in text:
        lower_case = c.lower()
        if lower_case not in character_dict:
            character_dict[lower_case] = 1
        else:
            character_dict[lower_case] += 1
    return character_dict

def get_sorted_chars (chars_dict):
    char_list = []

    for char, num in chars_dict.items():   
        sorted_char = {"char": char, "num": num}
        char_list.append(sorted_char)

    def sort_on_nums (entry):
        return entry["num"]

    char_list.sort(reverse=True, key=sort_on_nums)
    return char_list