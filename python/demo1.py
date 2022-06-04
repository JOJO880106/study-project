#執行時入要清除頁面輸入cls指令即可
#此為註解方式

#變數的名稱只能用英文or數字or_的組合
#變數的開頭不能為數字
Name = '陳JO'
Age = 23
is_Male = True #使用布林值需要大寫 True&False

#印出，變數型態不同不能相加再一起
print(Name) #字串不能與數字相+印出來
print(Name + '的\n換行教學') #\n為換行
print('重複印出教學'*3) #字串可用*法重複印出

#三個單引號空格換行教學
print('''字串三個單引號換行教學
字串三個單引號換行教學
字串三個單引號換行教學''')

start = 'HELLO word'
#內建函式
print(start.lower()) #lower()將英文全部變小寫
print(start.upper()) #upper()將英文全部變大寫
print(start.lower().islower()) #判斷全部是否為小寫
print(start.lower().isupper()) #判斷全部是否為大寫
print(start.upper().islower()) #判斷全部是否為小寫
print(start.upper().isupper()) #判斷全部是否為大寫

#可使用[]來選取變數中的字體,[0]為第一個數,以此類推，也可選取範圍[0:3]0~2位或者[0:]意旨0到全部
print(start[0])
print(start[0:3])
print(start[0:])
print(start[-1]) #-1為倒數第一個數字以此類推

#index()可尋找變數中的某個字,並且判別在哪個位置,若同字串有兩個字會取最前面的
print(start.index('w'))
print(start.index('L'))

#replace()可替換變數中某個字的字
print(start.replace('L','z'))