/*
  object物件:
  宣告物件名稱
  一個key對應一個value
*/
const person ={ //person為物件
  name:'JOJO', //name為key,'JOJO'為value
  age:23, //age為key,23為value
  is_male:true, //is_male為key,true為value
  print_name:function(){ //可在object中做函數
    console.log(this.name)
  }
}

person.print_name() //呼叫物件函數
console.log(person.age) //呼叫物件中的值

//object結合陣列
const obj_arr = {
  title:'1995',
  maker:'公司',
  duration:114,
  actors:[
    {
      name:'一號',
      age:18
    },
    {
      name:'二號',
      age:20
    }
  ]
}

console.log(obj_arr.actors[1].name) //呼叫物件中的陣列的key

/*
  switch case,若case=switch()中的值則做某件事,並且break
  若沒有繼續看下一個case,直到最後出現default則做default的事件
*/
let key = 250

switch (key){
  case 100:
    console.log('考100')
    break
  case 200:
    console.log('考200')
    break
  case 300:
    console.log('考300')
    break
  default:
    console.log('缺考')
    break
}

/*
  while迴圈,()的條件會自動轉成布林值,
  true執行，false不停止
*/
let i = 1

while(i <= 3){
  console.log(i)
  i += 1 //i += 1等於i = i + 1
}
//do while迴圈(先做一次)
let k = 5

do{
  console.log(k)
  k += 1
}while(k<=3)
