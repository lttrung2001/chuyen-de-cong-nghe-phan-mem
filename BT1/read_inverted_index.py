from entities.InvertedIndex import InvertedIndex
# This file use to read reverse index data
file = open('reverse-index-data.txt', 'r')
my_dict = {}
for line in file:
  arr = line.split('::')
  my_dict[arr[0]] = InvertedIndex(arr[1], eval(arr[2]))

# Test: visible and wendelstein and with
s1 = my_dict["visible"].s
s2 = my_dict["wendelstein"].s
s3 = my_dict["with"].s
print(len(s1), len(s2), len(s3))
r1 = s1 & s2
print(r1)
r2 = r1 & s3
print(r2)