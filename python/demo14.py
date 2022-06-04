#class
class IO:
  SupportedSrcs = ['console','file']
  def read(src):
    if src not in IO.SupportedSrcs:
      print('not supportedsrcs')
    else:
      print('read from',src)

#呼叫class
print(IO.SupportedSrcs)
IO.read('file')
IO.read('internet')

#class&object
class phone:
  def __init__(self,os,number,is_waterproof): #需用函數(__init__)(self,)來當做object
    self.os = os #將值寫入物件
    self.number = number
    self.is_waterproof = is_waterproof
  
  def is_ios(self): #在class中建立函式
    if self.os == 'ios':
      return True
    else:
      False
  def add(self,num1,num2):
    return num1 + num2

#使用變數來建造class中的物件與函數
phone1 = phone('ios',123,True)
print(phone1.os)
print(phone1.is_ios()) #呼叫phone1建造的class函式
print(phone1.add(2,3)) #呼叫phone1建造的class函式

#class&object做讀取檔案
class file:
#初始化函式寫入物件
  def __init__(self,name):
    self.name = name
    self.file = None #未開啟檔案因此為None
#實體方法(函式)
  def open(self):
    self.file = open(self.name,mode='r',encoding='utf-8')
  def read(self):
    return self.file.read()

#讀取第一個檔案
f1 = file('python\demo13data.txt')
f1.open()
data1 = f1.read()
print(data1)

#讀取第二個檔案
f2 = file('python\demo14data.txt')
f2.open()
data2 = f2.read()
print(data2)