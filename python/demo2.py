number1 = 12
number2 = 5
result = number1 / number2
result_int = number1 // number2 #整數除法用2個/

print(result)
print(result_int)

#字串數字轉換
print('轉字串教學' + str(number1)) #數字轉字串str()
print(int('12') + 5) #字串轉整數
print(float('3.5')+ 3) #字串轉浮點數


from math import * #載入math函式庫
number = -6.7

print(abs(number)) #絕對值用abs()
print(max(2,3,4,5,6,55,33,22)) #取最大值用max()
print(min(2,3,4,number,22)) #取最小值用min()
print(floor(5.2)) #無條件捨去用floor()，需載入math函式庫
print(ceil(5.2)) #無條件進入用ceil()，需載入math函式庫
print(round(number)) #取四捨五入用round()
print(pow(2,3)) #次放用pow(底數,次方)
print(2**4) #次方用**方式,底數**次方
print(sqrt(36)) #開根號用sqrt()
print(36**0.5) #開根號使用**方式,底數**0.5