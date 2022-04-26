//class
class phone{ //在class中可建構物件與函數
  constructor(number,year,is_waterproof){ //建構物件需使用constructor()
    //這裡的this則會在之後建構變數後跟隨變數物件
    this.number = number
    this.year = year
    this.is_waterproof = is_waterproof
  }
  phone_age(age){ //建構函數
    return age - this.year
  }
}

//設變數來建造class中的物件與函數需使用new來建構
const phone1 = new phone('123',2020,false)
const phone2 = new phone('456',2018,false)

console.log(phone1.phone_age(2021)) //呼叫phone1建造的class函數
console.log(phone1.number) //呼叫phone1建造的class物件
console.log(phone2.number) //呼叫phone1建造的class物件

//this
class card{
  constructor(initName){
    this.name = initName
  }
  hello(){
    console.log('hello ' + this.name)
  }
}

const c1 = new card('JOJO')
const c2 = {name:'陳JO'}
c2.hellooooo = c1.hello //c2的hellooooo函數等於c1的hello函數

c1.hello()
c2.hellooooo() //這裡的hello 陳JO是因為函數的this是跟著物件,而c2的物件name被改為陳JO

//綁定this方法(bind)
class card2{
  constructor(initName){
    this.name = initName
    this.hellooo = this.hello.bind(this) //用bind綁定this,先設定一個物件使它等於函數並用bind綁定(this)
  }
  hello(){
    console.log('hello ' + this.name)
  }
}

const c3 = new card2('JOJO')
const c4 = {name:'陳JO'} 
c4.hellooooo = c3.hellooo

c3.hellooo()
c4.hellooooo() //即使c4物件name為陳JO,this也因綁定而指向C3的物件name

//綁定this方法(箭頭函數)
class card3{
  constructor(initName){
    this.name = initName
  }
  hello=()=>{ //在函數使用箭頭函數撰寫,將會把this指定為外面一層的物件
    console.log('hello ' + this.name)
  }
}

const c5 = new card3('JOJO')
const c6 ={name:'陳JO'}
c6.hellooooo = c5.hello

c5.hello()
c6.hellooooo() //即使c6物件name為陳JO,this因箭頭函數指定外物件而指向c5的name
