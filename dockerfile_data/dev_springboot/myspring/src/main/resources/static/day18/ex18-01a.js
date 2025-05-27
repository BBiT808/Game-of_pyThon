const arr = [11,22,33,44,55]
console.log(arr)

// 웹브라우저에서 실행하는 것과 백엔드에서 실행하는 것을 구분해 줘야함 !!!

/* 옅은 복사 !!.... 보다는 참조 복사!!!! ; 주소만 복사되어서 겉보기만 ..!!*/ 
const arr2 = arr
arr[2] = 77
console.log(arr, arr2)
console.log(arr == arr2)
console.log(arr === arr2)

/* 깊은 복사 !!! ..... 보다는 옅은 복사 !!!! ; */
const srr = [66,77,88,99,0]
const arr3 = [...srr]  // 연계연산자 !!!
arr3[2] == 77
console.log(srr, arr3)
console.log(srr == arr3)
console.log(srr === arr3)

console.log(Math.max(1,2,3,4,11,22,33,44,77,34)) // 여기는 튜플이 없어!!! (튜플을 넣을 수 없어!!)
console.log(Math.max(arr))  //NaN
console.log(Math.max(...arr))   // 요로코롬 연계연산자를 이용하면 튜플도 소환 가능 !!!
console.log(Math.min(...arr))
