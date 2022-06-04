#網路連線
from statistics import mode
import urllib.request as request
src1 = 'https://www.ntu.edu.tw/'

with request.urlopen(src1) as response: #with request.urlopen(網站)連接網站用法
  data1 = response.read().decode('utf-8') #變數.read()，取得網址中網站的原始碼(HTML、CSS、JS)，decode('utf-8')可以將亂碼改成適用文字

print(data1)

#串接、擷取公開資料
import json
#網站來源:台北市政府公開資料
src2 = 'https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire'

with request.urlopen(src2) as response:
  data2 = json.load(response) #利用json模組處理json格式資料

#處理json資料，撈出要用的列表
DataList = data2['result']['results'] #觀察json檔中要撈出的列表
#將抓出來的資料寫入檔案
with open('python\demo13data.txt',mode='w',encoding='utf-8') as file:
#使用for迴圈將列表中的資料一一列出來(由json檔觀察列表的key&value)
  for company in DataList:
    file.write('公司名稱:' + company['公司名稱'] + ' 地址:' + company['公司地址'] + '\n')