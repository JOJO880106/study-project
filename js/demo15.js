let heightDOM = document.querySelector('.height')
let kgDOM = document.querySelector('.kg')
let sendDOM = document.querySelector('.send')
let resetDom = document.querySelector('.reset')
let list =document.querySelector('.list')

const arr =[]
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

//渲染畫面
function render(){
  let str = ''
  arr.forEach(function(item){
    return str += '<li>BMI指數為 :'+ item.bmi + 
    ' 狀態是 <span class="'+ 
    bmidata[item.status].class+'">' + 
    bmidata[item.status].statusText +'</span>' + ' bmi平均為:' +item.bmiavg +'</li>'
  })
  list.innerHTML = str
}

let bmisum = 0
sendDOM.addEventListener('click',function(){
  let thisheight = heightDOM.value //將取的DOM寫入變數中
  let thiskg = kgDOM.value //將取的DOM寫入變數中
  let bmi = parseInt(thiskg / (thisheight / 100 * thisheight / 100))
  bmisum += bmi
  let bmiavg = bmisum / (arr.length+1)
  //處理資料
  const userRecord = {
    height:'',
    kg:'',
    bmi:'',
    status:'',
    bmiavg:''
  }
  userRecord.height = thisheight
  userRecord.kg = thiskg
  userRecord.bmi = bmi
  userRecord.bmiavg = bmiavg
  if(bmi < 18.5){
    userRecord.status = 'overThin'
  }
  else if(bmi <= 24){
    userRecord.status = 'normal'
  }
  else if(bmi <= 27){
    userRecord.status = 'overweight'
  }
  else if(bmi <= 30){
    userRecord.status = 'mildObesity'
  }
  else if(bmi <= 35){
    userRecord.status = 'moderateObesity'
  }
  else{
    userRecord.status = 'severeObesity'
  }

  //放入陣列
  arr.push(userRecord)
  console.log(arr)
  //呼叫函數,渲染畫面
  render()

  heightDOM.value = ''
  kgDOM.value = ''

  resetDom.addEventListener('click',function(){
    arr.length = 0
    render()
  })
})