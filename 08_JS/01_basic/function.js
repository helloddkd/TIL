//1. 함수 키워드 정의
function add(num1, num2) {
    return num1 + num2;
}

//2. 변수에 함수로직 할당
const sub = function(num1, num2) {
    return num1 - num2;
};

//3. 함수 표현식 2가지
const mul = function (num1, num2) {
    return num1 * num2;
};

/*
1. function 키워드를 없앤다.
2. ()와 {} 사이에 =>를 넣는다.
 */
//
// const mul = (num1, num2) => {
//     return num1 * num2;
// };

/*
1. 인자가 단 하나라면 괄호생략가능!
2. 함수 블록 안에 코드가 return문 한 줄이라면 {} & return 키워드 삭제가능!
 */

let square = function(num) {
    return num ** 2;
};

square = num => num**2;
square(3);

let noArgs = () => {
    return 'nothing'
};

noArgs = () => 'nothing';
manArgs = (a,b,c,d,e) => 'many';
oneArgs = a => 'one';

/*
Default Args
 */

function sayHello(name){
    return `hi ${name}`
}

const sayhello = (name='ssafy') => `hi ${name}`;

console.log(sayhello('지원'));

console.log((num => num**2)(4));
(check_long_str('hi')) ? console.log('long'): console.log('small');