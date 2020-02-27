class Channel:
  def __init__(self, name, vc, tp):
    self.vc = vc
    self.name = name
    self.tp = tp
	

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Channel("HBO", 36, "J22")
p1.myfunc()