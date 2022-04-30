let heightDOM = document.querySelector('.height')
let kgDOM = document.querySelector('.kg')
let sendDOM = document.querySelector('.send')
let bmiDOM = document.querySelector('.BMI')
let statusDOM = document.querySelector('.status')

const bmidata = {
  'overThin': {
    statusText:'體重過輕',
    class:'blue',
  },
  'normal': {
    statusText:'正常',
    class:'green',
  },
  'overweight': {
    statusText:'過重',
    class:'pink',
  },
  'mildObesity': {
    statusText:'輕度肥胖',
    class:'orange',
  },
  'moderateObesity': {
    statusText:'中度肥胖',
    class:'purple',
  },
  'severeObesity': {
    statusText:'重度肥胖',
    class:'red',
  }
}

function bmiresult(bmi){
  if(bmi < 18.5){
    render('overThin',bmi)
  }
  else if(bmi <= 24){
    render('normal',bmi)
  }
  else if(bmi <= 27){
    render('overweight',bmi)
  }
  else if(bmi <= 30){
    render('mildObesity',bmi)
  }
  else if(bmi <= 35){
    render('moderateObesity',bmi)
  }
  else{
    render('severeObesity',bmi)
  }
}

function render(status,bmiText){
  bmiDOM.textContent = bmiText //將bmiDOM透過.textContent修改成傳入的bimText值
  statusDOM.textContent = bmidata[status].statusText //將statusDOM透過.textContent修改bmidata物件中的值
  statusDOM.classList.remove(statusDOM.classList) //先刪除statusDOM上的class
  statusDOM.classList.add(bmidata[status].class) //新增statusDOM上的class(CSS中的字體顏色)
}

sendDOM.addEventListener('click',function(){
  let thisheight = heightDOM.value //將取的DOM寫入變數中
  let thiskg = kgDOM.value //將取的DOM寫入變數中
  let bmi = parseInt(thiskg / (thisheight / 100 * thisheight / 100))
  bmiresult(bmi)
})