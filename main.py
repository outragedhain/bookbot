import sys
from stats import get_book_text, character_count, sorted_list

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]
    a = get_book_text(path_to_book)  # No need for str() conversion
    print(f"Found {a} total words")    
    b = character_count(path_to_book)  # No need for str() conversion
    c = sorted_list(b)
    print(c)
main()



    








    
