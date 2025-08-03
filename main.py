from stats import get_word_count, character_count, sort_character_count

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
  filepath = "books/frankenstein.txt"
  book_text = get_book_text(filepath)
  char_count = character_count(book_text)
  sorted_char_count = sort_character_count(char_count)
  print_output(filepath, get_word_count(book_text), sorted_char_count)

main()
