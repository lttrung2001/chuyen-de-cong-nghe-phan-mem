from read_inverted_index import read_inverted_index
from utils.read_doc_file import read_docs
import math
def intersect(p1, p2):
  answer = []
  i1 = i2 = 0
  while i1 < len(p1) and i2 < len(p2):
    if p1[i1] == p2[i2]:
      answer.append(p1[i1])
      i1 += 1
      i2 += 1
    elif p1[i1] < p2[i2]:
      i1 += 1
    else:
      i2 += 1
  return answer

def intersect_skip(list1, list2):
  i1 = i2 = 0
  len1, len2 = len(list1), len(list2)
  skip1 = int(math.sqrt(len1))
  skip2 = int(math.sqrt(len2))

  skip_dict_1 = {}
  skip_dict_2 = {}

  while i1 + skip1 < len1:
    skip_dict_1[i1] = list1[i1 + skip1]
    i1 += skip1
  while i2 + skip2 < len2:
    skip_dict_2[i2] = list2[i2 + skip2]
    i2 += skip2

  answer = []

  i1 = i2 = 0
  while i1 < len1 and i2 < len2:
    if list1[i1] == list2[i2]:
      answer.append(list1[i1])
      i1 += 1
      i2 += 1
    elif list1[i1] < list2[i2]:
      if i1 in skip_dict_1 and skip_dict_1[i1] <= list2[i2]:
        while i1 in skip_dict_1 and skip_dict_1[i1] <= list2[i2]:
          i1 += skip1
      else:
        i1 += 1
    else:
      if i2 in skip_dict_2 and skip_dict_2[i2] <= list1[i1]:
        while i2 in skip_dict_2 and skip_dict_2[i2] <= list1[i1]:
          i2 += skip2
      else:
        i2 += 1
  return answer



if __name__ == '__main__':
  # Test: visible and wendelstein and with
  doc_dict = read_docs()
  vocab_dict = read_inverted_index()

  intersect_results = intersect(
    sorted(vocab_dict["visible"].s),
    sorted(vocab_dict["with"].s)
  )
  print(intersect_results)

  intersect_skip_results = intersect_skip(
     sorted(vocab_dict["visible"].s),
     sorted(vocab_dict["with"].s)
  )
  print(intersect_skip_results)