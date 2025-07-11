from stats import count_words, count_chars, sort_chars
import sys

def get_book_text(path_to_file :str) -> str:
    with open(path_to_file) as file:
        contents = file.read()
    return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Getting contents
    path = sys.argv[1]
    contents = get_book_text(path)
    character_distribution = count_chars(contents)

    # Printing report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(contents)} total words")
    print("--------- Character Count -------")
    for char in sort_chars(character_distribution):
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

if __name__=="__main__":
    main()
