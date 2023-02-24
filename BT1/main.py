from read_inverted_index import read_inverted_index
from utils.read_doc_file import read_docs
def intersect(p1, p2):
  answer = []
  i1 = 0
  i2 = 0
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

if __name__ == '__main__':
  # Test: visible and wendelstein and with
  doc_dict = read_docs()
  vocab_dict = read_inverted_index()
  results = intersect(
    sorted(vocab_dict["visible"].s),
    sorted(vocab_dict["with"].s)
  )
  for res in results:
    print(doc_dict[res])
    print()
    print()