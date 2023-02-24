# This file use to save reverse index data
# Import utils and needed class
from utils.read_vocab_file import read_vocabs
from utils.read_doc_file import read_docs
from utils.generate_locator_cards import generate_cards
from entities.ReverseIndex import ReverseIndex

# Read vocabs from file
vocab_list = read_vocabs()
# Read docs from file
doc_list = read_docs()

# Generate locator cards (tạo danh sách thẻ định vị)
cards = generate_cards(doc_list)

# Sort cards
cards.sort()

# Tổng hợp danh sách thẻ định vị
my_dict = dict()
for card in cards:
  if card[0] not in my_dict:
    my_dict[card[0]] = set()
  my_dict[card[0]].add(card[1])
# Save to file
file = open('reverse-index-data.txt', 'w')
for key, value in my_dict.items():
  file.write('{0}::{1}\n'.format(key, value))
file.close()
