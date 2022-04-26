//定義函數
function test(){
  console.log('函數教學')
}

function add(num1,num2){ //能在函數內帶入值
  console.log('呼叫add函數')
  return num1+num2
  console.log('return之後的動作皆不做')
}

test() //呼叫test函數
let value = add(3,4) //將value的值定為add函數內的動作並呼叫(10)
console.log(value)
console.log(add(5,7)) //呼叫add函數,並帶入值



//建構函數
function createCard(initName){
  this.name = initName  //this綁定為函數建造的object
}

//new,建立構造,皆有name的屬性
const a1 = new createCard('一號')
const a2 = new createCard('二號')
const a3 = new createCard('三號')
const a4 = new createCard('四號')
const a5 = new createCard('五號')

console.log(a1)
console.log(a2)
console.log(a3)
console.log(a4)
console.log(a5)