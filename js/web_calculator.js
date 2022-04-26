let num1 = prompt('請輸入數字1:') //prompt()能使網頁跳出輸入框,要求輸入,值為string
let num2 = prompt('請輸入數字2:')

/*
  將值由string轉數字
  整數:parseInt
  有小數的數:parseFloat
*/
num1 = parseFloat(num1) 
num2 = parseFloat(num2)

document.write(num1 + num2)