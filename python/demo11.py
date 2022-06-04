#文字檔案讀取與覆寫，用open開啟檔案
# open可存入變數，開啟後須關閉
# open('檔案路徑',mode = '開啟模式',encoding='utf-8')
# 檔案路徑分為絕對路徑以及相對路徑(同資料夾內)
# mode = 'r' 讀取
# mode = 'w' 覆寫
# mode = 'r+' 讀寫
# mode = 'a' 在原先資料後寫東西

# 也可使用with open('檔案路徑',mode = '開啟模式') as 變數，來存取即可不用關閉
with open('python\PyData.txt',mode = 'w',encoding='utf-8') as file: #若要寫入中文可多寫encoding='utf-8'
#存入變數後若要寫入則是變數.write()，會覆寫
  file.write('3\n5') #若要換行要用\n

with open('python\PyData.txt',mode='r',encoding='utf-8') as file:
#存入變數後可印出若讀取要變數.read()
  data = file.read() #將資料存入變數data

print(data)

sum = 0
with open('python\PyData.txt',mode='r',encoding='utf-8') as file:
#可用for迴圈將檔案中一行一行列出，也可存入變數做相加
  for line in file:
    sum += int(line)

print(sum)

#使用json格式讀取檔案以及覆寫檔案
import json
#從檔案中讀取json資料放入變數data中
with open('python\PyConfig.json',mode='r',encoding='utf-8') as file:
  data = json.load(file) #json檔的讀取需要使用json.load(變數)

print(data) #json讀取出來的資料為字典
print('name:',data['name'])
print('version:',data['version'])

data['name'] = 'new name'
with open('python\PyConfig.json',mode='w',encoding='utf-8') as file:
  json.dump(data,file) #將資料覆寫入json用法，json.dump(要寫入的資料變數,檔案變數)
print(data)