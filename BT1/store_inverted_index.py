# This file use to save reverse index data
# Import utils and needed class
from utils.read_vocab_file import read_vocabs
from utils.read_doc_file import read_docs
from utils.generate_locator_cards import generate_cards
from entities.InvertedIndex import InvertedIndex

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
  # Chưa có trong dict -> khởi tạo
  if card[0] not in my_dict:
    my_dict[card[0]] = InvertedIndex(0, set())
  # Doc chưa có trong postings set -> frequency + 1
  if card[1] not in my_dict[card[0]].s:
    my_dict[card[0]].freq += 1
  # Thêm doc_id vào postings set
  my_dict[card[0]].s.add(card[1])
file = open('reverse-index-data.txt', 'w')
# Save to file
for key, value in my_dict.items():
  file.write('{0}::{1}::{2}\n'.format(key, value.freq, value.s))
file.close()
