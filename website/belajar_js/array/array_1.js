// Method 1: push
// Menambahkan satu atau lebih elemen ke akhir array dan mengembalikan panjang array yang baru.
var array = ["banana","apple","anggur","mangga","bakso"]
var penggabungan = array.push("puding")
console.log(array)

// Method 2: splice
// Mengubah konten array dengan menghapus atau mengganti elemen yang ada dan/atau menambah elemen baru di tempat.
var hapus = array.splice(2,2)
console.log(array)

// Method 3: concat
// Menggabungkan dua atau lebih array dan mengembalikan array baru.
// var array1 = ["a", "b", "c"];
// var array2 = ["d", "e", "f"];
// var newArray = array1.concat(array2);
// console.log(newArray);

// // Method 4: every
// // Memeriksa apakah semua elemen dalam array memenuhi kondisi yang diberikan.
// var isBelowThreshold = function (currentValue) {
//   return currentValue < 40;
// };
// var array3 = [1, 30, 39, 29, 10, 13];
// console.log(array3.every(isBelowThreshold));

// Method 5: filter
// Membuat array baru dengan semua elemen yang lulus uji yang diberikan.
var words = ["spray", "limit", "elite", "exuberant", "destruction", "present"];
var result = words.filter(word => word.length > 6)
console.log(result)




// // Method 6: find
// // Mengembalikan nilai elemen pertama dalam array yang memenuhi kondisi yang diberikan.
// var array4 = [5, 12, 8, 130, 44];
// var found = array4.find(element => element > 10);
// console.log(found);

// // Method 7: findIndex
// // Mengembalikan indeks elemen pertama dalam array yang memenuhi kondisi yang diberikan.
// var array5 = [5, 12, 8, 130, 44];
// var foundIndex = array5.findIndex(element => element > 10);
// console.log(foundIndex);

// // Method 8: forEach
// // Memanggil fungsi yang diberikan untuk setiap elemen dalam array.
// var array6 = [1, 4, 9, 16];
// array6.forEach((element, index, array) => {
//   console.log(element, index, array);
// });

// // Method 9: includes
// // Memeriksa apakah array berisi elemen yang diberikan.
// var array7 = [1, 2, 3];
// console.log(array7.includes(2));

// // Method 10: indexOf
// // Mengembalikan indeks pertama dari elemen yang diberikan dalam array.
// var beasts = ['ant', 'bison', 'camel', 'duck', 'bison'];
// console.log(beasts.indexOf('bison'));

// // Method 11: join
// // Menggabungkan semua elemen array menjadi string.
// var elements = ['Fire', 'Air', 'Water'];
// console.log(elements.join());

// // Method 12: lastIndexOf
// // Mengembalikan indeks terakhir dari elemen yang diberikan dalam array.
// var animals = ['Dodo', 'Tiger', 'Penguin', 'Dodo'];
// console.log(animals.lastIndexOf('Dodo'));

// // Method 13: map
// // Membuat array baru dengan hasil pemanggilan fungsi yang diberikan pada setiap elemen dalam array.
// var array8 = [1, 4, 9, 16];
// var map1 = array8.map(x => x * 2);
// console.log(map1);

// // Method 14: pop
// // Menghapus elemen terakhir dari array dan mengembalikan elemen tersebut.
// var array9 = [1, 2, 3];
// console.log(array9.pop());

// // Method 15: push
// // Menambahkan satu atau lebih elemen ke akhir array dan mengembalikan panjang array yang baru.
// var array10 = [1, 2, 3];
// console.log(array10.push(4, 5, 6));

// // Method 16: reduce
// // Menerapkan fungsi yang diberikan pada setiap elemen dalam array untuk mengurangi array menjadi satu nilai.
// var array11 = [1, 2, 3, 4];
// var reducer = (accumulator, currentValue) => accumulator + currentValue;
// console.log(array11.reduce(reducer));

// // Method 17: reduceRight
// // Menerapkan fungsi yang diberikan pada setiap elemen dalam array untuk mengurangi array menjadi satu nilai, dimulai dari kanan.
// var array12 = [1, 2, 3, 4];
// var reducerRight = (accumulator, currentValue) => accumulator + currentValue;
// console.log(array12.reduceRight(reducerRight));

// // Method 18: reverse
// // Membalikkan urutan elemen dalam array.
// var array13 = [1, 2, 3, 4, 5];
// console.log(array13.reverse());

