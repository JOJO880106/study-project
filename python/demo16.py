#問答題

#用class物件建構題目以及答案
class question:
  def __init__(self,description,answer):
    self.description = description
    self.answer = answer 

#將題目寫入list
test = [
  '香蕉是甚麼顏色?\n(a)紅色\n(b)綠色\n(c)黃色\n',
  '草莓是甚麼顏色?\n(a)紅色\n(b)綠色\n(c)黃色\n',
  '奇異果是甚麼顏色?\n(a)紅色\n(b)綠色\n(c)黃色\n'
]

#呼叫class將題目以及答案寫入q1
q1 = [
  question(test[0],'c'),
  question(test[1],'a'),
  question(test[2],'b')
]

#將執行寫入函式
def run_test(questions):
  score = 0 #答對題數
  for question in questions: #這裡的question與class的question無關
    answer = input(question.description) #用變數紀錄答案，這裡的question為for迴圈內容物(q1)的question物件
#若紀錄的答案與物件中的答案相同則答對+1   
    if answer == question.answer: #這裡的question為for迴圈內容物(q1)的question物件
      score += 1
#印出結果
  print('你得到' + str(score) + '分，共' + str(len(questions)) + '題')

#呼叫函式
run_test(q1)