def get_num_words(text):
    words = text.split()
    return len(words)

def get_dict_count(text):
    words = text.split()
    count_words = {}
    for word in words:
        for i in word:
            if i.lower() in count_words:
                count_words[i.lower()] += 1
            else: 
                count_words[i.lower()] = 1
    return count_words

def sort_characters_by_count(count_words):

    chars_list = []
    for char, count in count_words.items():
        chars_list.append({"char": char, "count": count})

    def sort_on(dict):
        return  dict["count"]

    chars_list.sort(reverse=True, key=sort_on)

    return chars_list
    
def print_report(path, word_count, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Print each character and its count
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        
        # Skip non-alphabetical characters
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")