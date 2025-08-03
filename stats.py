def get_word_count(book):
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

def sort_on(items):
  return items["num"]

def sort_character_count(character_counts):
  sorted_character_counts = []
  for char in character_counts:
    character_count_dict = {"char": char, "num": character_counts[char]}
    sorted_character_counts.append(character_count_dict)
  sorted_character_counts.sort(reverse=True, key=sort_on)
  return sorted_character_counts
