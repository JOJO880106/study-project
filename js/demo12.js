/*
  取得html物件方式
  document.getElementById,只能取得id
  document.querySelector,能取得id與class,id需+#,class需+.
*/
let title1 = document.querySelector('#title')
let btn1 = document.querySelector('#btn')
let box1 = document.getElementById('box')
let input = document.getElementById('input1')
let img1 = document.getElementById('img')

//取得物件後可修改,innerText為修改文字,innerHTML為修改DOM模板
title1.innerText = '取得html物件、監聽，網站教學'
box1.innerHTML = `<p>innerHTML的DOM修改教學<p/>` //innerHTML後要使用``來匡列內容,``為模板樣式

//監聽
btn1.addEventListener('click',function(){ //click按下後做後面函數
  alert('你按了')
  this.innerText = '你真的按了'
  this.style.color = 'red' //style.color為修改文字顏色
})

input.addEventListener('keyup',function(e){ //keyup為鍵值,偵測按下甚麼
  console.log(e.metaKey.value)
})

img1.addEventListener('mouseover',function(){ //mouseover為滑鼠移至後做函數事件
  this.src = 'img2 example.jpg' //更換照片
})
img1.addEventListener('mouseout',function(){ //mouseout為滑鼠移開後做函數事件
  this.src = 'img1 example.jpg' //更換照片
})



