#list是[],tuple是()，功能類似差別在於tuple不能被新增、刪除、修改
arr = [80,60,20,30,50]
aaa = (80,60,20,30,50)

print(arr) #印出list中的值
print(aaa) #印出tuple中的值
print(arr[0]) #列出第一項
print(arr[-1]) #在list列表中,若要選取其值倒數第一位為[-1]以此類推
print(arr[1:4]) #[1:4]為選取位置1~4(不包含第四)

arr[1] = 10
print(arr[1])
print(len(arr)) #len()能列出list、tuple的長度
print(len(aaa))

arr.append(99) #在list後放增加一個值用append()
print(arr)

arr.pop() #將list最後一位移除用pop()
print(arr)

arr1 = [30,40,50]
arr2 = [10,20,30]
arr3 = [30,40,50]
arr4 = [10,20,30]

arr1.extend(arr2) #list列表可以將兩個串接,用extend()
arr3 = arr3 + arr4 #list串接也可使用list+list來製作
print(arr1)
print(arr3)

arr1.insert(1,60) #在list中插入值用insert(位置,值)
print(arr1)

arr1.remove(60) #將list中的值刪除用remove(值)
print(arr1)

arr1.clear() #將list中清空用clear()
print(arr1)

arr.sort() #將list做由小到大做排序用sort()
print(arr)

arr.reverse() #將list做反轉用reverse()
print(arr)

print(arr.count(50))#在list中尋找值的位置用count(值)

arr[1:4] = [] #list可用[1:4]來選取並連續刪除
print(arr)