//用alert做密碼驗證
let password = '123456'
let input
let i = 0
let out_of_limit = false

//因判別使用!==(嚴謹)因input輸入為string所以password需設定字串,若password使用數字則判別為不相同
while(password !== input && !out_of_limit){ //!out_of_limit這邊的!為與原_out_of_limit相反的值
  i += 1
  if(i <= 3){
    input = prompt('請輸入密碼:')
  }
  else{
    out_of_limit = true
  }
}

if(out_of_limit){
  alert('超出次數') //alert()為網頁警告提示,能跳出()中文字
}
else{
  alert('登入成功')
}