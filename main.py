from stats import word_count, character_count

def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()

def main():
  book_text = get_book_text("books/frankenstein.txt")
  print(f"{word_count(book_text)} words found in the document")
  print(character_count(book_text))

main()
