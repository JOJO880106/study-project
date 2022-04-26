//取得HTML物件
let content1 = document.getElementById('content')
let date1 = document.getElementById('date')
let time1 = document.getElementById('time')
let add1 = document.querySelector('.add')
let delete1 = document.querySelector('#deleteBtn')
let list = document.getElementById('list')

const arr = []

//函數
function render(){
  let htmlStr = ''
/*
  forEach將陣列做辨識內容並做for迴圈,
  function()中能放入item(陣列內容)、i(for迴圈的i)、arr(陣列本身)
*/
  arr.forEach(function(item){ 
    htmlStr += 
//在``模板中若要加入元素物件需要使用${}加入
    `
    <div class="item">
      <div>
        <p>內容:${item.content}</p>
        <p>時間:${item.date}${item.time}</p>
      </div>
    </div>
    `
  })
  list.innerHTML = htmlStr //使用innerHTM修改DOM
}

//監聽
add1.addEventListener('click',function(){
  arr.unshift({ //將值存放入陣列
    content:content1.value,
    date:date1.value,
    time:date1.value
  })
  render()
})

delete1.addEventListener('click',function(){
  arr.shift()
  render()
})