// // Method 19: shift
// // Menghapus elemen pertama dari array dan mengembalikan elemen tersebut.
// var array14 = [1, 2, 3];
// console.log(array14.shift());

// // Method 20: slice
// // Mengembalikan bagian dari array tanpa mengubah array asli.
// var array15 = [1, 2, 3, 4, 5];
// console.log(array15.slice(2, 4));

// // Method 21: some
// // Memeriksa apakah setidaknya satu elemen dalam array memenuhi kondisi yang diberikan.
// var array16 = [1, 2, 3, 4, 5];
// var even = (element) => element % 2 === 0;
// console.log(array16.some(even));

// // Method 22: sort
// // Mengurutkan elemen dalam array.
// var array17 = [1, 2, 3, 4, 5];
// console.log(array17.sort());

// // Method 23: splice
// // Mengubah konten array dengan menghapus atau mengganti elemen yang ada dan/atau menambah elemen baru di tempat.
// var array18 = [1, 2, 3, 4, 5];
// console.log(array18.splice(2, 0, 6, 7));

// // Method 24: toString
// // Mengembalikan string yang mewakili array.
// var array19 = [1, 2, 3, 4, 5];
// console.log(array19.toString());

// // Method 25: unshift
// // Menambahkan satu atau lebih elemen ke awal array dan mengembalikan panjang array yang baru.
// var array20 = [1, 2, 3, 4, 5];
// console.log(array20.unshift(0));

// // Method 26: valueOf
// // Mengembalikan nilai primitif dari array.
// var array21 = [1, 2, 3, 4, 5];
// console.log(array21.valueOf());

// // Method 27: concat
// // Menggabungkan dua atau lebih array dan mengembalikan array baru.
// var array22 = [1, 2, 3];
// var array23 = [4, 5, 6];
// console.log(array22.concat(array23));

// // Method 28: copyWithin
// // Menyalin sebagian array ke lokasi lain dalam array, tanpa mengubah panjangnya.
// var array24 = [1, 2, 3, 4, 5];
// console.log(array24.copyWithin(0, 3, 4));

// // Method 29: entries
// // Mengembalikan iterator yang berisi pasangan [indeks, nilai] untuk setiap elemen dalam array.
// var array25 = [1, 2, 3, 4, 5];
// var iterator = array25.entries();
// for (let entry of iterator) {
//   console.log(entry);
// }

// // Method 30: every
// // Memeriksa apakah semua elemen dalam array memenuhi kondisi yang diberikan.
// var array26 = [1, 2, 3, 4, 5];
// var isBelowThreshold = (currentValue) => currentValue < 40;
// console.log(array26.every(isBelowThreshold));

// // Method 31: fill
// // Mengisi semua elemen dalam array dengan nilai yang diberikan.
// var array27 = [1, 2, 3, 4, 5];
// console.log(array27.fill(0, 2, 4));

// // Method 32: filter
// // Membuat array baru dengan semua elemen yang lulus uji yang diberikan.
// var array28 = [1, 2, 3, 4, 5];
// var even = (element) => element % 2 === 0;
// console.log(array28.filter(even));

// // Method 33: find
// // Mengembalikan nilai elemen pertama dalam array yang memenuhi kondisi yang diberikan.
// var array29 = [1, 2, 3, 4, 5];
// var isLargeNumber = (element) => element > 13;
// console.log(array29.find(isLargeNumber));

// // Method 34: findIndex
// // Mengembalikan indeks elemen pertama dalam array yang memenuhi kondisi yang diberikan.
// var array30 = [1, 2, 3, 4, 5];
// var isLargeNumber = (element) => element > 13;
// console.log(array30.findIndex(isLargeNumber));

// // Method 35: forEach
// // Memanggil fungsi yang diberikan untuk setiap elemen dalam array.
// var array31 = [1, 2, 3, 4, 5];
// array31.forEach(element => console.log(element));

// // Method 36: from
// // Membuat array baru dari objek yang dapat diiterasi.
// var array32 = Array.from('foo');
// console.log(array32);

// // Method 37: includes
// // Memeriksa apakah array berisi elemen yang diberikan.
// var array33 = [1, 2, 3, 4, 5];
// console.log(array33.includes(2));

// // Method 38: indexOf
// // Mengembalikan indeks pertama dari elemen yang diberikan dalam array.
// var array34 = [1, 2, 3, 4, 5];
// console.log(array34.indexOf(2));

