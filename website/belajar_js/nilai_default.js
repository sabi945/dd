// ini adalah 
const object = {
    name: "baso",
    age: 10,
    baso() {
        console.log(this.name, "apa kabar")
    }
}

delete object.age
console.log(object.age)
object.baso()
// ini adalah prototype
var prototype = {
    basp: function() {
        console.log('halo kawan ku!')
    }
}
var hasil = Object.create(prototype)
hasil.basp()
// akhir

function basi(name, age) {
    this.baso = name
    this.siji = age
}

var bass = new basi("hallo",10)
console.log(bass.baso)

//create person
let obj = {
    _nama: "John",
    get nama() {
      return this._nama;
    }
  };
  
  console.log(obj.nama); // Output: "John"
          
var object_1 = {
    a: 1,
    b: 10
}

var object_2 = {
    b: 19,
    c: 20
}
function basii() {
    return this.b
}
let hasil_func = basii.call(object_1)
console.log(hasil_func)
var hasill = Object.assign(object_1,object_2)

