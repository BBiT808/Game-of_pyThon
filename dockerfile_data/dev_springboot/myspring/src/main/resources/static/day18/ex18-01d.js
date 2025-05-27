const user = {name : "홍길동", age : 10}
// const updated = {age : 20}

// 객체의 키로 값을 읽는 법 : R
console.log(user.name)  // 평소에 잘 쓰는 법~
console.log(user['name'])  // 가~ 끔 위의 방법이 에러날 때 !!

// 객체를 수정하는 법  ; 대입 연산자 사용 ~ : C
user.gender = "male"
user['address'] = "부산"

// 수정하는 법  : U
user.age = 17
user['name'] = '슈퍼맨'

// 삭제하기 !! : D
delete user['gender']

// 출력하기
console.log(user)
// 근데 이런 방식으로 하면 렌더링이 안 된대 !!!!!!

// 새~로운 객체 문법!!!
// const test = {test} // {test:test}

const updated = { ...user, age:20}  // 업데이트를 하고 싶으면 이렇게 해야 해!!!
console.log(updated)


//참고
// const updated = {user, age : 20}  // 하나를 새로 만들어버림~
// console.log(updated)

