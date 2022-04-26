/*
  陣列第一項為[0]第二項為[1]...以此類推
*/
const arr = [80,60,20,30,50] //陣列宣告多用const,即無法修改型態
console.log(arr) //列印陣列所有值
console.log(arr[0]) //列出陣列第一項
arr[1] = 10
console.log(arr[1])

console.log(arr.length) //列出陣列長度

arr.push(99) //從陣列後方增加一個值
console.log(arr)
arr.pop() //從陣列後方取出一個值
console.log(arr)
arr.unshift(99) //從陣列最前方(第0項)增加一個值
console.log(arr)
arr.shift() //從陣列最前方(第0項)取出一個值
console.log(arr)

let newarr = arr.filter(function(item){ //利用filter來做陣列篩選
  return item >= 30
})
console.log(newarr)

//當array傳入函數進行操作先copy一份在操作
function Num(list){
  var newArr = list.slice(0) //使用slice(0)copy,(0)為從第一項開始複製
  newArr.push("9");
  console.log(newArr)
}

const arr1 = [1,2,3];
Num(arr1);
console.log(arr1)
