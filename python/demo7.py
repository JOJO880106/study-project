#集合的用法，使用{}來存放物件
from unicodedata import name


set1 = {3,4,5}
set2 = {4,5,6,7}

print(set1)
#in與not in查詢set方法，若拿來查詢字典則會判斷key
print(3 in set1) #透過in查詢3是否有在set內
print(10 not in set1) #透過not in查詢10不再set內

set3 = set1 & set2 #兩個集合可以用交集取相同的資料，&
print(set3)

set4 = set1 | set2 #兩個集合可以用聯集取相同且不重複的資料，|
print(set4)

set5 = set1 - set2 #兩個集合相減為差集,會減去重疊的部分
print(set5)

set6 = set1 ^ set2 #兩個集合中使用^,能取兩個集合中部重疊的部分稱為反交集
print(set6)

s = set('Hello') #set(字串),能將字串拆解成集合,但不重複
print('H' in s)

#字典用法，使用{}來存放key,value
dic = {
  'name':'JO',
  'age':23,
  'is_male':True
}
dic['name'] = '陳JO'
print(dic['name'])
print(dic)

del dic['name'] #字典能使用del來刪除內部鍵值
print(dic)

dic1 = {i:i * 2 for i in [3,4,5]} #字典能使用list來產生
print(dic1)