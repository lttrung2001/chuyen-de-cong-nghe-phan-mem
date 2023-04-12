def read_docs():
  # Read doc file
  doc_file = open('datasets/doc-text', 'r')
  doc_dict = {}
  i = None
  tmp = ''
  try:
    for line in doc_file:
      strip_line = line.strip('\n')
      if strip_line.isdigit():
        i = int(strip_line)
      elif strip_line.endswith('/'):
        doc_dict[i] = tmp.strip()
        tmp = ''
      else:
        tmp += " {}".format(strip_line)
  except IndexError:
    print('end of file')
  doc_file.close()
  return doc_dict





def read_queries():
  # Read doc file
  query_file = open('datasets/query-text', 'r')
  query_list = []
  tmp = ''
  try:
    for line in query_file:
      strip_line = line.strip('\n')
      if strip_line.isdigit():
        continue
      elif strip_line.endswith('/'):
        query_list.append(tmp.strip())
        tmp = ''
      else:
        tmp += " {}".format(strip_line.lower())
  except IndexError:
    print('end of file')
  query_file.close()
  return query_list





def read_vocabs():
  # Read vocabulary file
  vocab_file = open('datasets/term-vocab', 'r')
  vocabs = []
  try:
    for line in vocab_file:
      vocabs.append(line.split()[1].lower())
  except IndexError:
    print('end of file')
  vocab_file.close()
  return vocabs