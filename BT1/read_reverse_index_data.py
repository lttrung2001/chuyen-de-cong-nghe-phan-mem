# This file use to read reverse index data
from entities.ReverseIndex import ReverseIndex
file = open('reverse_index_data.txt', 'r')
my_dict = {}
for line in file:
  ls = line.split('::')
  my_dict[ls[0]] = ReverseIndex(ls[1], eval(ls[2]))