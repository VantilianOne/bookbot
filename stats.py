def count_words (book_text):
    words = len(book_text.split())
    return words

def character_count (book_text):
    chars = {}
    for letter in book_text:
        letter = letter.lower()
        if letter in chars:
            chars[letter] += 1
        else :
            chars[letter] = 1
    return chars

def sort_on(cnt): #create key to sort on num
    return cnt["num"]

def sort_chars (dict):
    list_of_dicts = []
    for entry, ct in dict.items():
        if entry.isalpha():
            a = {"char":entry, "num":ct}
            list_of_dicts.append(a)
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts
