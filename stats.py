def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_content = f.read()
        words_list = file_content.split()
        num_of_words = len(words_list)
        return num_of_words

def character_count(path_to_file):
    with open(path_to_file) as f:
        file_content = f.read()
        char_count_dictionary = {}
        lower_case = file_content.lower()
        for char in lower_case:
            if char in char_count_dictionary:
                char_count_dictionary[char] += 1
            else:
                char_count_dictionary[char] = 1
        return char_count_dictionary
    
def sort_on(char_dict):
    return char_dict["count"]
def sorted_list(char_count_dictionary):
    char_count_list = [{"char": char, "count": count} for char, count in char_count_dictionary.items()]
    char_count_list.sort(reverse=True, key=sort_on)
    for char_dict in char_count_list:
        char = char_dict["char"]
        count = char_dict["count"]
        print(f"{char}: {count}")





            
        