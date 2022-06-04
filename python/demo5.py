#定義函式
def test():
  print('函式教學')

def add(num1,num2):
  print('呼叫add函式')
  return num1 + num2 #retune會回傳值,回傳後的動作皆不做
  print('return後的動作皆不執行')

test() #呼叫test函數
value = add(3,4) #呼叫add函式
print(value)
print(add(5,7)) #呼叫add函數,並帶入值