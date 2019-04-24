//숫자로 이루어진 배열의 요소들을 각각 ?? 한다. ??는 알아서 해라
const EachNumber = (numbers, callback) => {
    let acc;
    for (const num of numbers) {
        acc = callback(num, acc)
    }
    return acc;
};

console.log(EachNumber([1,2,3,4,5], (number, sum=0) => sum+=number));


const muller = (number, sum=1) => {
    return sum *= number
}

const subber = (number, sum=0) => {
    return sum -= number
}

const adder = (number, sum=0) => {
    return sum += number
};

EachNumber([1,2,3,4,5], adder);


//인자로 배열을 받는다. 해당 배열의 모든 요소를 더한 숫자를 return


const AddEachNumber = numbers => {
    let acc = 0;
    for (const number of numbers) {
        acc += number;
    }
    return acc;
};

console.log(AddEachNumber([1,2,3,4,5]))


//인자로 배열을 받는다. 해당 배열의 모든 요소를 뺀 숫자를 return

const SubEachNumber = numbers => {
    let acc = 0;
    for (const number of numbers){       //for a of [asdfadsf]는 asdfadsf하나하나 in은 인덱스
        acc -= number;
    }
    return acc;
};

console.log(SubEachNumber([1,2,3,4,5]))

const MulEachNumber = numbers => {
    let acc = 1;
    for (const number of numbers){
        acc *= number;
    }
    return acc;
};


console.log(MulEachNumber([1,2,3,4,5]))



