class car:
  def  __init__(self,Name):
    self.Name = Name

  def start(self):
    print(self.Name)

#繼承
class porsche(car): #繼承方式
  def __init__(self,Name,age): #這裡的繼承等同於將car複製一分到porsche，porsche可覆蓋car的Class
    self.Name = Name
    self.age = age
  def start1(self):
    print(self.Name)

c1 = porsche('JOJO的保時捷',23)

print(c1.Name)
print(c1.age)
c1.start()
c1.start1()

#self綁定延伸討論
class card:
  def __init__(self,initName):
    self.initName = initName
  def  hello(self):
    print('hello '+self.initName)

c1 = card('JOJO')
c2 = card('陳JO')
c2.hellooooo = c1.hello #c2的hellooooo函數等於c1的hello函數

print(c1.initName)
print(c2.initName)
c1.hello()
c2.hellooooo() #因等於c1的函式，所以物件為c1的
c2.hello() #因C2物件為陳JO因此印出hello 陳JO