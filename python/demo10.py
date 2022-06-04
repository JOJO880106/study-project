#Module
import sys 
sys.path.append('PyModule') #在模組的搜尋路徑列表中新增路徑(若用相對路徑則由專案路徑開始搜尋)
print(sys.path) #印出模組的搜尋路徑列表

import geometry as gm #import可用as更改別名

result1 = gm.distance(1,1,5,5)
result2 = gm.slope(1,2,5,6)
print('兩點距離',result1)
print('斜率:',result2)

#封包應用,使用封包資料夾來放置module並且使用
#封包資料夾需與主程式在同層資料夾，並解需給予要一個__init__.py
import PyGeometry.point as point #import須為封包.module,可用as更改別名

result3 = point.distance(3,4)
print('與原點距離:',result3)