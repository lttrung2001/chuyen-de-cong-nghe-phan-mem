class ReverseIndex:
  # This is constructor
  def __init__(self, doc_id):
    self.freq = 1
    self.l = [doc_id]
  
  # Similar to toString in Java
  def __str__(self):
        return str(self.freq) + " " + str(self.l)

  # Use this method to update frequency and list
  def update(self, doc_id):
    if doc_id in self.l:
      return
    self.freq += 1
    self.l.append(doc_id)