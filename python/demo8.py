# while迴圈,條件會自動轉成布林值,
# true執行，false不停止
from unittest import result


i = 1
while i <= 3:
  print(i)
  i += 1

k = 5
while k <= 3:
  print(k)
  k += 1
else:
  print(k)

#for迴圈使用for 變數 in range(範圍)，若範圍為3則變數是從0,1,2開始
for j in range(4):
  print(j)

#for迴圈使用for 變數 in list，會將list中內容一一列出
arr = ['紅','橙','黃','綠','藍']

for l in arr:
  print(l)

#while與for迴圈能使用break強制結束迴圈
n = 0
while n<5:
  if n == 3:
    break
  print(n) #印出迴圈中的n
  n += 1
print('最後的n:',n) #印出結束迴圈後的n

#while與for迴圈能使用continue跳出迴圈但不結束
a = 0
for x in [0,1,2,3]:
  if x % 2 == 0:
    continue
  print(x)
  a += 1
print('最後的a:',a)

#while與for迴圈能使用else迴圈結束前先執行else內動作
sum = 0
for z in range(11):
  sum += z
else:
  print(sum) #印出0+1+2+...+10的結果

#運用函數以及for迴圈算次方
def power(base_num,pow_num):
  result = 1
  for index in range(pow_num):
    result = result * base_num
  return result
print(power(2,0))

#綜合範例找出平方根
#輸入9得到平方根3
#輸入11得到沒有整數平方根
v = input('輸入一個正整數:')
v = int(v)
for c in range(v): #c從0 ~ v-1
  if c * c == v:
    print('整數平方根=',c) #用break強制結束迴圈並不會執行else區塊
    break
else:
  print('沒有整數平方根')