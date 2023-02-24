# This file use to read reverse index data
file = open('reverse-index-data.txt', 'r')
my_dict = {}
for line in file:
  arr = line.split('::')
  my_dict[arr[0]] = eval(arr[1])

# Test: visible and wendelstein and with
s1 = my_dict["visible"]
s2 = my_dict["wendelstein"]
s3 = my_dict["with"]
print(len(s1), len(s2), len(s3))
print(s1)
print(sorted(s1))
r1 = s1 & s2
print(r1)
r2 = r1 & s3
print(r2)