def read_vocabs():
  # Read vocabulary file
  vocab_file = open('datasets/term-vocab', 'r')
  vocab_list = []
  try:
    for line in vocab_file:
      vocab_list.append(line.split()[1])
  except IndexError:
    print('end of file')
  vocab_file.close()
  vocab_list.sort()
  return vocab_list