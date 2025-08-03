def word_count(book):
  words = book.split()
  return len(words)

def character_count(book):
  character_counts = {}
  characters = list(book)
  for character in characters:
    lower_character = character.lower()
    if (lower_character in character_counts):
      character_counts[lower_character] += 1
    else:
      character_counts[lower_character] = 1
  return character_counts
