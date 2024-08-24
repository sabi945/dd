// let button = 'anda berhasil login'
// const Panggil_button = document.getElementById('btn')
// const body = document.body

// Panggil_button.style.padding = '8px'
// Panggil_button.style.border = 'none'
// Panggil_button.style.background = 'tomato'

// function Login() {
//     Panggil_button.style.background = 'aqua'
// }
// function perubahan() {
//     Panggil_button.textContent = 'kamu berhasil'
//     Panggil_button.style.background = 'aqua'
// }
// function out() {
//     Panggil_button.textContent = 'kalik satu'
//     Panggil_button.style.background = 'tomato'
    
// }
// let confir = confirm('apakah kamu sudah makan?')
// if (confir == true){
//     alert('baiklah kalau kamu sudah makan')
// }

// let year = 2004
// let hasil = (year == 2005)
// if (hasil) {
//     alert("kamu berhasil yey")
// }
// let ternary = (year == 2005) ? alert("kamu sangat beruntung") : alert("yah kamu kurang beruntung")


// function call(text,func,fun_1) {
//     if (confirm(text)) func()
//     else fun_1()
// }

// // function text() {
// //     alert('kamu sudah berhasil yeay')
// // }
// // function text_1() {
// //     alert('yah sayang nya kamu salah deeh')
// // }
// call(
//     "apakah kamu masuk hari ini?",
//     function() { alert("yeay kamu sudah berhasil?")},
//     function() { alert("semoga lekas sembh ya uhuy")}                                   
//     )

// function gret(name) {
//     name('baso')
// }
// gret(function(name) {
//     alert(`halo ${name}`)
// })   

// percobaan mengambil karakter sesuai index
// const hasil = "halo nama baso"
// const perubahan = hasil.charAt(0)
// console.log(perubahan)

// // menggabungkan sebah sting    

// const stringg = "halo"
// const stringg_1 = "baso"
// const hasil_1 = stringg.concat(" ", stringg_1 )
// console.log(hasil_1)

// // untuk code uniqode 
// const uniqode = String.fromCharCode(U+OCA4)
// console.log(uniqode)

// function greet(name) {
//     return this.greeting +  ", " + name 
// }

// var person = {
//     greeting: "halo"
// }

// var hasil = greet.apply(person, ["baso"])
// console.log(hasil)
// Fungsi untuk menyapa seseorang
function greet(firstName, lastName) {
    console.log(this.firstName + " " + "Halo, " + firstName + " " + lastName + "!");
  }
  
  // Memanggil fungsi greet dengan context objek 'person'
  const person = {
    firstName: "John",
    lastName: "Doe"
  };
  
  greet.apply(person, ["Alice", "Smith"]); // Output: Halo, Alice Smith!
  
  // Memanggil fungsi greet dengan context global (this menjadi wi
  var tanggal = new Date()
  var hasol = tanggal.getDate()
  var tahunIni = tanggal.getFullYear()
  =
  console.log(tahunIni)
  console.log(hasol)