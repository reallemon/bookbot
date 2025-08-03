from stats import get_word_count, character_count, sort_character_count
import sys

def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()

def print_output(filepath, word_count, sorted_char_count):
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {filepath}...")
  print("----------- Word Count ----------")
  print(f"Found {word_count} total words")
  print("--------- Character Count -------")
  for char_dict in sorted_char_count:
    if (char_dict["char"].isalpha()):
      print(f"{char_dict['char']}: {char_dict['num']}")
  print("============= END ===============")

def main():
  if (len(sys.argv) != 2):
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  filepath = sys.argv[1]
  book_text = get_book_text(filepath)
  char_count = character_count(book_text)
  sorted_char_count = sort_character_count(char_count)
  print_output(filepath, get_word_count(book_text), sorted_char_count)

main()
