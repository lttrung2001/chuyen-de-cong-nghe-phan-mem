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
# Cần sửa: For theo từ điển
first_card = cards[0]
current_term = first_card[0]
current_class = ReverseIndex(first_card[1])
my_dict = dict()
for card in cards:
  if card[0] != current_term:
    my_dict[current_term] = current_class.__str__()
    current_class = ReverseIndex(card[1])
    current_term = card[0]
  else:
    current_class.update(card[1])

print(my_dict)