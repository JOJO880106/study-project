#建立一個計算機
num1 = input('請輸入第一個數字:')
op = input('請輸入運算符號:')
num2 = input('請輸入第二個數字:')

num1 = float(num1)
num2 = float(num2)
result = 0

if op == '+':
  result = num1 + num2 
  print('答案為:',result)
elif op == '-':
  result = num1 - num2
  print('答案為:',result)
elif op == '*':
  result = num1 * num2 
  print('答案為:',result)
elif op == '/':
  result = num1 / num2 
  print('答案為:',result)
else:
  print('輸入有誤')
  