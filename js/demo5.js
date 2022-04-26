//如果考100我給1000$,80以上我給500$,60以上我給100,否則你給300$
let score1 = 100

if(score1 === 100){ //判別若一樣的用三個=,三個=比較嚴謹屬於強制等於
  console.log('我給你1000$')
}
else if(score1 >= 80){
  console.log('我給你500$')
}
else if(score1 >= 60){
  console.log('我給你100$')
}
else{
  console.log('你給我300$')
}

//如果你考100且今天下雨我給1000$,否則你給100
let score2 = 90
let rainy2 = true

if(score2 === 100 && rainy2 === true){
  console.log('我給你1000$')
}
else{
  console.log('你給我100$')
}

//如果你考100或今天下雨我給1000$,否則你給100
let score3 = 90
let rainy3 = true

if(score3 === 100 || rainy3 === true){
  console.log('我給你1000$')
}
else{
  console.log('你給我100$')
}

//如果你考100或今天沒有下雨我給1000$,否則你給100
let score4 = 90
let rainy4 = true

if(score4 ===100 || rainy4 !== true){ //!==為不等於,也可寫===false
  console.log('我給你1000$')
}
else{
  console.log('你給我100$')
}

//函數與if運用,在函數內做if判別能使用return取代else、else if
function addmoney(price1,price2,price3){
  let result = price1 + price2 + price3
  let message = '普通會員'

  if(result >= 50000){
    message = '尊榮會員'
    return message
  }
  if(result >= 20000){
    message = '白金會員'
    return message
  }
  return message
}

function max_num(a,b,c){
  if(a > b && a > c){
    return a
  }
  if(b > a && b > c){
    return b
  }
  return c
}

let msg = addmoney(10000,11000,1000)
console.log(msg)
console.log(max_num(10,3,25))