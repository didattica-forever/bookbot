import sys
from stats import get_num_words, count_characters, chars_dict_to_sorted_list

def get_book_text(file_name):
    file_contents = None
    with open(file_name) as f:
        file_contents = f.read()
    return file_contents




def main():
    text = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")
    sorted_list = chars_dict_to_sorted_list(count_characters(text))
    for item in sorted_list:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
    
if(len(sys.argv) < 2):
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
main()
    