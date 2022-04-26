//問答題
const questions = [
  {
    prompt:'香蕉是甚麼顏色?\n(a)紅色\n(b)綠色\n(c)黃色', // \n能使文字換行
    answer:'c'
  },
  {
    prompt:'草莓是甚麼顏色?\n(a)紅色\n(b)綠色\n(c)黃色',
    answer:'a'
  },
  {
    prompt:'奇異果是甚麼顏色?\n(a)紅色\n(b)綠色\n(c)黃色',
    answer:'b'
  }
]

let score = 0

for(let i = 0; i < questions.length; i += 1){
  let input = prompt(questions[i].prompt)
  if(input === questions[i].answer){
    score += 1
    alert('答對了')
  }
  else{
    alert('答錯了')
  }
}
alert('總共答對' + score + '題')