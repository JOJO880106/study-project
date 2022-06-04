#如果考100我給1000$,80以上我給500$,60以上我給100,否則你給300$
score1 = 100

if(score1 == 100):
  print('我給你1000$')
elif(score1 >= 80): #else if用elif
  print('我給你500$')
elif(score1 >= 60):
  print('我給你100$')
else:
  print('你給我300$')

#如果你考100且今天下雨我給1000$,否則你給100
score2 = 90
rainy2 = True

if(score2 == 100 and rainy2 == True): #這裡的&用and
  print('我給你1000$')
else:
  print('你給我100$')

#如果你考100或今天下雨我給1000$,否則你給100
score3 = 90
rainy3 = True

if(score3 == 100 or rainy3 == True): #這裡的||用or
  print('我給你1000$')
else:
  print('你給我100$')

#如果你考100或今天沒有下雨我給1000$,否則你給100
score4 = 90
rainy4 = True

if(score4 == 100 or rainy4 != True): #!=為不等於,也可寫==false
  print('我給你1000$') 
else:
  print('你給我100$')

#函式與if運用,在函式內做if判別能使用return當作else、else if
def addmoney(price1,price2,price3):
  result = price1 + price2 + price3
  message = '普通會員'
  
  if(result >= 50000):
    message = '尊榮會員'
    return message
  if(result >= 20000):
    message = '白金會員'
    return message
  return message

msg = addmoney(10000,11000,1000)
print(msg)

#使用函數比大小
def max_unm(a,b,c):
  if(a > b and a > c):
    return a
  if(b > a and b > c):
    return b
  return c

print(max_unm(10,3,25))

def power(base,exp=0): #函式的參數可以預設資料
  print(base ** exp) #開根號
power(3)

#函式的參數可以無限撰寫(*變數)括號加*號
def avg(*ns):
  sum = 0
  for n in ns:
    sum += n
  print(sum / len(ns))

avg(3,4)
avg(3,5,10)
avg(1,4,-1,-8)