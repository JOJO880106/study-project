/*
  js多行註解
*/
// js單行註解

/*
  js的變數分為:var、let、const
  var:全域,可多次宣告
  let:有區塊性,不可重複宣告
  const:有區塊性,不可重複宣告,並修改其值與型別(多用在array、object)
  let基本上已取代var,常用let、const
*/

//變數的個型別,string('jojo')、數字(23)、boolean(true、false)、空值(null、undefined)
let my_Name = 'jojo'
let my_Age = 23
let is_Male = true

//document.write,將()的內容顯示在網頁上
document.write('document.write示範')
document.write('<br/>') //可在js中換行
document.write(my_Name + my_Age + '歲' + is_Male)
document.write('<br/>')

my_Name = '陳jo'
document.write('變更變數的值:' + my_Name) //更換變數的值