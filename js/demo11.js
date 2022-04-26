class car{
  constructor(initName){
    this.name = initName
  }
  start(){
    console.log('車子啟動')
  }
}

//繼承
class porsche extends car{ //在class中,(子) extends(繼承) (父)
  constructor(namePoresche){
    super(namePoresche) //繼承後物件使用super()來繼承
  }
  start1(){
    super.start() //繼承函數使用super.函數()來繼承
    console.log('車子排氣')
  }
}

const c1 = new porsche('JOJO的保時捷') //此時變數建構的class物件為繼承的子物件

console.log(c1.name) //因c1建造的class是繼承的子物件,所以可以使用父的物件
c1.start() //因c1建造的class是繼承的子物件,所以可以使用父的函數
c1.start1() //因start1函數有使用super來繼承因此會先做完繼承的事情在做自己的事件
/*
  若在porsche也可寫入start()函數,並且使用super.start()繼承
  可以呼叫父函數後做自己的事件
*/