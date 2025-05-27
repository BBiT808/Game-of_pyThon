// 매개변수
//function (a,b,c,d) {}

function fn (arr) {
    console.log(arr)
}
fn(1,2)  // 1


function fn (...arr) {  // 나머지 매개변수로 묶어주는 역할 !!
    console.log(...arr) // 전개연산자
}
fn(1,2)
fn(1,2,3,4,5,6)