// // Method 39: isArray
// // Memeriksa apakah nilai yang diberikan adalah array.
// console.log(Array.isArray([1, 2, 3, 4, 5]));

// // Method 40: join
// // Menggabungkan semua elemen array menjadi string.
// var array35 = [1, 2, 3, 4, 5];
// console.log(array35.join());

// // Method 41: keys
// // Mengembalikan iterator yang berisi indeks untuk setiap elemen dalam array.
// var array36 = [1, 2, 3, 4, 5];
// var iterator = array36.keys();
// for (let key of iterator) {
//   console.log(key);
// }

// // Method 42: lastIndexOf
// // Mengembalikan indeks terakhir dari elemen yang diberikan dalam array.
// var array37 = [2, 5, 9, 2];
// console.log(array37.lastIndexOf(2));

// // Method 43: map
// // Membuat array baru dengan hasil pemanggilan fungsi yang diberikan pada setiap elemen dalam array.
// var array38 = [1, 4, 9, 16];
// var map1 = array38.map(x => x * 2);
// console.log(map1);

// // Method 44: pop
// // Menghapus elemen terakhir dari array dan mengembalikan elemen tersebut.
// var array39 = [1, 2, 3, 4, 5];
// console.log(array39.pop());

// // Method 45: push
// // Menambahkan satu atau lebih elemen ke akhir array dan mengembalikan panjang array yang baru.
// var array40 = [1, 2, 3];
// console.log(array40.push(4, 5, 6));

// // Method 46: reduce
// // Menerapkan fungsi yang diberikan pada setiap elemen dalam array untuk mengurangi array menjadi satu nilai.
// var array41 = [1, 2, 3, 4];
// var reducer = (accumulator, currentValue) => accumulator + currentValue;
// console.log(array41.reduce(reducer));

// // Method 47: reduceRight
// // Menerapkan fungsi yang diberikan pada setiap elemen dalam array untuk mengurangi array menjadi satu nilai, dimulai dari kanan.
// var array42 = [1, 2, 3, 4];
// var reducerRight = (accumulator, currentValue) => accumulator + currentValue;
// console.log(array42.reduceRight(reducerRight));

// // Method 48: reverse
// // Membalikkan urutan elemen dalam array.
// var array43 = [1, 2, 3, 4, 5];
// console.log(array43.reverse());

// // Method 49: shift
// // Menghapus elemen pertama dari array dan mengembalikan elemen tersebut.
// var array44 = [1, 2, 3];
// console.log(array44.shift());

// // Method 50: slice
// // Mengembalikan bagian dari array tanpa mengubah array asli.
// var array45 = [1, 2, 3, 4, 5];
// console.log(array45.slice(2, 4));

// // Method 51: some
// // Memeriksa apakah setidaknya satu elemen dalam array memenuhi kondisi yang diberikan.
// var array46 = [1, 2, 3, 4, 5];
// var even = (element) => element % 2 === 0;
// console.log(array46.some(even));

// // Method 52: sort
// // Mengurutkan elemen dalam array.
// var array47 = [1, 2, 3, 4, 5];
// console.log(array47.sort());

// // Method 53: splice
// // Mengubah konten array dengan menghapus atau mengganti elemen yang ada dan/atau menambah elemen baru di tempat.
// var array48 = [1, 2, 3, 4, 5];
// console.log(array48.splice(2, 0, 6, 7));

// // Method 54: toString
// // Mengembalikan string yang mewakili array.
// var array49 = [1, 2, 3, 4, 5];
// console.log(array49.toString());

// // Method 55: unshift
// // Menambahkan satu atau lebih elemen ke awal array dan mengembalikan panjang array yang baru.
// var array50 = [1, 2, 3, 4, 5];
// console.log(array50.unshift(0));

// // Method 56: valueOf
// // Mengembalikan nilai primitif dari array.
// var array51 = [1, 2, 3, 4, 5];
// console.log(array51.valueOf());


var baso = [1,2,3,4,5,6]


var hasil = baso.forEach(function(name) {
    console.log(name)
})
var hapus = baso.pop()
console.log(hapus)

for(var bas = 0; bas < baso.length; bas++) {
    console.log(bas)
}

// penggunaan every 
var arr = [10,20,30,40,39]
var hasil = function(everyDay) {
    return everyDay < 16
}
var hasil = arr.every(hasil)=
console.log(hasil)

// pengggunaan find
var hasil_1 = function(baso) {
    return baso > 11
}
var hasbin = arr.find(hasil_1)
console.log(hasbin)