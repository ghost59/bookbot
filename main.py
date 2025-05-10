from stats import counters, sorting, count_character
import sys

def main():
    
    print(f"sys.arge: {sys.argv}")
    print(f"Length of sys.argv: {len(sys.argv)}")
    if len(sys.argv) != 2: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    with open(path, "r") as f:
        contents = f.read()
    word_count = counters(contents)

    char_counts = count_character(contents)
    
    sorted_chars = sorting(char_counts)
    print(word_count)
    print(sorted_chars)
    print(f"Found {word_count} total words")

    for item in sorted_chars:
        if not item["ch"].isalpha():
            continue
        print(f"{item['ch']}: {item['num']}")

main()