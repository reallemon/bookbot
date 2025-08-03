def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()

def word_count(book):
  words = book.split()
  return len(words)

def main():
  book_text = get_book_text("books/frankenstein.txt")
  print(f"{word_count(book_text)} words found in the document")

main()
