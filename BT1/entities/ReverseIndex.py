class ReverseIndex:
  # This is constructor
  def __init__(self, freq = 0, s = set()):
    self.freq = freq
    self.s = s
  
  # Similar to toString in Java
  def __str__(self):
        return str(self.freq) + " " + str(self.s)

  # Use this method to update frequency and list
  def update(self, doc_id):
    if doc_id in self.s:
      return
    self.freq += 1
    self.s.add(doc_id)