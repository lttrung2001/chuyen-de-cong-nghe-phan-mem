def read_docs():
  # Read doc file
  doc_file = open('datasets/doc-text', 'r')
  doc_list = []
  tmp = ''
  strip_line = ''
  try:
    for line in doc_file:
      strip_line = line.strip('\n')
      if strip_line.isdigit():
        continue
      elif strip_line.endswith('/'):
        doc_list.append(tmp.strip())
        tmp = ''
      else:
        tmp += " {}".format(strip_line)
  except IndexError:
    print('end of file')
  doc_file.close()
  return doc_list