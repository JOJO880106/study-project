#終極密碼，隨機生成一個數字並且只有三次猜題機會
import random #若要使用亂數需先import random

num = random.randint(1,100) #亂數生成1~100需用random.randint(範圍)，這裡只有整數
ans = None 
ans_count = 0
ans_limit = 5 #最高猜題次數
result = False #判斷是否答對

while ans != num and ans_count < ans_limit: #輸入答案為正確答案或大於次數跳出迴圈
  ans_count += 1
  ans = int(input('請輸入數字:'))
  if num > ans:
    print('再大一點')
  elif num < ans:
    print('再小一點')
  else:
    result = True

if result == True:
  print('答對了')
else:
  print('失敗,答案為:',num)