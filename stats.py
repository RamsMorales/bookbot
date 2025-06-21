def count_words(contents : str) -> int:
    return len(contents.split())

def count_chars(contents : str) -> dict:
    result = {}
    for char in contents:
        lower_char = char.lower()
        if lower_char not in result:
            result[lower_char] = 1
        else:
            result[lower_char] = result[lower_char] + 1
    return result

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(items):
    return items["num"]

def sort_chars(char_dict : dict) -> list:
    result = []
    for key in char_dict:
        #print(f"{key}:{char_dict[key]}")
        result.append({"char": key, "num":char_dict[key]})
    result.sort(key=sort_on,reverse=True)
    return result
