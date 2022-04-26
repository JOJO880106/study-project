const youtuberitem = [
  {
    id:221,
    name:'a',
    age:12
  },
  {
    id:222,
    name:'b',
    age:13
  },
  {
    id:223,
    name:'c',
    age:14
  },
  {
    id:224,
    name:'d',
    age:15
  }
]
//使用reduce()複製陣列中物件
const mapobj = youtuberitem.reduce(
  (accumulator,{id,name,age})=>({ //accumulator為累加{物件}
    ...accumulator, //...複製陣列中物件
    [`${id}`]:{name,age}, 
  }),
  {}
)

console.log(youtuberitem)
console.log(mapobj)
console.log(mapobj[221])