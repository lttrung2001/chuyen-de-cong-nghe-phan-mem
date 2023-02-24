from entities.InvertedIndex import InvertedIndex
# This file use to read reverse index data
def read_inverted_index():
  file = open('reverse-index-data.txt', 'r')
  my_dict = {}
  for line in file:
    arr = line.split('::')
    my_dict[arr[0]] = InvertedIndex(arr[1], eval(arr[2]))
  return my_dict