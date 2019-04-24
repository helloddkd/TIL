const numbers = [1,2,3,4];

numbers[0];
numbers[-1];
numbers.length;

numbers.reverse();
numbers.push('a'); // new length 리턴

numbers.pop();
numbers.unshift('a'); //newlength 반환
numbers.shift('a') // Q처럼 앞에서 꺼내기
numbers.includes(searchElement:1); //true
numbers.includes(searchElement:0); // False

numbers.indexOf('b') // -1 없다는 뜻

[1,2,3,4].join(' '); // 1 2 3 4

numbers.shift('a')