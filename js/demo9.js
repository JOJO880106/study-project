/*
  for迴圈,需要再for()設條件,條件內會在{}中執行事件,
*/
for(let i = 0;i <= 3;i += 1){
  console.log(i)
}

let arr = ['紅','橙','黃','綠','藍']

for(let j = 0;j < arr.length;j += 1){
  console.log(arr[j])
}

//二維陣列 & 巢狀迴圈
let arr1 = [
  ["紅","橙","黃"],
  ["綠","藍","靛"],
  ["紫","黑","白"],
  ["灰"]
]

for(let k = 0;k < arr1.length;k += 1){
  for(let l = 0;l <arr1[k].length;l += 1){
    console.log(arr1[k][l])
  }
}